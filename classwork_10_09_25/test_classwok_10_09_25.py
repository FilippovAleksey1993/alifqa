# def test_sum():
#     assert 2 + 2 == 4


# def test_string():
#     assert "qa" in "qa course"


# def test_ckeck_length():
#     actual_length = len([1, 2, 3])

#     try:
#         assert actual_length == 3, "dlina norm"
#         assert actual_length < 3
#         assert actual_length < 5
#         assert actual_length < 9
#     except:
#         raise AssertionError


# def add(a, b):
#     return a + b


# def test_add():
#     result = add(2, 3)
#     assert result == 5


def sum(a, b):
    return a + b


def test_sum():
    assert sum(a=5, b=4) == 10
