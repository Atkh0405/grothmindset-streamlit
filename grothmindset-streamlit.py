gimport streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title== "Data Sweeper",layout="wide")

# Custom Css
st.markdown(
    """
<style>
.stApp{
    background-color: black;
    color: white;
    }
    </style>
    """,
    unsafe_allow_html=True

)
# Title and Discrition
st.title("Data Sweeper Strealing Integrator By Atif Ullah Khan")
st.write("Transform your files between CSV and Excelformats with built-in data cleaning and visualiazation Creating the project for quarter 3! ")

# File Uploader
# File Uploader
uploaded_files = st.file_uploader("Upload your files (accepts CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"unsupported file type: {file_ext}")
            continue
    
        #file details
        st.write(" Preview the head of the Dataframe")
        st.write(df.head()) 

        

        #data cleaning options
        st.write("Data Cleaning Options")
        if st.checkbox("Clean data for {file.name}"):
            coll,col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicate from the file: {file.name}"):
                    df = df.drop_duplicates(inplace=True)
                    st.write("Duplicate removed!")

            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(includes=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled!")

        st.subheader("Select Columns to keep")
        selected_columns = st.multiselect(f"Choose columns"for  {file.name}", df.columns, default=df.columns)
        if selected_columns:
            df = df[columns]
            

            #data visulization
            st.subheader("Data Visualization")
            if st.checkbox(f"Show visulization for {file.name}"):
                st.bar_chart(select_dtypes(include=["number"]).iloc[:, :2])


        #Conversion options
        st.subheader("Conversion Options")
        conversion_type = st.radio("Convert {file.name} to:", ["CVS" , "Excel"], key=file.name)
        if st.button(f"convert{file.name}:
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.csv(buffer, index=False)
                file_name = file.name.replace(file_ext,"csv")
                mime_type = "text/csv
            elif conversion_type == "Excel":
                df.to.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext,"xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)
            
            
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

            st.sucess( Alll files processed successfully)

        

                    
            

            



            






