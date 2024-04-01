import streamlit as st
import sqlite3
import pandas as pd

# Create and populate the HR database
def create_hr_database():
    conn = sqlite3.connect('hr_database.db')
    cursor = conn.cursor()

    # Create employees table
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        employee_id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        department_id INTEGER
                    )''')

    # Create departments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                        department_id INTEGER PRIMARY KEY,
                        department_name TEXT
                    )''')

    # Insert sample data into employees table
    employees_data = [
        (1, 'John', 'Doe', 1),
        (2, 'Jane', 'Smith', 2),
        (3, 'Mike', 'Johnson', 1),
        (4, 'Emily', 'Brown', 2),
        (5, 'David', 'Williams', 3)
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees_data)

    # Insert sample data into departments table
    departments_data = [
        (1, 'HR'),
        (2, 'Finance'),
        (3, 'IT')
    ]
    cursor.executemany("INSERT INTO departments VALUES (?, ?)", departments_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Perform SQL Inner Join and display results using Streamlit
def inner_join():
    conn = sqlite3.connect('hr_database.db')
    cursor = conn.cursor()

    # SQL query for Inner Join
    query = """
            SELECT employees.employee_id, employees.first_name, employees.last_name, departments.department_name
            FROM employees
            INNER JOIN departments ON employees.department_id = departments.department_id
            """

    # Execute the query
    cursor.execute(query)
    data = cursor.fetchall()

    # Display the results in a DataFrame using Streamlit
    df = pd.DataFrame(data, columns=['Employee ID', 'First Name', 'Last Name', 'Department'])
    st.write(df)

    # Close connection
    conn.close()

def main():
    st.title('HR Database - SQL Inner Join')
    create_hr_database()
    inner_join()

if __name__ == '__main__':
    main()
