# market_gap_anlyzr
Scrapes forums & social media for unmet needs using NLP.

market-gap-analyzer/
│── data/                     # Stores raw & processed data
│── models/                   # Trained NLP models (optional)
│── notebooks/                # Jupyter Notebooks for exploration
│── src/                      # Source code
│   │── scraper.py            # Reddit scraping script
│   │── nlp_analysis.py       # NLP & sentiment analysis
│   │── insights.py           # Market gap detection logic
│   │── config.py             # API keys & settings (add to .gitignore)
│── dashboard/                # Future dashboard UI (Streamlit)
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
│── .gitignore                # Ignore unnecessary files

---

###  `requirements.txt`
praw
numpy
pandas
nltk
transformers
scikit-learn
torch

