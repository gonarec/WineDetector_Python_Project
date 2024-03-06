import pandas as pd
import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: green;'>FIND THE BEST MODEL TO CLASSIFY YOUR DATABASE</h1>", 
    unsafe_allow_html=True)

# Linea di testo
st.write("")
st.write("")
st.markdown("<p style='text-align: left;'>INSERT YOUR DATABASE:</p>", unsafe_allow_html=True)
st.write("")

# Caricamento del file CSV e salvataggio del percorso in una variabile
file = st.file_uploader("Select a CSV file:")

# Elaborazione del file se è stato caricato
if file is not None:
    df = pd.read_csv(file)
    st.write("This is your Dataset:")
    new_df = df.copy()
    st.dataframe(new_df)  

    if new_df.isnull().values.any():
        st.write("There are Nan values in the DataFrame.")
        st.write("Do you want to remove the Nan Values?")
    else:
        st.write("DataFrame is clean. No Nan Values.")