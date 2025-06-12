from pipeline.validator import (
    validate_orders, validate_products, validate_customers, validate_config
)

import json
import pandas as pd

with open("data/orders.json") as f:
    orders = json.load(f)
validate_orders(orders)

products = pd.read_csv("data/products.csv")
validate_products(products)

with open("data/customers.json") as f:
    customers = json.load(f)
validate_customers(customers)

with open("config/config.json") as f:
    config = json.load(f)
validate_config(config)

print("All data validated!")
