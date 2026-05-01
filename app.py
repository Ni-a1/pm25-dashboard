import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("pm25_results.csv")
time = pd.to_datetime(data["t_plot"])
actual = data["Y"]
predicted = data["Y_pred"]
st.title("PM2.5 Dashboard (From MATLAB Output)")
mse = ((actual - predicted) ** 2).mean()
st.metric("MSE", round(mse, 2))
view_option = st.selectbox(
    "Select View",
    ["Actual vs Predicted", "Only Actual", "Only Predicted"])
fig, ax = plt.subplots()

if view_option == "Actual vs Predicted":
    ax.plot(time, actual, label="Actual (MATLAB)")
    ax.plot(time, predicted, label="Predicted (MATLAB)")

elif view_option == "Only Actual":
    ax.plot(time, actual, label="Actual (MATLAB)")

else:
    ax.plot(time, predicted, label="Predicted (MATLAB)")
    
ax.set_title("PM2.5 Comparison")
ax.set_xlabel("Time")
ax.set_ylabel("PM2.5")
ax.legend()
ax.grid(True)
st.pyplot(fig, clear_figure=True)
if st.checkbox("Show Raw Data"):
    st.write(data)
