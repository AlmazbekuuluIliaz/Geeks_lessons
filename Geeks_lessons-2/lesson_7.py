import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

connection = create_connection('group_34.db')
sql_create_empployees_table = '''
CREATE TABLE employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(200) NOT NULL,
salary FLOAT NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
is_married BOOLEAN DEFAULT FALSE
'''

if connection is not None:
    print('Successfully connected!')

    connection.close()