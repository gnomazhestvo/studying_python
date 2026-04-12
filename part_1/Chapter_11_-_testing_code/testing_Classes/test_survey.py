from survey import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """Проверяет, что один ответ сохранен правильно."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Проверяет, что три ответы сохранены правильно."""
    responses = ['English', 'Russian', 'French']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses