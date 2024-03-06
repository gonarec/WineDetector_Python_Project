import pandas as pd
import streamlit as st
import base64

st.markdown(
    "<h1 style='text-align: center; color: green;'>FIND THE BEST MODEL TO CLASSIFY YOUR DATABASE</h1>", 
    unsafe_allow_html=True)

# Linea di testo
st.write("")
st.write("")
st.markdown("<p style='text-align: left; color: yellow;'>INSERT YOUR DATABASE:</p>", unsafe_allow_html=True)
st.write("")

# Caricamento del file CSV e salvataggio del percorso in una variabile
file = st.file_uploader("Select a CSV file:")

# Elaborazione del file se è stato caricato
if file is not None:
    df = pd.read_csv(file)
    st.write("This is your Dataset:")
    new_df = df.copy()
    st.dataframe(new_df)
    st.write(new_df.shape)  

    if new_df.isnull().values.any():
        st.write("There are Nan values in your Dataset.")
        st.markdown("<p style='color: yellow;'>Do you want to remove the Nan values?</p>", unsafe_allow_html=True)
        option = st.radio("", ("Yes", "No"))
        
        if option == "Yes":
            st.write("You chose to remove Nan values.")
            st.write("Now choose between the options how do you want remove the Nan values. ")
            st.markdown("<p style='color: yellow;'>Select cleaning function:</p>", unsafe_allow_html=True)
            cleaning_option = st.selectbox("", ("Drop NaN", "Fill NaN", "Interpolate", "Custom Function"))
            if cleaning_option == "Drop NaN":
                new_df = new_df.dropna()
                st.write("NaN values have been dropped.")
            elif cleaning_option == "Fill NaN":
                # Your code to fill NaN values
                st.write("NaN values have been filled.")
            elif cleaning_option == "Interpolate":
                # Your code to interpolate NaN values
                st.write("NaN values have been interpolated.")
            elif cleaning_option == "Custom Function":
                # Your code for a custom cleaning function
                st.write("Custom cleaning function applied.")
            # Your code to remove Nan values goes here
            st.write("This is your new dataset.")
            st.dataframe(new_df) 
            st.write("Size of Dataset after cleaning:", new_df.shape)  

            # Adding download button for cleaned DataFrame
            csv = new_df.to_csv(index=False)
            # Download button
            st.download_button(label="Download the new CSV", data=csv, file_name="cleaned_data.csv", mime="text/csv")

        elif option == "No":
            st.write("You chose not to remove Nan values.")
    else:
         st.write("The dataset is clean there are not Nan values inside.")
    
    
