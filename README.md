# 📰 News Credibility Monitor

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.42.0-FF4B4B?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.6.1-F7931E?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-2.2.3-150458?logo=pandas)
![NLTK](https://img.shields.io/badge/NLTK-3.9.1-329539)

An intelligent NLP-powered web application that evaluates the credibility of news articles. By utilizing classical machine learning techniques (TF-IDF Vectorization and Logistic Regression), this system analyzes linguistic patterns to classify news articles as **Real** or **Fake**.

This project represents **Milestone 1** of a larger initiative to build an agentic AI misinformation monitoring assistant.

---

## 🌟 Key Features

- **Text Pattern Analysis:** Analyzes the vocabulary, structure, and sentiment markers of news text.
- **High Accuracy Model:** Logistic Regression model achieving ~98.1% accuracy on the sanitized ISOT fake news dataset.
- **Bias Mitigation:** Custom regex-based text cleaning to strip publisher prefixes (e.g., "Reuters") preventing the model from "cheating" and forcing it to learn actual linguistic differences.
- **Interactive UI:** A highly responsive and user-friendly Streamlit web interface for real-time predictions.
- **Confidence Scoring:** Outputs the exact probability mathematical confidence of its prediction.

---

## 🏗️ System Architecture & Design

The system is designed with a strict modular architecture separating data processing, feature engineering, model training, and the presentation layer.

```mermaid
graph TD
    subgraph Data Pipeline
        A[Raw Datasets <br> True.csv & Fake.csv] --> B(Data Loader)
        B --> C{Text Cleaner}
        C -- Regex Bias Mitigation & <br> Stopword Removal --> D[Processed Text]
    end

    subgraph Feature Engineering & Training
        D --> E[TF-IDF Vectorizer]
        E -- 5000 Max Features <br> Bi-grams --> F[Document-Term Matrix]
        F --> G(Logistic Regression Model)
        G -- Evaluated on Test Set --> H[(Serialized Models <br> .pkl)]
    end

    subgraph Presentation Layer <br> app.py
        I[User Input Text] --> J{Text Cleaner}
        J --> K[Loaded TF-IDF Vectorizer]
        K --> L[Loaded Prediction Model]
        L --> M((Credibility Score <br> & UI Render))
    end
    
    H -. Loads into .-> K
    H -. Loads into .-> L
```

### Module Breakdown (src/)
*   `config.py`: Centralized configuration and file path management.
*   `data/`: Scripts for loading, merging, and shuffling raw data.
*   `features/`: Vocabulary building and TF-IDF matrix generation.
*   `models/`: Logistic Regression training algorithm and evaluation metrics.
*   `utils/`: Core utilities like the `text_cleaner.py` (responsible for tokenization, regex bias stripping, and lowercasing).
*   `pipeline/`: The orchestrator script (`training_pipeline.py`) that executes the end-to-end flow.

---

## 🚀 Getting Started

### Prerequisites

You need Python 3.12+ installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SatyamKumarCS/news-credibility-monitor.git
   cd news-credibility-monitor
   ```

2. Create and activate a Virtual Environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the NLTK Stopwords package (if you haven't already):
   ```python
   import nltk
   nltk.download('stopwords')
   ```

### Running the Application

To launch the Streamlit frontend locally:

```bash
streamlit run app.py
```
The app will automatically open in your browser at `http://localhost:8501`.

### Retraining the Model

If you add new data to `data/raw/` or modify the cleaning heuristics, you can retrain the model with a single command:

```bash
python3 -m src.pipeline.training_pipeline
```
This will automatically overwrite the `.pkl` files in the `models/` directory, and the Streamlit app will immediately use the new intelligence on the next prediction.

---

## ⚠️ Limitations & Best Practices

- **Topic Specificity:** The current model was trained heavily on **US Political** and **World News** datasets from 2016-2018. It is highly accurate within these domains but may struggle with sports, entertainment, or highly technical financial news (where vocabulary drastically diverges).
- **Length Constraint:** The NLP model requires sufficient context to detect linguistic patterns. Inputs should ideally be a full paragraph (50+ words) rather than a single sentence summary.

---

## 📜 Next Steps (Milestone 2)

Future iterations of this project will transition from classical ML to an Agentic AI architecture (using LangGraph and RAG) to verify claims against live, trusted databases rather than relying solely on static linguistic patterns.
