import pandas as pd

def extract(fp="../data/reddit_analyzed.csv"):
    df = pd.read_csv(fp)
    neg = df[df["sent"] < -0.2]
    kw = ["problem", "issue", "struggle", "need", "wish", "can't find", "frustrated"]
    gaps = neg[neg["txt"].str.contains("|".join(kw), na=False, case=False)]
    gaps.to_csv("../data/market_gaps.csv", index=False)

if __name__ == "__main__":
    extract()
