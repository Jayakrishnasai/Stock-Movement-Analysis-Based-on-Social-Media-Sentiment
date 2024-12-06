# Stock-Movement-Analysis-Based-on-Social-Media-Sentiment

# Stock Movement Prediction

## Overview
Stock movements are influenced by various factors, including social media sentiment. This project develops a machine learning model to predict stock price trends by analyzing user-generated content from social platforms like Twitter and Reddit. 

The project demonstrates:
- **Data Scraping**: Collecting stock-related discussions.
- **Preprocessing and Feature Extraction**: Cleaning data and extracting relevant features.
- **Prediction Modeling**: Using machine learning to forecast stock price movements.

## Repository Structure
StockMovementPrediction_repo/
├── scraper/              # Scripts for scraping social media data
├── model/                # Scripts for model training and evaluation
├── notebooks/            # Jupyter notebooks for demonstrations
├── data/
│   ├── raw/              # Raw data files
│   └── processed/        # Processed data ready for analysis
└── README.md             # Project documentation

# HOW TO RUN PROJECT
To run your **Stock Movement Prediction** project with Twitter API data scraping (using a **bearer token**), here’s a step-by-step guide on how to proceed:

---

### **1. Setup Twitter API Access**
Before running the project, you need to set up your Twitter Developer credentials.

#### Steps to Get Twitter API Access:
1. Go to [Twitter Developer Portal](https://developer.twitter.com/).
2. Create a new **Twitter Developer App** and obtain:
   - **Bearer Token** (used for authentication in your scraping script).
3. Store the **Bearer Token** securely.

---

### **2. Install Required Dependencies**
Make sure you have the necessary dependencies installed, especially for Twitter scraping. You can install them by running:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include dependencies like:
```txt
tweepy
pandas
numpy
scikit-learn
tensorflow
beautifulsoup4
matplotlib
seaborn
```

---

### **3. Configuration of Bearer Token**
To use the Twitter API, the **bearer token** must be added to your scraping script.

#### Example:
If your scraping script uses the **Tweepy** library, you should authenticate it using the bearer token.

```python
import tweepy

# Set your Twitter API Bearer Token
bearer_token = "YOUR_TWITTER_BEARER_TOKEN"

# Authenticate to Twitter
client = tweepy.Client(bearer_token=bearer_token)

# Example: Scrape tweets related to stock movements
query = "stock market"
tweets = client.search_recent_tweets(query=query, max_results=100)

# Display the scraped tweets
for tweet in tweets.data:
    print(f"{tweet.text}")
```

Replace `"YOUR_TWITTER_BEARER_TOKEN"` with your actual bearer token.

---

### **4. Running the Scraper**
After configuring the API and dependencies, follow these steps:

#### **4.1 Run the Scraping Script**
1. Navigate to the `scraper/` directory:
   ```bash
   cd scraper/
   ```

2. Run your scraping script (replace `<scraping_script.py>` with the actual script file name):
   ```bash
   python <scraping_script.py>
   ```

   The script will use the Twitter API to scrape tweets related to stock movements and save them as raw data.

---

### **5. Preprocessing Data**
Once you have the scraped data (usually in `.csv`, `.json`, or `.txt` format), you’ll need to preprocess it. 

#### **5.1 Run the Preprocessing Script**
Navigate to the `model/` directory and run the preprocessing script:
```bash
cd model/
python preprocess_data.py
```

This script will clean the data and extract useful features for training the model.

---

### **6. Model Training**
After preprocessing, the data is ready to be used for training the model.

#### **6.1 Run the Model Training Script**
Navigate to the `model/` directory and run the model training script:
```bash
python train_model.py
```

This will train the machine learning model to predict stock movements based on the sentiment or other features extracted from the scraped data.

---

### **7. Evaluation**
Once the model is trained, you can evaluate it using various metrics such as accuracy, precision, and recall.

#### **7.1 Run the Model Evaluation Script**
If you have an evaluation script:
```bash
python evaluate_model.py
```

This will evaluate the model’s performance on the test data.

---

### **8. Jupyter Notebooks**
For easier visualization and understanding, you can run Jupyter notebooks that demonstrate each of the above steps (scraping, preprocessing, training, and evaluation).

#### **8.1 Run Jupyter Notebooks**
To launch Jupyter Notebooks, navigate to the `notebooks/` directory and run:

```bash
jupyter notebook
```

This will open a Jupyter notebook interface in your browser. You can open and run the notebooks to see the data scraping, preprocessing, training, and evaluation steps.

---

### **9. Final Thoughts**
- Make sure you replace placeholder values (like API keys, bearer tokens) with your actual credentials.
- Follow the steps in the order (scraping → preprocessing → model training → evaluation).

To run the **Stock Movement Prediction** project, which involves scraping Twitter data using the **Twitter API** and a **Bearer Token**, follow these detailed steps:

---
# SET UP ENVIRONMENT 

### **1. Set Up the Environment**

1. **Clone the Repository**:
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/StockMovementPrediction.git
   cd StockMovementPrediction
   ```

2. **Install Dependencies**:
   Install all required dependencies for the project by running:
   ```bash
   pip install -r requirements.txt
   ```

---

### **2. Set Up Twitter API Credentials**

You need to configure your **Bearer Token** to scrape Twitter data.

1. **Create a Twitter Developer Account**:
   - Go to [Twitter Developer Portal](https://developer.twitter.com/) and sign up for an API key.
   - Create an app and generate the **Bearer Token**.

2. **Configure the Bearer Token**:
   - Open the `scraper/aptweet_scraping.py` file.
   - Look for the line where the Bearer Token is configured and replace it with your own token, like this:
     ```python
     BEARER_TOKEN = 'YOUR_TWITTER_BEARER_TOKEN'
     ```
     Alternatively, you can set the Bearer Token using environment variables to keep it secure:
     ```python
     import os
     BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
     ```

---

### **3. Run the Data Scraping Script**

To scrape the data from Twitter, use the following command:

```bash
python scraper/aptweet_scraping.py
```

- The script will use the Bearer Token to authenticate with the Twitter API and fetch tweets related to stock market discussions.
- The scraped data will be saved in the `data/raw/` directory.

---

### **4. Preprocess the Data**

Once the data is scraped, it needs to be preprocessed for model training.

1. **Run the Preprocessing Script**:
   ```bash
   python model/preprocessing.py
   ```

   This will clean the data and extract the necessary features for the machine learning model.

---

### **5. Train the Model**

After preprocessing, you can train the machine learning model.

1. **Run the Training Script**:
   ```bash
   python model/training.py
   ```

   This script will train the model using the processed data.

---

### **6. Evaluate the Model**

After training the model, evaluate its performance.

1. **Run the Evaluation Script**:
   ```bash
   python model/evaluation.py
   ```

   This script will output metrics like accuracy, precision, recall, and other performance insights.

---

### **7. Verify the Results and Future Steps**

- **Visualize**: You can open Jupyter notebooks in the `notebooks/` folder to visualize data scraping, feature extraction, model training, and evaluation.
- **Future Improvements**: Consider integrating multiple data sources, improving the model with advanced NLP techniques, or creating a real-time dashboard for predictions.

---

### **Summary**

To summarize, the steps to run the project are:

1. **Clone** the repository.
2. **Install** dependencies with `pip install -r requirements.txt`.
3. **Configure** the Twitter API Bearer Token in `aptweet_scraping.py`.
4. **Run** the scraping script: `python scraper/aptweet_scraping.py`.
5. **Preprocess** data: `python model/preprocessing.py`.
6. **Train** the model: `python model/training.py`.
7. **Evaluate** the model: `python model/evaluation.py`.
