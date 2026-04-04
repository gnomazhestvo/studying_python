# 8.9. Сообщения.
# Создайте список с серией коротких сообщений. Передайте
# список функции show_messages(), которая выводит текст
# каждого сообщения в списке.
print()
print('8.9. Сообщения.\n')

messages = ['message0', 'message1', 'message2', 'message3']

def show_messages(messages):
    while messages:
        message = messages.pop(0)
        print(message)

show_messages(messages)
print()

# 8.10. Отправка сообщений.
# Начните с копии вашей программы из упражнения 8.9. Напишите
# функцию send_messages(), которая выводит каждое сообщение и
# перемещает его в новый список sent_messages. После вызова
# функции выведите оба списка и убедитесь в том, что
# перемещение прошло успешно.

print('8.10. Отправка сообщений.\n')

messages = ['message0', 'message1', 'message2', 'message3']
sent_messages = []

def show_messages_sequence(messages, sent_messages):
    print('--- К отправке запланирован список: ---')
    print(messages)
    print()
    print('--- Уже отправлено: ---')
    print(sent_messages)
    print()

def send_messages(messages, sent_messages):
    print('--- Очередь отправки сообщений ---')
    while messages:
        sending_message = messages.pop(0)
        print(f'Отправляю сообщение: "{sending_message}.') 
        sent_messages.append(sending_message)
    print('--- Отправка завершена ---\n')

show_messages_sequence(messages, sent_messages)
send_messages(messages, sent_messages)
show_messages_sequence(messages, sent_messages)

print()

# 8.11. Архивированные сообщения.
# Начните с программы из упражнения 8.10. Вызовите функцию
# send_messages(), чтобы создать копию списка сообщений.
# После вызова функции выведите оба списка и убедитесь в том,
# что в исходном списке остались все сообщения.

print('8.11. Архивированные сообщения.\n')

messages = ['message0', 'message1', 'message2', 'message3']
sent_messages = []

show_messages_sequence(messages, sent_messages)
send_messages(messages[:], sent_messages)
show_messages_sequence(messages, sent_messages)