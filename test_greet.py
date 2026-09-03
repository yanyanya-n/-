from greet import greet


def test_greet_basic():
    assert greet("World") == "Hello, World!"


def test_greet_empty_name():
    assert greet("") == "Hello, !"
