import pandas as pd
import sqlite3

conn = sqlite3.connect('warehouse.db')

sql_query = """
SELECT
    c.Customer_Name,
    SUM(f.amount) as Total_Spend
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.Customer_Name
ORDER BY Total_Spend DESC
LIMIT 3;
"""

result_df = pd.read_sql_query(sql_query, conn)

print("--- ผลลัพธ์การคิวรีข้อมูล (Top 3 Customers) ---")
print(result_df)

conn.close()