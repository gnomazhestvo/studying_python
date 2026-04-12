from employee import Employee
import pytest

@pytest.fixture
def nastya():
    nastya = Employee('Анастасия', 'Шкурина', 80_000)
    return nastya

def test_give_default_raise(nastya):
    nastya.give_raise()
    assert nastya.salary == 85_000

def test_give_custom_raise(nastya):
    nastya.give_raise(16_000)
    assert nastya.salary == 96_000