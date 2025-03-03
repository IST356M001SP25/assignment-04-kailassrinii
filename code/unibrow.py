"""
UniBrow - Universal Dataset Browser
A Streamlit application for browsing datasets in various formats.
"""

import streamlit as st
import pandas as pd
import os
from pandaslib import (
    get_column_names,
    get_columns_of_type,
    get_unique_values,
    get_file_extension,
    load_file
)

def main():
    st.title("UniBrow")
    st.subheader("Universal Dataset Browser")
    
    uploaded_file = st.file_uploader(
        "Upload a file", 
        type=["xlsx", "csv", "json"]
    )
    
    if uploaded_file is not None:
        file_extension = get_file_extension(uploaded_file.name)
        
        try:
            if file_extension == 'csv':
                df = pd.read_csv(uploaded_file)
            elif file_extension in ['xlsx', 'xls']:
                df = pd.read_excel(uploaded_file)
            elif file_extension == 'json':
                df = pd.read_json(uploaded_file)
            else:
                st.error(f"Unsupported file type: {file_extension}")
                return
            
            all_columns = get_column_names(df)
            
            st.subheader("Select Columns")
            selected_columns = st.multiselect(
                "Choose columns to display",
                options=all_columns,
                default=all_columns
            )
            
            st.subheader("Filter Data")
            use_filter = st.checkbox("Apply filter")
            
            filtered_df = df.copy()
            
            if use_filter:
                text_columns = get_columns_of_type(df, 'object')
                
                if text_columns:
                    filter_column = st.selectbox(
                        "Select column to filter on",
                        options=text_columns
                    )
                    
                    unique_values = get_unique_values(df, filter_column)
                    
                    filter_value = st.selectbox(
                        f"Select value from {filter_column}",
                        options=unique_values
                    )
                    
                    filtered_df = df[df[filter_column] == filter_value]
                else:
                    st.warning("No text columns available for filtering")
            
            if selected_columns:
                result_df = filtered_df[selected_columns]
                
                st.subheader("Data")
                st.dataframe(result_df)
                
                st.subheader("Summary Statistics")
                st.dataframe(result_df.describe())
            else:
                st.warning("Please select at least one column to display")
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()