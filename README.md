# 💻 Laptop Price Prediction

This project predicts the **price of laptops** based on their specifications such as brand, processor, RAM, storage, GPU, and display features. The goal is to help users estimate the fair market price of a laptop using **Machine Learning models**.

---

## 📂 Repository Contents

* **Laptop\_price\_predication.ipynb** → Jupyter Notebook for data preprocessing, EDA, feature engineering, and model training.
* **app.py** → Flask/Streamlit web application for predicting laptop prices.
* **laptop\_data.csv** → Dataset containing laptop specifications and prices.
* **forest\_model.pkl** → Saved Random Forest model for prediction.
* **df2.pkl** → Preprocessed data file for quick loading.
* **requirements.txt** → Python dependencies for running the project.
* **.gitignore** → Ignored files and folders like `venv/`, `.vscode/`, and config files.

---

## ⚙️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Model:** Random Forest Regressor
* **Deployment:** Flask / Streamlit (via `app.py`)

---

## 🚀 How to Run the Project

1. Clone this repository

   ```bash
   git clone https://github.com/your-username/Laptop_price_predication.git
   cd Laptop_price_predication
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook for training (optional)

   ```bash
   jupyter notebook Laptop_price_predication.ipynb
   ```
4. Start the web app

   ```bash
   python app.py
   ```
5. Open the app in your browser to predict laptop prices.

---

## 📊 Results

* Achieved an **R² Score \~0.84**, indicating good accuracy.
* **Important Features:** Processor, RAM, Brand, GPU.
* Interactive price prediction via web app.

---

## 🔮 Future Enhancements

* Try advanced ML models (XGBoost, Gradient Boosting).
* Expand dataset with more brands and latest specs.
* Deploy app on **Heroku / Streamlit Cloud / AWS**.

---

## 👨‍💻 Author

**Arun Gautam**

* Data Analyst | Machine Learning Enthusiast
* [LinkedIn](https://www.linkedin.com/in/arun-gautam-20921822b) | [GitHub](https://github.com/subashgautam088)

---
