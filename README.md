<<<<<<< HEAD

````markdown

# 🍽 AI Restaurant Rating Predictor

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)

---

# 📌 Project Overview

**AI Restaurant Rating Predictor** is a Machine Learning project designed to predict the **aggregate rating of a restaurant** using various restaurant features such as location, cuisine type, cost for two people, customer votes, and service options.

The project demonstrates a complete **end-to-end machine learning workflow**, including:

- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Interactive dashboard deployment

An interactive **Streamlit dashboard** allows users to enter restaurant details and instantly receive predicted ratings along with visual insights.

This project showcases practical skills in **machine learning, data preprocessing, model evaluation, and building interactive data applications**.

---

# ❓ Key Questions Explored

- Which factors influence restaurant ratings the most?
- Does **average cost for two** affect ratings?
- Do **online delivery and table booking** impact customer satisfaction?
- How do **customer votes** influence restaurant ratings?
- How do ratings vary across different **cities**?

---

# 🛠 Technologies & Tools Used

| Tool | Purpose |
|-----|------|
| Python | Core programming language |
| Pandas | Data analysis and preprocessing |
| NumPy | Numerical computations |
| Scikit-learn | Machine learning models |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| Git & GitHub | Version control |

---

# 📊 Dataset

**File in Repository**

```
dataset.csv
```

The dataset contains information about restaurants including pricing, services, and customer engagement metrics.

### Important Features

- City
- Cuisines
- Average Cost for Two
- Has Table Booking
- Has Online Delivery
- Votes
- Aggregate Rating

These features are used to train a machine learning model that predicts restaurant ratings.

---

# 📂 Project Structure

```
AI-Restaurant-Rating-Predictor
│
├── dataset.csv
├── model.py
├── model.pkl
├── app.py
├── style.css
├── requirements.txt
└── README.md
```

### Folder Details

**dataset.csv**  
Restaurant dataset used for training the machine learning model.

**model.py**  
Script used for data preprocessing and model training.

**model.pkl**  
Saved trained machine learning model used for predictions.

**app.py**  
Streamlit web application for user interaction and predictions.

**style.css**  
Custom styling used to improve the UI of the dashboard.

**requirements.txt**  
Python dependencies required to run the project.

---

# 🤖 Machine Learning Model

The project evaluates multiple regression models to predict restaurant ratings.

### Models Tested

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Among these models, **Random Forest Regressor** performed best in predicting restaurant ratings by capturing complex relationships between the features.

The trained model was saved as:

```
model.pkl
```

and integrated into the Streamlit application for real-time predictions.

---

# 🌐 Features of the Web Application

The Streamlit dashboard allows users to:

- Select **City**
- Enter **Average Cost for Two**
- Enter **Customer Votes**
- Select **Online Delivery Availability**
- Select **Table Booking Availability**

### Dashboard Features

- ⭐ Star Rating Display
- 🍔 Restaurant Result Card
- 📊 Feature Importance Graph
- 📈 Interactive Charts

---

# ▶ Running the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Agi91/AI-Restaurant-Rating-Predictor.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd AI-Restaurant-Rating-Predictor
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

### 5️⃣ Open in Browser

```
http://localhost:8501
```

You will see the **Restaurant Rating Prediction Dashboard**.

---

# 🚀 Future Improvements

- Improve dashboard UI
- Add deep learning models
- Integrate real-time restaurant APIs
- Deploy on cloud platforms

---

# 👨‍💻 Author

**AI Restaurant Rating Predictor**  
Machine Learning Project

GitHub Repository  
https://github.com/Agi91/AI-Restaurant-Rating-Predictor

---

⭐ Built with **Python, Machine Learning, and Streamlit**