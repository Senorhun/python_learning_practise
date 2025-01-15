import mysql.connector

server_connection = mysql.connector.connect(
    host = 'localhost',
    user='szaboptr',
    password='szaboptr'
)

cursor = server_connection.cursor()
cursor.execute('DROP DATABASE IF EXISTS fruits_new')
cursor.execute('CREATE DATABASE fruits_new')
server_connection.close()

schema_connection = mysql.connector.connect(
    host='localhost',
    user='szaboptr',
    password='szaboptr',
    database='fruits_new'
)
try:
    cursor = schema_connection.cursor()
    cursor.execute('''
        CREATE TABLE fruits_new(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            amount INT)
    ''')

    fruits_insert= 'INSERT INTO fruits_new(name, amount) VALUES (%s, %s)'
    cursor.execute(fruits_insert, ('apple', 3))
    cursor.execute(fruits_insert, ('banana', 2))
    cursor.execute(fruits_insert, ('orange', 5))

    cursor.execute('SELECT * FROM fruits_new')
    fruits = cursor.fetchall()
    for fruit in fruits:
        print(fruit)

except Exception as e:
    print(e)
    schema_connection.rollback()
else:
    schema_connection.commit()
schema_connection.close()