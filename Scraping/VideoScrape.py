from time import sleep
import pandas as pd
import os
import emoji
from selenium import webdriver
from bs4 import BeautifulSoup


def scroll_to_comments_area():
    screen_height = driver.execute_script("return window.screen.height;")
    for i in range(2):
        driver.execute_script(f"window.scrollTo(0, {screen_height * 0.6});")
        sleep(1)


def extract_count_with_suffix(count_text):
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


def removeEmoji(text):
    return emoji.replace_emoji(text, replace="")


def ScrapVideo(videoLink, startingIndex):
    driver.get(videoLink)
    driver.maximize_window()
    scroll_to_comments_area()
    sleep(1)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # click ..more to see views and date
    try:
        show_more_button = driver.find_element("id", "expand")
        if show_more_button.is_displayed():
            show_more_button.click()
            sleep(1)
    except Exception as e:
        print(f"Error expanding description: {e}")

    try:
        title = soup.find(
            "h1", attrs={"class": "style-scope ytd-watch-metadata"}
        ).text.strip()
        title = removeEmoji(title)
    except AttributeError:
        title = "NA"

    try:
        channel_name = soup.find(
            "a", attrs={"class": "yt-simple-endpoint style-scope yt-formatted-string"}
        )
        channel_name = channel_name and channel_name.text.strip("\n")
    except AttributeError:
        channel_name = "NA"

    try:
        sub_count_text = soup.find(
            "yt-formatted-string", {"id": "owner-sub-count"}
        ).text.strip("subscribers")
        sub_count = extract_count_with_suffix(sub_count_text)
    except AttributeError:
        sub_count = "NA"

    try:
        like_count_text = (
            soup.find("div", {"id": "segmented-like-button"})
            .find("span", {"class": "yt-core-attributed-string"})
            .text
        )
        like_count = extract_count_with_suffix(like_count_text)
    except AttributeError:
        like_count = "NA"

    try:
        comment_count_text = soup.find(
            "yt-formatted-string",
            {"class": "count-text style-scope ytd-comments-header-renderer"},
        ).text.strip("Comments")
        comment_count = int(comment_count_text.replace(",", ""))
    except AttributeError:
        comment_count = "NA"

    try:
        duration = soup.find("span", attrs={"class": "ytp-time-duration"}).text
    except AttributeError:
        duration = "NA"

    try:
        views = soup.find("yt-formatted-string", {"id": "info"}).text.strip()
        both = views.split("views")
        # split the views
        view_count_text = both[0]
        # date = both[1].split("ago")[0]
        view_count = extract_count_with_suffix(view_count_text)
    except AttributeError:
        view_count = "NA"
        # date = "NA"

    video_data = {
        "Links": videoLink,
        "Channel": channel_name,
        "Subscribers": sub_count,
        "Title": title,
        "Likes": like_count,
        "Duration": duration,
        "Views": view_count,
        "Comments": comment_count,
    }

    # write the data of one video in file
    df = pd.DataFrame([video_data])
    df.to_csv("Scraping/VideosINFO.csv", mode="a", header=False, index=False)

    f = open(file="Scraping/progress.txt", mode="w")
    f.write(str(startingIndex) + "\n")


def loadLinksFromFile():
    # reading all videos links from csv
    df = pd.read_csv("Scraping/VideosURL.csv", header=None)
    allUrls = df[0].values.tolist()
    return allUrls


def loadProgess(filename):
    given_file = open(file=filename, mode="r")
    lines = given_file.read()
    numbers = []
    arr = lines.split()
    for s in arr:
        num = int(s)
        numbers.append(num)
    return numbers[0]


def start_scraping():
    # store all urls in list
    urls_list = loadLinksFromFile()
    startingIndex = loadProgess("Scraping/progress.txt")

    urls_list = urls_list[startingIndex:65001]

    # Check if the output file already exists
    fieldnames = [
        "Links",
        "Channel",
        "Subscribers",
        "Title",
        "Likes",
        "Duration",
        "Views",
        "Comments",
    ]
    if not os.path.exists("Scraping/VideosINFO.csv"):
        pd.DataFrame(columns=fieldnames).to_csv("Scraping/VideosINFO.csv", index=False)
    # scrap data from each video in list
    for url in urls_list:
        startingIndex += 1
        ScrapVideo(url, startingIndex)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--blink-settings=imagesEnabled=false")  # Disable media
    driver = webdriver.Chrome(options=options)
    start_scraping()
