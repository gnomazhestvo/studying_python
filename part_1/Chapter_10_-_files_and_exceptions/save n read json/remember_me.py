from pathlib import Path
import json

def get_stored_username(path):
    """Получает сохраненное в файле имя пользователя, если оно
    существует."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    username = input('What is your name?\n')
    contents = json.dumps(username.title())
    path.write_text(contents)
    return username

def greet_user(path):
    """Приветствует пользователя по имени."""
    username = get_stored_username(path)
    if username:
        print(f'Welcome back, {username}')
    else:
        username = get_new_username(path)
        print(f'We will remember you next time, {username.title()}!\n')

path = Path('username.json')
greet_user(path)