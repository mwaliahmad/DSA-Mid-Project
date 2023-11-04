from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
from selenium import webdriver
from bs4 import BeautifulSoup


class StatThread(QThread):
    def __init__(self, links):
        super().__init__()
        self.links = links
        self.data = []

    def run(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--blink-settings=imagesEnabled=false")  # Disable media
        self.driver = webdriver.Chrome(options=options)
        urls_list = self.links
        # scrap data from each video in list
        for url in urls_list:
            video = self.ScrapVideo(url)
            self.data.append(video)
        self.driver.quit()
        return self.data

    def scroll_to_comments_area(self):
        screen_height = self.driver.execute_script("return window.screen.height;")
        for i in range(2):
            self.driver.execute_script(f"window.scrollTo(0, {screen_height * 0.6});")
            time.sleep(1)

    def extract_count_with_suffix(self, count_text):
        try:
            if "K" in count_text:
                like_count = int(float(count_text.replace("K", "").strip()) * 1000)
            elif "M" in count_text:
                like_count = int(float(count_text.replace("M", "").strip()) * 1000000)
            else:
                like_count = int(count_text)
            return like_count
        except ValueError:
            return "NA"

    def ScrapVideo(self, videoLink):
        self.driver.get(videoLink)
        self.driver.maximize_window()
        self.scroll_to_comments_area()
        time.sleep(1)
        content = self.driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        # click ..more to see views and date
        try:
            show_more_button = self.driver.find_element("id", "expand")
            if show_more_button.is_displayed():
                show_more_button.click()
                time.sleep(1)
        except Exception as e:
            print(f"Error expanding description: {e}")

        try:
            sub_count_text = soup.find(
                "yt-formatted-string", {"id": "owner-sub-count"}
            ).text.strip("subscribers")
            sub_count = self.extract_count_with_suffix(sub_count_text)
        except AttributeError:
            sub_count = 0

        try:
            like_count_text = (
                soup.find("div", {"id": "segmented-like-button"})
                .find("span", {"class": "yt-core-attributed-string"})
                .text
            )
            like_count = self.extract_count_with_suffix(like_count_text)
        except AttributeError:
            like_count = 0

        try:
            comment_count_text = soup.find(
                "yt-formatted-string",
                {"class": "count-text style-scope ytd-comments-header-renderer"},
            ).text.strip("Comments")
            comment_count = int(comment_count_text.replace(",", ""))
        except AttributeError:
            comment_count = 0

        try:
            duration = soup.find("span", attrs={"class": "ytp-time-duration"}).text
        except AttributeError:
            duration = 0

        try:
            views = soup.find("yt-formatted-string", {"id": "info"}).text.strip()
            both = views.split("views")
            # split the views
            view_count_text = both[0]
            # date = both[1].split("ago")[0]
            view_count = self.extract_count_with_suffix(view_count_text)
        except AttributeError:
            view_count = 0
            # date = "NA"

        video_data = [
            sub_count,
            like_count,
            self.Duration_conversion(duration),
            view_count,
            comment_count,
        ]
        return video_data

    def Duration_conversion(self, Duration):
        count = 0
        time = 0
        for i in Duration:
            if i == ":":
                count += 1
        if count > 0:
            Duration = Duration.split(":")
            if count == 2:
                time = (
                    int(Duration[0]) * 3600 + int(Duration[1]) * 60 + int(Duration[2])
                )
            else:
                time = int(Duration[0]) * 60 + int(Duration[1])
        return time
