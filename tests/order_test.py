def test_order_validation():
    from customer import Customer
    from coffee import Coffee
    from order import Order
    try:
        Order(Customer("Test"), Coffee("Mocha"), 0.5)
        assert False
    except ValueError:
        assert True