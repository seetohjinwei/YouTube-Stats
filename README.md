# YouTube Stats
Built by See Toh Jin Wei

Polls links from CSV and updates into same CSV.

Grabs the following data:
1. Title
2. Views
3. Likes
4. Dislikes
5. Comments
6. Likes/Dislikes Ratio
7. Likes/Views Ratio

Requirements:
1. Python 3.7.1+ (Only tested on Python 3.9.6)
2. Install Google Data API libraries from <a href="https://developers.google.com/youtube/v3/quickstart/python">link</a>.
3. Install `pandas` from <a href="https://pandas.pydata.org/docs/getting_started/install.html">link</a>.
4. Google Data API Key <a href="https://console.cloud.google.com">link</a>.

Instructions to use:
1. Download `main.py` and `videos.csv`
2. Add your API key onto line 53 (near the end) of `main.py`
3. Paste a YouTube video URL on a separate line each
4. [Optional] Add a name to a video by adding `,NAME` to the end of the url

Example: `https://www.youtube.com/watch?v=gjyEcSim4js,Cool Video`
