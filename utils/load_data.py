import pandas as pd
import sys

sys.path.append("../2022-cs-65dsamidproject")

from model.video import video


def load_data():
    df = pd.read_csv("Scraping/VideosINFO.csv", header=0)
    Videos = []
    for index, row in df.iterrows():
        url = row["Links"]
        channel = row["Channel"]
        subscribers = row["Subscribers"]
        title = row["Title"]
        likes = row["Likes"]
        duration = row["Duration"]
        views = row["Views"]
        comments = row["Comments"]
        v = video(url, channel, subscribers, title, likes, duration, views, comments)
        v.Validate()
        Videos.append(v)
    return Videos
