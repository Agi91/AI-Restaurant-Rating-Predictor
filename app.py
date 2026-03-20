import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(page_title="AI Restaurant Rating Dashboard",layout="wide")

# -----------------------------
# Custom UI (Black Gradient)
# -----------------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# -----------------------------
# Load Model
# -----------------------------

model = pickle.load(open("model.pkl","rb"))

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("dataset.csv")

# -----------------------------
# Title
# -----------------------------

st.title("🍽 AI Restaurant Rating Dashboard")

# -----------------------------
# Encoding Maps
# -----------------------------

city_cat = df['City'].astype('category')
city_map = dict(enumerate(city_cat.cat.categories))
city_map_rev = {v:k for k,v in city_map.items()}

cuisine_cat = df['Cuisines'].astype('category')
cuisine_map = dict(enumerate(cuisine_cat.cat.categories))
cuisine_map_rev = {v:k for k,v in cuisine_map.items()}

# -----------------------------
# Sidebar Inputs
# -----------------------------

st.sidebar.header("Restaurant Input")

city_name = st.sidebar.selectbox("Select City",list(city_map_rev.keys()))
cuisine_name = st.sidebar.selectbox("Select Cuisine",list(cuisine_map_rev.keys()))

city = city_map_rev[city_name]
cuisine = cuisine_map_rev[cuisine_name]

cost = st.sidebar.number_input("Average Cost for Two (₹)",0,10000)

table = st.sidebar.selectbox("Table Booking",[0,1])
delivery = st.sidebar.selectbox("Online Delivery",[0,1])

votes = st.sidebar.number_input("Votes",0,5000)

# -----------------------------
# Dataset Metrics
# -----------------------------

st.subheader("Restaurant Dataset Overview")

col1,col2,col3 = st.columns(3)

col1.metric("Total Restaurants",len(df))
col2.metric("Average Rating",round(df["Aggregate rating"].mean(),2))
col3.metric("Total Votes",df["Votes"].sum())

# -----------------------------
# Prediction
# -----------------------------

if st.sidebar.button("Predict Rating"):

    input_data = np.array([[city,cuisine,cost,table,delivery,votes]])

    rating = model.predict(input_data)[0]

    st.subheader("⭐ Predicted Rating")

    stars = "⭐"*int(round(rating))

    st.markdown(f"## {stars} ({rating:.2f})")

    # Restaurant Card

    st.markdown(f"""
    <div class="restaurant-card">

    <h3>🍔 Restaurant Prediction</h3>

    <b>📍 City:</b> {city_name} <br>
    <b>🍽 Cuisine:</b> {cuisine_name} <br>
    <b>💰 Cost for Two:</b> ₹{cost} <br>
    <b>👍 Votes:</b> {votes} <br><br>

    <h2 style="color:#facc15;">⭐ Rating: {rating:.2f}</h2>

    </div>
    """,unsafe_allow_html=True)

# -----------------------------
# 3D Visualization
# -----------------------------

st.subheader("📈 3D Restaurant Data Visualization")

fig3d = px.scatter_3d(
df,
x="Votes",
y="Average Cost for two",
z="Aggregate rating",
color="Aggregate rating"
)

st.plotly_chart(fig3d,use_container_width=True)

# -----------------------------
# Feature Importance
# -----------------------------

st.subheader("📊 Feature Importance")

importances = model.feature_importances_

features = [
'City',
'Cuisines',
'Average Cost',
'Table Booking',
'Online Delivery',
'Votes'
]

fig = px.bar(
x=features,
y=importances,
color=importances
)

st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# City Heatmap
# -----------------------------
st.subheader("🌍 Top Cities by Average Rating")

city_rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False).head(10)

fig2 = px.bar(
x=city_rating.index,
y=city_rating.values,
labels={"x":"City","y":"Average Rating"},
color=city_rating.values,
title="Top 10 Cities by Restaurant Rating"
)

st.plotly_chart(fig2,use_container_width=True)


# 
st.subheader("🍽 Most Popular Cuisines")

cuisine_votes = df.groupby("Cuisines")["Votes"].sum().sort_values(ascending=False).head(10)

fig3 = px.bar(
x=cuisine_votes.index,
y=cuisine_votes.values,
color=cuisine_votes.values,
labels={"x":"Cuisine","y":"Total Votes"}
)

st.plotly_chart(fig3,use_container_width=True)

#
st.subheader("💰 Cost vs Rating")

fig4 = px.scatter(
df,
x="Average Cost for two",
y="Aggregate rating",
color="Aggregate rating",
title="Restaurant Cost vs Rating"
)

st.plotly_chart(fig4,use_container_width=True)