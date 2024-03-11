import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colormaps
import streamlit as st
import base64
from function_def import replace_outliers_with_median, replace_outliers_with_mean, remove_outliers,new_quality_value
from function_def import  classificator, plot_boxplots, plot_boxplots_comparision, plot_bar_chart_df, plot_result
from function_def import classificator_evo, classification_evo, plot_result_evo, plot_bar_chart_df_evo, trova_max, restore_function_corr

st.markdown(
    "<h1 style='text-align: center; color: blue;'>FIND THE BEST MODEL TO CLASSIFY YOUR DATABASE</h1>", 
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

    
    #feature_to_classify = st.text_input("Which feature do you want classify?")
    #new_df=new_df.drop(columns=feature_to_classify)

    corr_matrix = new_df.corr().abs()
    corr_index = np.where((np.triu(corr_matrix, k=1) > 0.20)) # correlated index features
    corr_features = pd.DataFrame({
        'Feature1': corr_matrix.columns[corr_index[0]], #Feature1
        'Feature2': corr_matrix.columns[corr_index[1]], #Feature2
        'Correlazione': corr_matrix.values[corr_index]
    })

    # Creiamo il plot del heatmap
    #plt.figure(figsize=(8, 6))
    #sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    #plt.title('Heatmap della matrice di correlazione')

    # Mostriamo il plot utilizzando Streamlit
    #st.pyplot(plt)
if file is not None:
    with st.expander("DATA CLEANING"):
        if new_df.isnull().values.any():
            st.markdown("<p style='color: yellow;'>There are Nan values in your Dataset.</p>", unsafe_allow_html=True)
            option = st.radio("Do you want to remove the Nan values?",  ("Yes", "No"))
            
            if option == "Yes":
                st.markdown("<p style='color: yellow;'>You chose to remove Nan values.</p>", unsafe_allow_html=True)
                st.write("Now choose between the options how do you want remove the Nan values. ")
                cleaning_option = st.selectbox("Select cleaning function:", (None,"Drop raw with NaN", "Fill NaN with the mean of the column", 
                                                    "Fill NaN with the median fo the column", "Fill NaN with the mean of correlated data",
                                                    "Fill NaN with the meadian of correlated data"))
                
                if cleaning_option == "Drop raw with NaN":
                    new_df = new_df.dropna()
                    st.write("NaN values have been dropped.")
                elif cleaning_option == "Fill NaN with the mean of the column":
                    new_df=new_df.fillna(new_df.mean())
                    st.write("NaN values have been filled.")
                elif cleaning_option == "Fill NaN with the median fo the column":
                    new_df=new_df.fillna(new_df.median())
                    st.write("NaN values have been filled.")
                elif cleaning_option == "Fill NaN with the mean of correlated data":
                    new_df=restore_function_corr(corr_features,0.10,new_df,'mean')
                    st.write("NaN values have been filled.")
                elif cleaning_option == "Fill NaN with the meadian of correlated data":
                    new_df=restore_function_corr(corr_features,0.10,new_df,'median')
                    st.write("NaN values have been filled.")                  
                    
                if cleaning_option is not None:
                    st.markdown("<p style='color: yellow;'>This is your new dataset.</p>", unsafe_allow_html=True)
                    st.dataframe(new_df) 
                    st.write("Size of Dataset after cleaning:", new_df.shape)  

                    # Adding download button for cleaned DataFrame
                    csv = new_df.to_csv(index=False)
                    # Download button
                    st.download_button(label="Download the new CSV", data=csv, file_name="cleaned_data.csv", mime="text/csv")

            elif option == "No":
                st.markdown("<p style='color: yellow;'>If you dont remove the perfomance of the classification can be compromised.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: yellow;'>The dataset is clean there are not Nan values inside.</p>", unsafe_allow_html=True)
        
        
