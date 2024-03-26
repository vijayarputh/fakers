import streamlit as st
import pandas as pd

def load_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    return df

def explore_data(df):
    st.header("Exploring the Dataset")
    
    # Display the first few rows of the dataset
    st.subheader("First Few Rows")
    st.write(df.head())

    # Get information about the columns and data types
    st.subheader("Data Information")
    st.write(df.info())

    # Summary statistics of numerical columns
    st.subheader("Summary Statistics")
    st.write(df.describe())

def filter_and_modify_data(df):
    st.header("Filtering and Modifying Data")
    
    # Filtering Data
    st.subheader("Filtering Data")
    party_to_filter = st.selectbox("Select a Party to Filter:", df['Party'].unique())
    filtered_data = df[df['Party'] == party_to_filter]
    st.write(filtered_data)

    # Modifying Data
    st.subheader("Modifying Data")
    column_to_update = st.selectbox("Select a Column to Update:", df.columns)
    update_value = st.number_input(f"Enter the New Value for {column_to_update}:")
    df[column_to_update] = update_value
    st.write("Data Updated Successfully!")
    st.write(df.head())

def main():
    st.title("Election Bonds and Scam Analysis")

    # Load the dataset
    file_path = "election_bonds_dataset.csv"
    df = load_data(file_path)

    # Explore the dataset
    explore_data(df)

    # Filter and Modify Data
    filter_and_modify_data(df)

if __name__ == "__main__":
    main()
