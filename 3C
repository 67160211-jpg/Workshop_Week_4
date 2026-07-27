dim_customer.to_sql('dim_customer', con=conn, if_exists='replace', index=False)
dim_product.to_sql('dim_product', con=conn, if_exists='replace', index=False)

fact_sales.to_sql('fact_sales', con=conn, if_exists='replace', index=False)

print('ETL Pipeline ran successfully!')

conn.close()