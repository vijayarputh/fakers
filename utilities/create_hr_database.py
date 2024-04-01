import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('hr_database.db')
cursor = conn.cursor()

# Create employees table
cursor.execute('''CREATE TABLE employees (
                    employee_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    department_id INTEGER
                )''')

# Create departments table
cursor.execute('''CREATE TABLE departments (
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

print("HR database created and populated successfully.")
