from dataclasses import dataclass
from googleapiclient.discovery import build
import pandas as pd
from re import compile


@dataclass
class Video:
    ID: str
    Title: str
    Views: float
    Likes: float
    Dislikes: float
    Comments: str


class YouTube:
    def __init__(self, api_key) -> None:
        self.build = build("youtube", "v3", developerKey=api_key)

    def get_data(self, videoID: str):
        try:
            video = self.build.videos().list(part="statistics", id=videoID).execute()
            title: str = (
                self.build.videos()
                .list(part="snippet", id=videoID)
                .execute()["items"][0]["snippet"]["title"]
            )
            stats = video["items"][0]["statistics"]
        except IndexError:
            print(f"Invalid link skipped: {videoID}")
            return None
        return Video(
            videoID,
            title,
            float(stats["viewCount"]),
            float(stats["likeCount"]),
            float(stats["dislikeCount"]),
            stats["commentCount"],
        )


def main(API_KEY: str):
    youtube: YouTube = YouTube(api_key=API_KEY)
    df: pd.DataFrame = pd.read_csv("videos.csv", index_col=False, dtype=str)
    for index, row in df.iterrows():
        video: Video = youtube.get_data(row["URL"])
        if not video:
            continue
        df.at[index, "Title"] = video.Title
        df.at[index, "Views"] = video.Views
        df.at[index, "Likes"] = video.Likes
        df.at[index, "Dislikes"] = video.Dislikes
        df.at[index, "Comments"] = video.Comments
        df.at[index, "Like/Dislike"] = video.Likes / video.Dislikes
        df.at[index, "Likes/Views"] = video.Likes / video.Views
    print(
        df[
            [
                "Name",
                "Views",
                "Likes",
                "Dislikes",
                "Comments",
                "Like/Dislike",
                "Likes/Views",
                "Title",
            ]
        ]
    )
    df.to_csv("videos.csv", index=False)


API_KEY: str = "XXX"  # put API key here (make sure there are quotes)
main(API_KEY)
