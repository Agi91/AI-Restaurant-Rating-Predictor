🍽 AI Restaurant Rating Predictor
Project Overview

AI Restaurant Rating Predictor is a Machine Learning project designed to predict the aggregate rating of a restaurant based on various factors such as location, cuisine type, cost for two people, customer votes, and service features like online delivery and table booking.

The goal of this project is to demonstrate how machine learning can analyze restaurant data and estimate customer ratings before users even visit the restaurant.

The project includes a complete machine learning workflow:

Data preprocessing

Feature engineering

Model training

Model evaluation

Interactive web application

A Streamlit-based web dashboard was built to allow users to input restaurant information and instantly receive a predicted rating along with visual insights.

This project demonstrates practical skills in data analysis, machine learning modeling, and building interactive ML applications, making it a strong portfolio project for showcasing data science and machine learning capabilities.

Key Questions Explored

Which factors influence restaurant ratings the most?

Does cost for two affect restaurant ratings?

Do online delivery and table booking impact customer satisfaction?

How do customer votes influence ratings?

How do restaurant ratings vary across different cities?

Technologies & Tools Used
Tool	Purpose
Python	Core programming language
Pandas	Data processing and analysis
NumPy	Numerical computations
Scikit-learn	Machine learning algorithms
Streamlit	Interactive web dashboard
Plotly	Data visualizations
Git & GitHub	Version control and project hosting
Dataset

File in Repository:
dataset.csv

The dataset contains information about restaurants including their services, pricing, location, and customer engagement metrics.

Key Columns

Restaurant Name

City

Cuisines

Average Cost for Two

Has Table Booking

Has Online Delivery

Votes

Aggregate Rating

These features are used to train a machine learning model that predicts the expected rating of a restaurant.

Project Structure
AI-Restaurant-Rating-Predictor
│
├── dataset.csv
│
├── model.py
│
├── model.pkl
│
├── app.py
│
├── style.css
│
├── requirements.txt
│
└── README.md
Folder Details

dataset.csv
Restaurant dataset used for training the machine learning model.

model.py
Script used for data preprocessing and model training.

model.pkl
Saved trained machine learning model used for predictions.

app.py
Streamlit web application for user interaction and predictions.

style.css
Custom styling used to improve the UI of the dashboard.

requirements.txt
Python dependencies required to run the project.

Machine Learning Model

The project experiments with multiple regression models to predict restaurant ratings.

Models Tested

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Among these models, Random Forest Regressor performed better in capturing relationships between features and predicting restaurant ratings more accurately.

The trained model was then saved as a .pkl file and integrated into the Streamlit application for real-time predictions.

Features of the Web App

The Streamlit dashboard allows users to:

Select City

Enter Average Cost for Two

Input Customer Votes

Choose Online Delivery Availability

Choose Table Booking Availability

The model then predicts the expected restaurant rating instantly.

Additional Visual Features

⭐ Star rating display

🍔 Restaurant style result card

📊 Feature importance graph

📈 Interactive charts using Plotly

Running the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/Agi91/AI-Restaurant-Rating-Predictor.git
2️⃣ Navigate to the Project Folder
cd AI-Restaurant-Rating-Predictor
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Streamlit Application
streamlit run app.py
5️⃣ Open in Browser
http://localhost:8501

You will see the Restaurant Rating Prediction Dashboard.

Future Improvements

Add deep learning models

Improve UI with advanced dashboards

Integrate real restaurant APIs

Deploy on cloud platforms

Author

AI Restaurant Rating Predictor
Machine Learning Project

GitHub Repository
https://github.com/Agi91/AI-Restaurant-Rating-Predictor