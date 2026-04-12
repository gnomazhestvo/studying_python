# 10.11. Любимое число.
# Напишите программу, которая запрашивает у пользователя его
# любимое число. Воспользуйтесь функцией json.dumps() для
# сохранения этого числа в файле. Напишите другую программу,
# которая читает это значение и выводит сообщение: «Я знаю
# ваше любимое число! Это _____».
# 
# 10.12. Сохраненное любимое число.
# Объедините две программы из упражнения 10.11 в файл. Если
# число уже сохранено, то сообщите его пользователю, а если
# нет — запросите любимое число пользователя и сохраните в
# файле. Выполните программу дважды, чтобы убедиться в том,
# что она работает.

from pathlib import Path
import json

print('\n10.11, 10.12. Любимое число.\n')

def whether_favorite_number_exists(path):
    """Проверяет, сообщал ли пользователь любимое число."""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None

def write_new_favorite_number(path):
    """Запрашивает у пользователя любимое число."""
    number = input('Введите ваше любимое число:\n')
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def show_written_favorite_number(path):
    """Выдает любимое число на экран, если оно записано. Если
    нет - запрашивает его."""
    number = whether_favorite_number_exists(path)
    if number:
        print(f'Я помню ваше любимое число: {number}')
    else:
        number = write_new_favorite_number(path)
        print(f'Ваше любимое число: {number}. Я запомню.')

path = Path('favorite_number.json')
show_written_favorite_number(path)