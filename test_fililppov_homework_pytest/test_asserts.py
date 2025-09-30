def test_asserts():
    s = "automation"
    assert len(s) == 10, "длина строки НЕ равна 10"


def test_max():
    spisok = [5, 9, 2, 7]
    assert max(spisok) == 9, "число 9 - НЕ максимальное"


def test_key():
    slovar = {"name": "QA", "level": 1}
    assert "name" in slovar, "словарь НЕ содержит ключ 'name'"
