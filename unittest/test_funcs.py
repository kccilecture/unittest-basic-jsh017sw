from my_funcs import is_even, get_average, get_max, get_min


def test_is_even_true():
    assert is_even(2) is True
    assert is_even(10) is True
    assert is_even(0) is True


def test_is_even_false():
    assert is_even(1) is False
    assert is_even(7) is False
    assert is_even(-3) is False


def test_get_average():
    assert get_average([1, 2, 3, 4, 5]) == 3.0
    assert get_average([10, 20, 30]) == 20.0
    assert get_average([7]) == 7.0


def test_get_max():
    assert get_max([1, 2, 3, 4, 5]) == 5
    assert get_max([-10, -3, -7]) == -3
    assert get_max([100]) == 100


def test_get_min():
    assert get_min([1, 2, 3, 4, 5]) == 1
    assert get_min([-10, -3, -7]) == -10
    assert get_min([100]) == 100