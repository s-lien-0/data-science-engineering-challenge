from pipeline.validator import (
    validate_orders, validate_products, validate_customers, validate_config
)

def test_validate_orders_good():
    good_orders = [
        {
            "order_id": 1,
            "customer_id": "C001",
            "items": [{"product_id": "P001", "qty": 2}],
            "date": "2024-06-01"
        }
    ]
    assert validate_orders(good_orders) == []

def test_validate_orders_bad():
    bad_orders = [
        {
            "order_id": 2,
            "customer_id": "",
            "items": [],
            "date": "2024-06-01"
        },
        {
            "order_id": 3,
            "customer_id": "C003",
            "items": [{"product_id": "", "qty": -1}],
            "date": "2024-06-02"
        }
    ]
    errors = validate_orders(bad_orders)
    assert len(errors) >= 3
    assert any("customer_id" in e for e in errors)
    assert any("items" in e for e in errors)
    assert any("product_id" in e for e in errors)
    assert any("qty" in e and "positive" in e for e in errors)

def test_validate_products_good():
    good_products = [
        {'product_id': 'P001', 'name': 'Apple', 'price': 0.99},
        {'product_id': 'P002', 'name': 'Banana', 'price': 1.2}
    ]
    assert validate_products(good_products) == []

def test_validate_products_bad():
    bad_products = [
        {'product_id': '', 'name': 'Apple', 'price': 0.99},
        {'product_id': 'P003', 'name': '', 'price': 0.99},
        {'product_id': 'P004', 'name': 'Orange', 'price': -1}
    ]
    errors = validate_products(bad_products)
    assert len(errors) == 3
    assert any("product_id" in e for e in errors)
    assert any("name" in e for e in errors)
    assert any("price" in e and "negative" in e for e in errors)

def test_validate_customers_good():
    good_customers = [
        {'customer_id': 'C001', 'name': 'Alice Smith', 'email': 'alice@example.com'},
        {'customer_id': 'C002', 'name': 'Bob Jones', 'email': 'bob@example.com'}
    ]
    assert validate_customers(good_customers) == []

def test_validate_customers_bad():
    bad_customers = [
        {'customer_id': '', 'name': 'Alice Smith', 'email': 'alice@example.com'},
        {'customer_id': 'C003', 'name': '', 'email': 'bob@example.com'},
        {'customer_id': 'C004', 'name': 'Jane', 'email': 'not-an-email'}
    ]
    errors = validate_customers(bad_customers)
    assert len(errors) == 3
    assert any("customer_id" in e for e in errors)
    assert any("name" in e for e in errors)
    assert any("email" in e for e in errors)

def test_validate_config_good():
    good_config = {'output_dir': 'reports', 'min_order_value': 10}
    assert validate_config(good_config) == []

def test_validate_config_bad():
    bad_config = {'output_dir': '', 'min_order_value': 'ten'}
    errors = validate_config(bad_config)
    assert len(errors) >= 1
    assert any("output_dir" in e or "min_order_value" in e for e in errors)