import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')
st.header("US Vehicle Data Analysis")
# Botón 1: Histograma del odómetro

p = st.button("Odometer Histogram")
if p:
    st.subheader("Histogram of Vehicle Odometer Values")
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'], nbinsx=50)])
    fig.update_layout(title="Distribution of Vehicle Odometer Values in the US",xaxis_title="Odometer",yaxis_title="Count")
    st.plotly_chart(fig, use_container_width=True)
    st.write("This histogram shows the distribution of the odometer variable.")
# Botón 2: Scatter odómetro vs precio

q = st.button("Odometer vs Price Scatter Plot")

if q:
    st.subheader("Scatter Plot of Odometer vs Price")
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],y=car_data['price'],mode='markers')])
    fig.update_layout(title="Odometer vs Price",xaxis_title="Odometer",yaxis_title="Price")
    st.plotly_chart(fig, use_container_width=True)
    st.write("This scatter plot shows the relationship between odometer and price.")