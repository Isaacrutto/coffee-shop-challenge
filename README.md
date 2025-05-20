@"
# ☕ Coffee Shop Challenge

This project models a simple coffee shop system using Python OOP. It defines three core entities: `Customer`, `Coffee`, and `Order`. The program enforces validations, object relationships, and aggregate methods using standard Python classes.

## 🗂 Project Structure
coffee-shop-challenge/
├── customer.py # Customer class with validation and relationships
├── coffee.py # Coffee class with immutable name and aggregate methods
├── order.py # Order class with validation and relationships
├── debug.py # Manual test runner for functionality demo
├── tests/ # Basic test scripts
│ ├── customer_test.py
│ ├── coffee_test.py
│ └── order_test.py
└── README.md # You are here ✅

markdown
Copy
Edit

## ✅ Features

### `Customer`
- Name must be 1–15 characters
- Can access orders and coffees
- `create_order(coffee, price)` to generate a new order
- Class method `most_aficionado(coffee)` to find the top spender

### `Coffee`
- Name must be ≥3 characters and is immutable after init
- Can access all related orders and customers
- Provides `num_orders()` and `average_price()` methods

### `Order`
- Links a `Customer` and a `Coffee`
- Enforces price as a float between 1.0 and 10.0
- All orders are tracked via a class-level list

## 🧪 How to Run

### Set up your environment:
```bash
pipenv install
pipenv shell
