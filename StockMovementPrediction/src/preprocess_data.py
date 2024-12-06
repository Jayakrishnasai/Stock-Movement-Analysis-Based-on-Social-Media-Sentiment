import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """Clean text data."""
    text = re.sub(r"http\S+|@\S+|#\S+", "", text)  # Remove URLs, mentions, hashtags
    text = re.sub(r"[^a-zA-Z\s]", "", text)       # Remove special characters
    text = " ".join([word.lower() for word in text.split() if word.lower() not in stop_words])
    return text

# Load Data
df = pd.read_csv(r"C:\Users\Administrator\Downloads\StockMovementPrediction\data\tweets.csv")

# Clean Data
df['Cleaned_Tweet'] = df['Tweet Content'].apply(clean_text)

# Save cleaned data
df.to_csv(r"C:\Users\Administrator\Downloads\StockMovementPrediction\data\processed_data.csv", index=False)
print("Data cleaned and saved!")
