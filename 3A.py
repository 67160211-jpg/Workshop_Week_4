conn = sqlite3.connect('warehouse.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dim_customer (
        customer_id INTEGER PRIMARY KEY,
        Customer_Name TEXT,
        Email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dim_product (
        product_id INTEGER PRIMARY KEY,
        Product TEXT
    )
''')
conn.commit()