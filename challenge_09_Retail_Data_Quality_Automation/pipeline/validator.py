from pydantic import BaseModel, field_validator, ValidationError, EmailStr

# --- OrderItem Model ---
class OrderItem(BaseModel):
    product_id: str
    qty: int

    @classmethod
    @field_validator('product_id')
    def not_empty_product_id(cls, v):
        if not v:
            raise ValueError('product_id must not be empty')
        return v

    @classmethod
    @field_validator('qty')
    def qty_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('qty must be positive')
        return v

# --- Order Model ---
class Order(BaseModel):
    order_id: int
    customer_id: str
    items: list[OrderItem]
    date: str

    @classmethod
    @field_validator('customer_id')
    def not_empty_customer_id(cls, v):
        if not v:
            raise ValueError('customer_id must not be empty')
        return v

    @classmethod
    @field_validator('items')
    def not_empty_items(cls, v):
        if not v or not isinstance(v, list):
            raise ValueError('items must be a non-empty list')
        return v

def validate_orders(orders):
    errors = []
    for i, order in enumerate(orders):
        try:
            Order(**order)
        except ValidationError as e:
            for err in e.errors():
                errors.append(f"Order at index {i}: {err['loc'][0]} - {err['msg']}")
    return errors

# --- Product Model ---
class Product(BaseModel):
    product_id: str
    name: str
    price: float

    @classmethod
    @field_validator('product_id')
    def not_empty_product_id(cls, v):
        if not v:
            raise ValueError('product_id must not be empty')
        return v

    @classmethod
    @field_validator('name')
    def not_empty_name(cls, v):
        if not v:
            raise ValueError('name must not be empty')
        return v

    @classmethod
    @field_validator('price')
    def non_negative_price(cls, v):
        if v < 0:
            raise ValueError('price must not be negative')
        return v

def validate_products(products):
    errors = []
    for i, prod in enumerate(products):
        try:
            Product(**prod)
        except ValidationError as e:
            for err in e.errors():
                errors.append(f"Product at index {i}: {err['loc'][0]} - {err['msg']}")
    return errors

# --- Customer Model ---
class Customer(BaseModel):
    customer_id: str
    name: str
    email: EmailStr = None

    @classmethod
    @field_validator('customer_id')
    def not_empty_customer_id(cls, v):
        if not v:
            raise ValueError('customer_id must not be empty')
        return v

    @classmethod
    @field_validator('name')
    def not_empty_name(cls, v):
        if not v:
            raise ValueError('name must not be empty')
        return v

def validate_customers(customers):
    errors = []
    for i, cust in enumerate(customers):
        try:
            Customer(**cust)
        except ValidationError as e:
            for err in e.errors():
                errors.append(f"Customer at index {i}: {err['loc'][0]} - {err['msg']}")
    return errors

# --- Config Model ---
class Config(BaseModel):
    output_dir: str
    min_order_value: int

def validate_config(config):
    errors = []
    try:
        Config(**config)
    except ValidationError as e:
        for err in e.errors():
            errors.append(f"Config: {err['loc'][0]} - {err['msg']}")
    return errors