import mysql.connector


host='localhost'
user='root'
password='Babula@143'
database='adminshell'


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Babula@143'
)


cursor = conn.cursor()


cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")


cursor.execute(f"USE {database}")


create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);
"""
cursor.execute(create_table_query)


conn.commit()
conn.close()

print(f"Database '{database}' and table 'users' created successfully.")