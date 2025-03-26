import pandas as pd, nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze(fp="../data/reddit.csv"):
    df = pd.read_csv(fp)
    df["sent"] = df["txt"].fillna("").apply(lambda t: sia.polarity_scores(t)["compound"])
    df.to_csv("../data/reddit_analyzed.csv", index=False)

if __name__ == "__main__":
    analyze()
