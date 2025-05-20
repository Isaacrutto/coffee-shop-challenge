def test_customer_name_validation():
    from customer import Customer
    try:
        Customer("")
        assert False
    except ValueError:
        assert True