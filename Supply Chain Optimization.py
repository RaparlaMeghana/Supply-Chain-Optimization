import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Generating sample data for Amazon, Flipkart, and Meesho
def generate_data(num_entries):
    data = []

    for i in range(num_entries):
        product_id = f'P{i + 1}'
        seller_id_amazon = f'Amazon_Seller{i + 1}'
        seller_id_flipkart = f'Flipkart_Seller{i + 1}'
        seller_id_meesho = f'Meesho_Seller{i + 1}'
        price = np.random.uniform(10, 100)
        quantity = np.random.randint(1, 10)
        order_date = datetime(2022, 1, 1) + timedelta(days=np.random.randint(1, 365))

        data.append({
            'ProductID': product_id,
            'SellerID_Amazon': seller_id_amazon,
            'SellerID_Flipkart': seller_id_flipkart,
            'SellerID_Meesho': seller_id_meesho,
            'Price': price,
            'Quantity': quantity,
            'OrderDate': order_date
        })

    return data

# Generating data for approximately 100 products
num_entries_per_platform = 100
amazon_data = generate_data(num_entries_per_platform)
flipkart_data = generate_data(num_entries_per_platform)
meesho_data = generate_data(num_entries_per_platform)

# Creating dataframes
amazon_df = pd.DataFrame(amazon_data)
flipkart_df = pd.DataFrame(flipkart_data)
meesho_df = pd.DataFrame(meesho_data)

# Saving data to CSV files
amazon_df.to_csv('amazon_data.csv', index=False)
flipkart_df.to_csv('flipkart_data.csv', index=False)
meesho_df.to_csv('meesho_data.csv', index=False)
print("Amazon Data:")
print(amazon_df.head())
print("\nFlipkart Data:")
print(flipkart_df.head())
print("\nMeesho Data:")
print(meesho_df.head())
