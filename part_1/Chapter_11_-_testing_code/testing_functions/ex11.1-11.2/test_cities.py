from city_functions import city_contry

def test_city_country():
    """Правильно ли выводится результат типа "Santiago, Chile"?"""
    message = city_contry('santiago', 'chile')
    assert message == 'Santiago, Chile'

def test_city_country_population():
    """Правивльно ли выводится результат типа
    "Santiago, Chile - population 500"?"""
    message = city_contry('Santiago', 'chile', 500)
    assert message == 'Santiago, Chile - population 500'