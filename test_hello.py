def test_greet():
    # test if the function is defined
    from hello import greet
    assert greet('Alice') == 'Hello, Alice'