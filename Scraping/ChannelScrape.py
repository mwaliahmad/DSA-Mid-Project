from selenium import webdriver
import pandas as pd
import time


def main():
    start_time = time.time()

    urls = LoadChannels()  # get channels urls from file
    NewURLs = AddVideotoURL(urls)  # change tab of channel to /videos
    NewURLs = NewURLs[54:61]  # for testing

    # scrape videos links
    for url in NewURLs:
        GetVideosLink(url)

    end_time = time.time()

    print(end_time - start_time)


def LoadChannels():
    df = pd.read_csv("Scraping/ChannelsURL.csv", header=None)
    channels = df[0].tolist()
    return channels


def GetVideosLink(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--blink-settings=imagesEnabled=false")  # Disable images
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.maximize_window()  # maximize the browser
    CurrentHeight = driver.execute_script(
        "return window.screen.height;"
    )  # get screen height

    # MaxHeight = driver.execute_script(  # get max height of the page
    #     """
    #         function MaxHeight(){
    #             return Math.max(
    #                 Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
    #                 Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
    #                 Math.max(document.body.clientHeight, document.documentElement.clientHeight)
    #             );
    #         }
    #         return MaxHeight();
    #     """
    # )

    # scroll window in order to load videos
    try:
        for i in range(1, 501):
            driver.execute_script(f"window.scrollTo(0, {CurrentHeight * i});")
            time.sleep(3)
    except:
        return
    finally:
        # get all <a> tags from the channels
        videos = driver.find_elements("xpath", '//*[@id="video-title-link"]')
        SavetoFile(videos)
        driver.quit()


def AddVideotoURL(URLs):
    newURLs = []
    for i in URLs:
        newURLs.append(i + "/videos")
    return newURLs


# extract links from <a> tags and save to csv file
def SavetoFile(videos):
    for i in videos:
        link = i.get_attribute("href")
        if link is not None:
            df = pd.DataFrame([link])
            df.to_csv(
                "Scraping/Data/VideosURL54to60.csv",
                index=False,
                encoding="utf-8",
                header=False,
                mode="a",
            )


if __name__ == "__main__":
    main()
