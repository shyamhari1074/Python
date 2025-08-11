
# ⚽ Football World Cup Winner Prediction

This repository contains a **machine learning project** that predicts the likely winner of the FIFA Football World Cup using historical match data, team stats, and engineered features.

The model is trained using historical datasets and outputs **probability rankings** for each team.

---

## 📌 Project Overview
The aim of this project is to:
- Ingest and clean historical football match and team ranking data.
- Engineer features such as **recent form**, **goal difference**, and **ranking differences**.
- Train ML models (e.g., Logistic Regression, Random Forest, XGBoost) to predict the winning team.
- Output ranked probabilities for each team in a tournament.

---

## 📂 Project Structure
```
.
├── data/
│   ├── raw/               # Original datasets (historical matches, rankings, etc.)
│   └── processed/         # Cleaned & feature-engineered data
├── notebooks/
│   └── Untitled.ipynb     # Main notebook for model training & prediction
├── models/                # Saved trained models
├── outputs/               # Prediction results
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🗂 Features Used
Typical features included:
- Team FIFA ranking difference
- Recent form (last N matches)
- Goals scored / conceded averages
- Head-to-head record
- Group stage strength
- Knockout path difficulty

---

## ⚙️ Installation
Clone this repository and set up the environment.

```bash
# Clone the repo
git clone https://github.com/<your-username>/worldcup-winner-prediction.git
cd worldcup-winner-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 How to Run
1. Place raw datasets in `data/raw/`.
2. Open the main notebook:

```bash
jupyter notebook notebooks/Untitled.ipynb
```

3. Run all cells to train the model and generate predictions.

4. Predictions will be saved in `outputs/` as CSV.

---

## 📊 Evaluation
The project evaluates models using:
- **Log Loss** — Probability prediction quality
- **Top-1 Accuracy** — Did the model pick the actual winner?
- **Top-K Accuracy** — Was the winner in the top K predictions?
- **Brier Score** — Probability calibration

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📧 Contact
**Author:** Shyam Hari  
**LinkedIn:** [https://www.linkedin.com/in/shyam-hari-5389492b3/](https://www.linkedin.com/in/shyam-hari-5389492b3/)  
**GitHub:** [https://github.com/shyamhari1074](https://github.com/shyamhari1074)
