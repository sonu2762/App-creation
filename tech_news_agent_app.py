
import streamlit as st
import feedparser
from datetime import datetime

# --------------------
# Config
# --------------------
st.set_page_config(page_title="Tech News Agent", layout="centered")

# --------------------
# App Title
# --------------------
st.title("🧠 Tech News Agent Dashboard")
st.markdown("Stay updated with the latest in **AI**, **AWS**, **Databricks**, and **Zero ETL**.")

# --------------------
# RSS Feed Sources
# --------------------
feeds = {
    "AWS": "https://aws.amazon.com/blogs/big-data/feed/",
    "Databricks": "https://www.databricks.com/blog.rss",
    "AI/ML News": "https://www.topbots.com/feed/",
    "arXiv AI": "http://export.arxiv.org/rss/cs.AI"
}

# --------------------
# Keywords
# --------------------
default_keywords = ["AI", "machine learning", "AWS", "Databricks", "Zero ETL", "Lakehouse", "Data Engineering"]
user_keywords = st.multiselect("🔍 Filter by keywords", default_keywords, default=default_keywords)

# --------------------
# Fetch News
# --------------------
def fetch_news():
    news_items = []
    for source, url in feeds.items():
        parsed = feedparser.parse(url)
        for entry in parsed.entries[:8]:
            if any(keyword.lower() in entry.title.lower() for keyword in user_keywords):
                news_items.append({
                    "source": source,
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.get("published", "N/A")
                })
    return news_items

if st.button("🔄 Refresh News"):
    st.experimental_rerun()

news = fetch_news()

st.markdown(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# --------------------
# Display News
# --------------------
if news:
    for item in news:
        st.markdown(f"### 🔹 {item['title']}")
        st.markdown(f"*Source:* {item['source']} | *Published:* {item['published']}")
        st.markdown(f"[Read More]({item['link']})")
        st.markdown("---")
else:
    st.info("No news found for the selected keywords.")
