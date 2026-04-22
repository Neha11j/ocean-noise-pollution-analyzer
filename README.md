# 🌊 Ocean Noise Pollution Analyzer

## 📌 Overview

The **Ocean Noise Pollution Analyzer** is a Machine Learning-based project designed to analyze and classify underwater acoustic signals. The system identifies different types of ocean noise (such as anthropogenic and natural sounds) using structured sonar/acoustic data and evaluates model performance through multiple metrics.

---

## 🎯 Objectives

* Analyze underwater acoustic data
* Classify noise sources using Machine Learning models
* Evaluate performance using standard metrics
* Compare models using a **Leaderboard system**
* Visualize results through graphs and plots

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn
* **Environment:** Jupyter Notebook
* **Version Control:** Git & GitHub

---

## 📊 Dataset

* Sonar Acoustic Dataset (CSV format)
* Contains numerical features representing acoustic signals
* Used for classification of different sound types

---

## ⚙️ Methodology (Pipeline)

1. **Data Loading**
2. **Data Preprocessing**

   * Handling missing values
   * Feature scaling
   * Label encoding
3. **Model Training**

   * Random Forest
   * Support Vector Machine (SVM)
   * Logistic Regression
4. **Evaluation Metrics**

   * Accuracy
   * Precision
   * Recall
   * F1 Score
5. **Visualization**

   * Confusion Matrix
   * ROC Curve
   * Model Comparison Graphs
6. **Leaderboard System**

   * Stores and ranks model performance

---

## 📈 Results

* Multiple models were trained and evaluated
* Best model selected based on **Accuracy and F1 Score**
* Performance visualized using graphs and ROC curve
* Results stored in a leaderboard for comparison

---

## 🏆 Leaderboard

| Rank | Model               | Accuracy | F1 Score |
| ---- | ------------------- | -------- | -------- |
| 1    | Random Forest       | High     | High     |
| 2    | SVM                 | Medium   | Medium   |
| 3    | Logistic Regression | Moderate | Moderate |

*(Actual values generated during execution)*

---

## 📁 Project Structure

```
ocean-noise-pollution-analyzer/
│
├── notebooks/
│   └── Ocean_Noise_Analyzer.ipynb
│
├── leaderboard/
│   └── leaderboard.csv
│
├── images/
│   └── (graphs and visualizations)
│
├── docs/
│   └── report.pdf
│
├── README.md
├── requirements.txt
```

---

## 🚀 How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/ocean-noise-pollution-analyzer.git
```

2. Install dependencies:

```

pip install -r requirements.txt
```

3. Run Jupyter Notebook:

```
Github_project.ipnb
```

4. Open and execute:

```
Ocean_Noise_Analyzer.ipynb
```
5.run pipelie.py

```
python pipeline.py
```
---

   
## 📊 Visualizations

* Model Accuracy Comparison
* Confusion Matrix
* ROC Curve

(All graphs are available in the `images/` folder)

---

## 💡 Future Scope

* Real-time ocean noise monitoring
* Deep learning models (CNN)
* Integration with IoT sensors
* Geographic noise mapping

---

## 👩‍💻 Author

**Neha Jadhav**
TY B.Sc. Data Science & Big Data Analytics

---

## 📜 License

This project is for academic and educational purposes.
