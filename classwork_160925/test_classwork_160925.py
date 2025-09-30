# some_value = "animal"
# some_value_2 = [1, 2, 3]
# some_int = 123


# def test_value_type():
#     assert isinstance(some_value, str)


# def test_value_type_int():
#     assert isinstance(some_int, int)


# def test_value_type2():
#     assert isinstance(
#         some_value, int
#     ), f"Ожидали что придет строка, а пришла {type(some_int)}"


# ----------------------------------------------

some_value_2 = [1, 2, 3]  # 3
some_value = "animal"


def test_length():
    assert len(some_value) == 6
    assert len(some_value_2) > 4


# print(len(some_value))  # 6

# ----------------------------------------------
