def test_coffee_name_validation():
    from coffee import Coffee
    try:
        Coffee("AB")
        assert False
    except ValueError:
        assert True