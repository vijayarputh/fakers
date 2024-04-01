import streamlit as st
import sqlite3
import pandas as pd

# Function to create and populate the HR database
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

# Function to perform SQL Inner Join and display results
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

    # Display the results in a DataFrame
    df = pd.DataFrame(data, columns=['Employee ID', 'First Name', 'Last Name', 'Department'])

    # Close connection
    conn.close()

    return df

def main():
    st.title('HR Database Analysis')

    # Create three tabs
    tabs = ["AIM and Algorithm", "Program", "Output"]
    selected_tab = st.sidebar.selectbox("Select Tab", tabs)

    # Tab 1: AIM and Algorithm
    if selected_tab == "AIM and Algorithm":
        st.subheader("AIM and Algorithm")
        st.write("""
        **AIM:** 
        The aim of this analysis is to perform an SQL Inner Join operation on two tables in an HR database to retrieve employee information along with their respective departments.
        
        **Algorithm Steps:**
        1. Connect to the HR database.
        2. Execute an SQL Inner Join query between the `employees` and `departments` tables.
        3. Fetch the result of the query.
        4. Display the output.
        """)

    # Tab 2: Program
    elif selected_tab == "Program":
        st.subheader("Program")
        st.write("""
        ```python
        import sqlite3
        import pandas as pd

        # Function to create and populate the HR database
        def create_hr_database():
            # Code omitted for brevity

        # Function to perform SQL Inner Join and display results
        def inner_join():
            # Code omitted for brevity

        def main():
            # Code omitted for brevity

        if __name__ == '__main__':
            main()
        ```
        """)

    # Tab 3: Output
    elif selected_tab == "Output":
        st.subheader("Output")
        create_hr_database()  # Create and populate the database
        df = inner_join()  # Perform Inner Join
        st.write(df)  # Display output

if __name__ == '__main__':
    main()
