import sqlite3

# Connect to the database
conn = sqlite3.connect("inventory.db")

# Create a cursor
cursor = conn.cursor()

# Create the table
table_query = '''
CREATE TABLE IF NOT EXISTS inventory (
    item_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
);
'''
cursor.execute(table_query)

# Function to add a new item to the inventory
def add_item():
    item_id = input("Enter the ID of the item: ")
    name = input("Enter the name of the item: ")
    quantity = input("Enter the quantity of the item: ")
    price = input("Enter the price of the item: ")
    insert_query = '''
    INSERT INTO inventory (item_id, name, quantity, price)
    VALUES (?,?,?,?);
    '''
    cursor.execute(insert_query, (item_id, name, quantity, price))
    conn.commit()

# Function to delete an item from the inventory
def delete_item():
    item_id = input("Enter the ID of the item to delete: ")
    delete_query = '''
    DELETE FROM inventory
    WHERE item_id=?;
    '''
    cursor.execute(delete_query, (item_id,))
    conn.commit()

# Function to search for an item in the inventory
def search_item():
    name = input("Enter the name of the item to search for: ")
    search_query = '''
    SELECT * FROM inventory
    WHERE name=?;
    '''
    cursor.execute(search_query, (name,))
    return cursor.fetchall()

# Function to update the quantity of an item in the inventory
def update_quantity():
    item_id = input("Enter the ID of the item to update: ")
    quantity = input("Enter the new quantity for the item: ")
    update_query = '''
    UPDATE inventory
    SET quantity=?
    WHERE item_id=?;
    '''
    cursor.execute(update_query, (quantity, item_id))
    conn.commit()

# Close the connection to the database
conn.close()
