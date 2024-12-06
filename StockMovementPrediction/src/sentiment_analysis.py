from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    """Analyze sentiment polarity of text."""
    if isinstance(text, str):  # Ensure that the text is a string
        return TextBlob(text).sentiment.polarity
    else:
        return 0.0  # Return a neutral sentiment if the text is not a string

# Load Data
df = pd.read_csv(r"C:\Users\Administrator\Downloads\StockMovementPrediction\data\processed_data.csv")

# Ensure that 'Cleaned_Tweet' is a string and handle missing values
df['Cleaned_Tweet'] = df['Cleaned_Tweet'].fillna('').apply(str)

# Perform Sentiment Analysis
df['Sentiment'] = df['Cleaned_Tweet'].apply(analyze_sentiment)
df['Label'] = df['Sentiment'].apply(lambda x: 1 if x > 0 else 0)  # Binary classification

# Save the processed data
df.to_csv(r"C:\Users\Administrator\Downloads\StockMovementPrediction\data\processed_data1.csv", index=False)

print("Sentiment analysis completed and saved!")
