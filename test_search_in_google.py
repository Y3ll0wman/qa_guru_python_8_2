from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_search_returns_should_be_no_results():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('eolfdk;l77777gidjxcznb44444hdkjasdhf888ghkl').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
