cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fact_sales (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product_id INTEGER,
        Amount REAL,
        FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
        FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
    )
''')
conn.commit()