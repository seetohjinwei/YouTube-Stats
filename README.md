# YouTube Stats
Built by See Toh Jin Wei

Grabs links from CSV (or plaintext) and updates information into same CSV.

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
3. Paste a YouTube video URL (only the ID portion) on a separate line each
4. [Optional] Add a name to a video by adding `,NAME` to the end of the url
5. Run `main.py` with `videos.csv` in the same folder.

Example: `gjyEcSim4js,Cool Music`

To use parser:
1. Copy paste as many YouTube links as needed in the `data` file in plaintext. `youtu.be` links **not** supported.
2. Can have irrelevant text inside. Only YouTube links will be detected.
3. Run `parse.py` with `main.py` and `videos.csv` in the same folder.
