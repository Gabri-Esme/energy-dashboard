import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3

# --- Load data from SQLite ---
db_path = "energy.db"

# Connect and load weather data
conn = sqlite3.connect(db_path)
df_weather = pd.read_sql("SELECT date, temp FROM elexon_weather", conn, parse_dates=['date'])

# Load generation data
df_generation = pd.read_sql("SELECT date, total_generation_gw FROM elexon_generation", conn, parse_dates=['date'])
conn.close()

# --- Merge datasets on date ---
df_merged = pd.merge(df_weather, df_generation, on='date', how='inner')

# --- Create the plot with secondary y-axis ---
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Temperature line (left y-axis)
fig.add_trace(
    go.Scatter(
        x=df_merged['date'], 
        y=df_merged['temp'], 
        name='Temperature (°C)',
        line=dict(color='orange')
    ),
    secondary_y=False,
)

# Total generation line (right y-axis)
fig.add_trace(
    go.Scatter(
        x=df_merged['date'], 
        y=df_merged['total_generation_gw'], 
        name='Total Generation (GW)',
        line=dict(color='green')
    ),
    secondary_y=True,
)

# --- Configure axes ---
fig.update_yaxes(title_text="Temperature (°C)", secondary_y=False, range=[0, df_merged['temp'].max()*1.1])
fig.update_yaxes(title_text="Total Generation (GW)", secondary_y=True, range=[0, df_merged['total_generation_gw'].max()*1.1])
fig.update_xaxes(title_text="Date")

# --- Layout settings ---
fig.update_layout(
    title_text="Energy Generation & Temperature Over Time",
    width=1200,
    height=600,
    margin=dict(l=50, r=50, t=50, b=50)
)

# --- Display in Streamlit ---
st.title("Energy Dashboard")
st.plotly_chart(fig, use_container_width=True)