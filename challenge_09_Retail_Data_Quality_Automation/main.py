from pipeline.validator import (
    validate_orders, validate_products, validate_customers, validate_config
)
import json
import pandas as pd

with open("data/orders.json") as f:
    orders = json.load(f)
order_errors = validate_orders(orders)

products = pd.read_csv("data/products.csv").to_dict(orient="records")
product_errors = validate_products(products)

with open("data/customers.json") as f:
    customers = json.load(f)
customer_errors = validate_customers(customers)

with open("config/config.json") as f:
    config = json.load(f)
config_errors = validate_config(config)

any_errors = False
if order_errors:
    print("Order errors found:")
    for e in order_errors:
        print("  ", e)
    any_errors = True
if product_errors:
    print("Product errors found:")
    for e in product_errors:
        print("  ", e)
    any_errors = True
if customer_errors:
    print("Customer errors found:")
    for e in customer_errors:
        print("  ", e)
    any_errors = True
if config_errors:
    print("Config errors found:")
    for e in config_errors:
        print("  ", e)
    any_errors = True

if any_errors:
    print("\n❌ Validation failed. Fix errors before running pipeline.")
    exit(1)

print("✅ All data validated! Ready for processing pipeline...")
