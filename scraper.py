import praw, pandas as pd
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

r = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

def scrape(sr="entrepreneur", lmt=100):
    s = r.subreddit(sr)
    d = [{"title": p.title, "txt": p.selftext, "s": p.score} for p in s.hot(limit=lmt)]
    pd.DataFrame(d).to_csv("../data/reddit.csv", index=False)

if __name__ == "__main__":
    scrape()
