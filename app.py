import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("pm25_results.csv")
time = pd.to_datetime(data["t_plot"])
actual = data["Y"]
predicted = data["Y_pred"]
st.title("PM2.5 Dashboard (From MATLAB Output)")

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
mse = ((actual - predicted) ** 2).mean()
st.metric("MSE", round(mse, 2))
rmse = mse ** 0.5
st.metric("RMSE", round(rmse, 2))

error = actual - predicted

fig2, ax2 = plt.subplots()
ax2.plot(time, error)
ax2.set_title("Prediction Error Over Time")
ax2.set_xlabel("Time")
ax2.set_ylabel("Error")
ax2.grid(True)

st.pyplot(fig2)
if st.checkbox("Show Raw Data"):
    st.write(data)
    
