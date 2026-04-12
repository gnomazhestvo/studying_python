from name_function import get_formatted_name

def test_first_last_name():
    """Поддерживаются ли имена типа "Настя Шкурина"?"""
    formatted_name = get_formatted_name('настя', 'шкурина')
    assert formatted_name == 'Настя Шкурина'

def test_first_last_middle_name():
    """Поддерживаются ли такие имена как Анастасия Дмитриевна Шкурина?"""
    formatted_name = get_formatted_name('анастасия', 'шкурина', 'дмитриевна')
    assert formatted_name == 'Анастасия Дмитриевна Шкурина'