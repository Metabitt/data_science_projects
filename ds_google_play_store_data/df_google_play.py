import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("./df_google_play_updated.csv")
st.line_chart(df)