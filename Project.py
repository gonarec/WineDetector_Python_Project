import pandas as pd
import streamlit as st

st.header('Title')
wine_dataframe = pd.read_csv('restore_winedata.csv')
wine_dataframe.info()

