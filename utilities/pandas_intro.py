import streamlit as st
import pandas as pd

def main():
    st.title("Introduction to Pandas")

    st.header("What is Pandas?")
    st.write("Pandas is a Python library used for data manipulation and analysis. It provides easy-to-use data structures and functions, making it powerful for working with structured data.")

    st.header("Basic Elements of Pandas")
    
    st.subheader("1. DataFrame")
    st.write("DataFrame is a two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or SQL table.")
    st.code("import pandas as pd\n\n# Create DataFrame\ndata = {'Name': ['John', 'Emma', 'Peter'], 'Age': [25, 30, 35]}\ndf = pd.DataFrame(data)")

    st.subheader("2. Series")
    st.write("Series is a one-dimensional labeled array capable of holding any data type.")
    st.code("import pandas as pd\n\n# Create Series\ns = pd.Series([10, 20, 30, 40, 50])")

    st.subheader("3. Index")
    st.write("Index is a unique identifier for rows in a DataFrame or labels for elements in a Series.")
    st.code("import pandas as pd\n\n# Create DataFrame with custom index\ndata = {'Name': ['John', 'Emma', 'Peter'], 'Age': [25, 30, 35]}\ndf = pd.DataFrame(data, index=['A', 'B', 'C'])")

    st.header("Object Data Indexing")
    st.write("Pandas provides various methods for indexing and selecting data in a DataFrame or Series.")

    st.subheader("DataFrame.loc[]")
    st.write("Access a group of rows and columns by labels.")
    st.code("df.loc['A']  # Select row with index 'A'")

    st.subheader("DataFrame.iloc[]")
    st.write("Access a group of rows and columns by integer position.")
    st.code("df.iloc[0]  # Select row at position 0")

    st.header("Selection Operating")
    st.write("Pandas offers powerful operations for selecting, filtering, and modifying data.")

    st.subheader("Filtering Data")
    st.write("Filter rows based on certain conditions.")
    st.code("df[df['Age'] > 30]  # Filter rows where Age is greater than 30")

    st.subheader("Modifying Data")
    st.write("Update values in a DataFrame.")
    st.code("df.loc['A', 'Age'] = 26  # Change the Age value for row 'A' to 26")

if __name__ == "__main__":
    main()
