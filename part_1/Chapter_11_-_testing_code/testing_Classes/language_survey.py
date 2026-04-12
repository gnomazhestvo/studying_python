from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра класса AnonymousSurvey:
question = '\nWhat language did you first learn to speak?'
language_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов:
language_survey.show_question()
print('Enter "q" at any time to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        print('== == == ==\n')
        break
    language_survey.store_response(response)

# Вывод результатов опроса:
print('\nThank you for participating!')
language_survey.show_results()
