import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Smart Energy Analysis for Automated Container Terminal")

st.write("""
This dashboard analyzes energy demand, solar generation, grid dependency,
and operational scenarios for an automated container terminal.
""")
import sqlite3

# Load data
conn = sqlite3.connect("energy.db")
df = pd.read_sql("SELECT * FROM energy_data", conn)

# Show data
st.subheader("Data Preview")
st.dataframe(df.head())

# Plot
st.subheader("Energy Profile Over the Day")

fig, ax = plt.subplots()

ax.plot(df["hour"], df["total_demand_kwh"], label="Total Demand")
ax.plot(df["hour"], df["solar_generation_kwh"], label="Solar Generation")
ax.plot(df["hour"], df["grid_usage_kwh"], label="Grid Usage")

ax.set_xlabel("Hour")
ax.set_ylabel("Energy (kWh)")
ax.set_title("Energy Profile")
ax.legend()
ax.grid()

st.pyplot(fig)
