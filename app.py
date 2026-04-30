import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("pm25_results.csv")
time = data["t_plot"]
actual = data["Y"]
predicted = data["Y_pred"]
st.title("PM2.5 Dashboard (From MATLAB Output)")
mse = ((actual - predicted) ** 2).mean()
st.metric("MSE", round(mse, 2))
fig, ax = plt.subplots()
ax.plot(time, actual, label="Actual (MATLAB)")
ax.plot(time, predicted, label="Predicted (MATLAB)")
ax.set_title("PM2.5 Comparison")
ax.set_xlabel("Time")
ax.set_ylabel("PM2.5")
ax.legend()
ax.grid(True)
st.pyplot(fig)

