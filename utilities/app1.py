import streamlit as st
import pandas as pd
import sqlite3

# Function to create the SQLite database and table
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert a user into the database
def create_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# Function to read all users from the database
def read_users():
    conn = sqlite3.connect('users.db')
    users_data = pd.read_sql_query('SELECT * FROM users', conn)
    conn.close()
    return users_data

# Function to update user information in the database
def update_user(username, new_password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
    conn.commit()
    conn.close()

# Function to delete a user from the database
def delete_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

# Create the SQLite database and table
create_database()

# Page configuration
st.set_page_config(page_title="CRUD Operations", page_icon="🔄")

# Sidebar
st.sidebar.title("CRUD Operations")

# Display main content
st.title("CRUD Operations with Streamlit")
st.write("Perform Create, Read, Update, and Delete operations using the sidebar buttons.")

# CRUD form
crud_operation = st.sidebar.selectbox("Select Operation", ["Create", "Read", "Update", "Delete"])

if crud_operation == "Create":
    st.sidebar.header("Create User")
    new_username = st.sidebar.text_input("New Username")
    new_password = st.sidebar.text_input("New Password", type="password")
    if st.sidebar.button("Create User"):
        create_user(new_username, new_password)
        st.sidebar.success(f"User '{new_username}' created successfully.")

elif crud_operation == "Read":
    st.sidebar.header("Read Users")
    users_data = read_users()
    st.dataframe(users_data)

elif crud_operation == "Update":
    st.sidebar.header("Update User")
    update_username = st.sidebar.text_input("Username to Update")
    new_password = st.sidebar.text_input("New Password", type="password")
    if st.sidebar.button("Update Password"):
        update_user(update_username, new_password)
        st.sidebar.success(f"Password updated for user '{update_username}'.")

elif crud_operation == "Delete":
    st.sidebar.header("Delete User")
    delete_username = st.sidebar.text_input("Username to Delete")
    if st.sidebar.button("Delete User"):
        delete_user(delete_username)
        st.sidebar.success(f"User '{delete_username}' deleted successfully.")