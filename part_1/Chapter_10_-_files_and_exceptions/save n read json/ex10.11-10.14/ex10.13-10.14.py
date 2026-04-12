# 10.13. Словарь пользователя.
# В программе remember_me.py хранится только один вид
# данных — имя пользователя. Дополните этот пример,
# запросив еще два вида информации о пользователе, а затем
# сохраните все собранные данные в словарь. Запишите его в
# файл с помощью функции json.dumps() и прочитайте данные
# с помощью функции json.loads(). Выведите сводку, какие
# именно данные о пользователе сохранила ваша программа.
# 
# 10.14. Проверка пользователя.
# Последняя версия remember_me.py предполагает, что
# пользователь либо уже ввел свое имя, либо программа
# выполняется впервые. Ее нужно изменить на тот случай, если
# текущий пользователь не является тем человеком, который
# использовал программу последним.
# Прежде чем выводить приветствие в greet_user(),
# спросите пользователя, правильно ли определено его имя.
# Если ответ будет отрицательным, то вызовите
# get_new_username() для получения правильного имени
# пользователя.

from pathlib import Path
import json

print('\n10.13, 10.14. Словарь пользователя.\n')

def get_stored_user(path):
    """Возвращает информацию о пользователе, если он
    существует. Если нет - не возвращает ничего."""
    if path.exists():
        contents = path.read_text()
        return(json.loads(contents))
    else:
        return None
   
def get_new_user(path):
    """Создает нового пользователя, сохраняет его в файле
    и возвращает данные."""
    userinfo = {}
    userinfo['username'] = input('Похоже, ты новичок тут.\nВведи свое имя:\n')
    userinfo['location'] = input('Откуда ты?\n')
    userinfo['birthday'] = input('Введи дату рождения в формате ДД.ММ.ГГГГ:\n')
    contents = json.dumps(userinfo)
    path.write_text(contents)
    return(userinfo)
        
def check_user(path):
    """Проверяет, является ли пользователь тем, кто использовал
    программу в последний раз. Если да, то приветствует его,
    если нет - создает новый профиль."""
    userinfo = get_stored_user(path)
    if userinfo:
        print(f'Привет! Ты {userinfo['username']}?\n')
        check = input('(y/n)\n')
        if check.lower() == 'y':
            return userinfo
        else:
            return None # пользователь не тот
    else:
        return None # файл отсутствует
    
def greet_user(path):
    """Приветствует существующего пользователя или создает
    нового."""
    userinfo = check_user(path)
    if userinfo: # пользователь подтвержден
        print(f'Добро пожаловать домой, {userinfo['username'].title()}.')
        print(f'Регион: {userinfo['location'].title()}.')
        print(f'Дата рождения: {userinfo['birthday']}.')
    else: # создаем нового пользователя
        userinfo = get_new_user(path)
        print(f'Спасибо, {userinfo['username']}. Теперь это и твой дом.')

path = Path('userinfo.json')
greet_user(path)