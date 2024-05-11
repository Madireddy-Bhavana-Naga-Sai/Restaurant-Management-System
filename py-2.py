import mysql.connector

# Establish connection to MySQL server
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bhavana@20",
    database="RestaurantDB"  # Name of your MySQL database
)

# Create a cursor object
cursor = conn.cursor()

# Now you can execute SQL queries using cursor
