# ---------------------------------------------
# ORIGINAL USER CODE (NO LINE REMOVED)
# ---------------------------------------------

# Core Libraries
import pandas as pd
import numpy as np

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error, r2_score

# Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

print("Welcome to the Restaurant Rating Predictor!")

# load data
df = pd.read_csv("dataset.csv")

# data exploration 
print("\nTop 5 Rows of Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values in Dataset:")
print(df.isnull().sum())

print("\nColumns in Dataset:")
print(df.columns)

# data preprocessing 
print("\nPreprocessing the Dataset...")

df.drop(['Restaurant ID','Restaurant Name','Address','Locality',
         'Locality Verbose','Rating color','Rating text','Currency'],
        axis=1,inplace=True)

df.dropna(subset=['Cuisines','Average Cost for two','Votes','Aggregate rating'], inplace=True)

df['Average Cost for two'] = df['Average Cost for two'].astype(str).str.replace(',', '')
df['Average Cost for two'] = df['Average Cost for two'].astype(float)

df['City'] = df['City'].astype('category').cat.codes
df['Cuisines'] = df['Cuisines'].astype('category').cat.codes

df['Has Table booking'] = df['Has Table booking'].map({'Yes':1,'No':0})
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes':1,'No':0})

# feature selection 
X = df[['City','Cuisines','Average Cost for two',
        'Has Table booking','Has Online delivery','Votes']]

y = df['Aggregate rating']

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

print("X_train shape:",X_train.shape)
print("X_test shape:",X_test.shape)

# model training
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train,y_train)

lr_model = LinearRegression()
lr_model.fit(X_train,y_train)

rf_model = RandomForestRegressor(n_estimators=100,random_state=42)
rf_model.fit(X_train,y_train)

# model evaluation
y_pred_rf = rf_model.predict(X_test)

mse_rf = mean_squared_error(y_test,y_pred_rf)
r2_rf = r2_score(y_test,y_pred_rf)

print("\nRandom Forest Performance")
print("MSE:",mse_rf)
print("R2 Score:",r2_rf)

# ---------------------------------------------
# NEW ADDITION (MODEL SAVE + PREDICTION)
# ---------------------------------------------

import pickle

# Save trained model (for Streamlit use)
pickle.dump(rf_model,open("model.pkl","wb"))

print("Model saved as model.pkl")


# Prediction function (Streamlit will call this)
def predict_rating(city,cuisines,cost,table,delivery,votes):

    input_data = np.array([[city,cuisines,cost,table,delivery,votes]])

    prediction = rf_model.predict(input_data)

    return prediction[0]