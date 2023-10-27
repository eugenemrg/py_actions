def test_greet():
    # test if the function is defined
    from hello import greet
    assert greet('Alice') == 'Hello, Alice'

def test_greet_with_default():
    from hello import greet
    assert greet() == 'Hello, World!!!'

def test_greet_with_empty_string():
    from hello import greet
    assert greet('') == 'Hello, '

def test_greet_with_number():
    from hello import greet
    assert greet(123) == 'Hello, 123'