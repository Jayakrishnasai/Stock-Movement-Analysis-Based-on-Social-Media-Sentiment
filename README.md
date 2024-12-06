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

To run the project, follow these steps:

### **1. Clone the Repository**

First, clone the repository to your local machine (if you haven’t done so already):

```bash
git clone https://github.com/<your-username>/StockMovementPrediction.git
cd StockMovementPrediction
```

### **2. Set Up the Environment**

It’s recommended to use a virtual environment for managing dependencies:

#### **Create a Virtual Environment**
```bash
python -m venv venv
```

#### **Activate the Virtual Environment**
- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **On Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

#### **Install Dependencies**
Once the virtual environment is activated, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### **3. Run the Scraping Script**

Navigate to the `scraper/` directory and run the scraping script to collect data from the chosen social media platform (Twitter, Reddit, or Telegram). Replace `<scraping_script.py>` with the actual script name.

```bash
python scraper/<scraping_script.py>
```

This script will fetch the necessary data and save it in the `data/raw/` directory.

### **4. Preprocess and Extract Features**

Once the raw data is collected, go to the `model/` directory and run the preprocessing script to clean and extract relevant features from the raw data:

```bash
python model/<preprocessing_script.py>
```

This will process the raw data and store the cleaned data in the `data/processed/` directory.

### **5. Train and Evaluate the Model**

After preprocessing, you can train the model. Run the model training script from the `model/` directory:

```bash
python model/<training_script.py>
```

This will train the machine learning model and evaluate its performance. The results will be stored and displayed based on the evaluation metrics defined in the script.

### **6. Visualize and Demonstrate with Notebooks**

You can explore the entire process, from data scraping to model evaluation, in the Jupyter notebooks located in the `notebooks/` folder.

- Start Jupyter Notebook by running:
  ```bash
  jupyter notebook
  ```

- Open the notebooks to see demonstrations and visualizations of the data scraping, preprocessing, and model evaluation steps.

### **7. Run Evaluation Metrics**

After training, you can evaluate the model’s performance. Check for the metrics like accuracy, precision, and recall printed in the training script or use additional evaluation scripts if available.

---

### **Optional: Running the Entire Pipeline**
You can also create a script to run the entire pipeline from scraping to model evaluation:

```bash
python scraper/<scraping_script.py>
python model/<preprocessing_script.py>
python model/<training_script.py>
```

This will run everything in sequence.

---

### **Final Notes**
- Ensure that you have set up the necessary credentials (API keys for Twitter, Reddit, etc.) if required.
- If running into issues with dependencies, check that all libraries are correctly installed.
- Refer to the notebooks for further understanding of each step.
