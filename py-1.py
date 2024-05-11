import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Menu (
        item_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
        FOREIGN KEY (item_id) REFERENCES Menu (item_id)
    )
''')

# Functions for CRUD operations

def add_customer(name, phone):
    cursor.execute('INSERT INTO Customers (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()

def add_menu_item(name, price):
    cursor.execute('INSERT INTO Menu (name, price) VALUES (?, ?)', (name, price))
    conn.commit()

def place_order(customer_id, item_id, quantity):
    cursor.execute('INSERT INTO Orders (customer_id, item_id, quantity) VALUES (?, ?, ?)', (customer_id, item_id, quantity))
    conn.commit()

def view_orders():
    cursor.execute('''
        SELECT Orders.order_id, Customers.name, Menu.name, Menu.price, Orders.quantity
        FROM Orders
        JOIN Customers ON Orders.customer_id = Customers.customer_id
        JOIN Menu ON Orders.item_id = Menu.item_id
    ''')
    orders = cursor.fetchall()
    for order in orders:
        print(order)

def delete_order(order_id):
    cursor.execute('DELETE FROM Orders WHERE order_id = ?', (order_id,))
    conn.commit()

# Sample data
add_customer('John Doe', '123-456-7890')
add_menu_item('Burger', 5.99)
add_menu_item('Pizza', 8.99)

# Test CRUD operations
place_order(1, 1, 2)  # John Doe orders 2 burgers
place_order(1, 2, 1)  # John Doe orders 1 pizza

view_orders()

# Uncomment to test delete_order function
# delete_order(1)  # Delete the first order

# Close the connection
conn.close()
