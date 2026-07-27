fact_sales = pd.merge(df_raw, dim_customer,
                      on=['Customer_Name', 'Email'],
                      how='left')

fact_sales = fact_sales.drop(columns=['Customer_Name', 'Email'])

# ทำซ้ำกระบวนการนี้กับ Product และ Time Dimensions

dim_product = fact_sales[['Product']].drop_duplicates().reset_index(drop=True)
dim_product['product_id'] = dim_product.index + 1
dim_product = dim_product[['product_id', 'Product']]

fact_sales = pd.merge(fact_sales, dim_product, on=['Product'], how='left')

fact_sales = fact_sales.drop(columns=['Product'])