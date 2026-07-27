dim_customer = df_raw[['Customer_Name', 'Email']].drop_duplicates()

dim_customer = dim_customer.reset_index(drop=True)
dim_customer['customer_id'] = dim_customer.index + 1

dim_customer = dim_customer[['customer_id', 'Customer_Name', 'Email']]