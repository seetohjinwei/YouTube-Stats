import pandas as pd
from re import compile, Pattern

pattern: Pattern = compile(r'(?<=watch\?v=)[a-zA-Z0-9-_]{11}')
with open("data", "r") as f:
    URLS = pattern.findall(f.read())
print(URLS)
df: pd.DataFrame = pd.concat(
    [pd.Series(URLS, name="URL").to_frame(),
     pd.DataFrame(columns=["URL", "Name", "Title", "Views", "Likes", "Dislikes", "Comments", "Like/Dislike", "Likes/Views"])]
)
df.to_csv("videos.csv", index=False)
import main  # call main
