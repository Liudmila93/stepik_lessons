from selenium import webdriver
"""
Вход пользователя в систему с верными данными 1.2.1
Предусловия: пользователь должен быть зарегистрирован. Пользователь нахоится на главной странице
Шаги:
1. Нажать кнопку "Войти или зарегистрироваться" (проверяем что нас отправляют на страницу с окнами "войти" и "зарегистрироваться") - открывается окно авторизации и регистрации пользователя
2. В окне входа в систему в поле "Адрес электронной почты" вводим существующую почту для ранее зарегестрированнного пользователя (проверяем что почта проходит по валидации)
3. В окне входа в систему в поле "Пароль" вводим существующий пароль для ранее зарегестрированнного пользователя  (проверяем что валидный пароль принимается без ошибок)
4. Нажимаем "Войти"(проверяем возможность входа в систему с верными логин/паролем) - Пользователь находится на главной странице странице. Отображается сообщение "Рады видеть вас снова". На странице в верхнем правом углу появилась кнопка "Выход" и "Аккаунт"
"""

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

login_btn_on_main_page = "#login_link"
login_mail_field = "[name='login-username']"
login_password_field = "[name='login-password']"
login_btn_on_login_page = "[name='login_submit']"
greeting_alert = ".alertinner"


def test_go_to_login_page():
    # Data
    login_page_url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(6)
        browser.get(main_page_link)

        # Act
        browser.find_element_by_css_selector(login_btn_on_main_page).click()

        # Assert
        assert browser.current_url == login_page_url, "User is redirected to the wrong page"

    finally:
        browser.quit()


def test_user_login_succesfully():
    # Data
    mail = "ludo4ka.th@mail.ru"
    password = "221063sla"
    greeting = "Рады видеть вас снова"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(6)
        browser.get(main_page_link)
        browser.find_element_by_css_selector(login_btn_on_main_page).click()

        # Act
        mail_input = browser.find_element_by_css_selector(login_mail_field)
        mail_input.click()
        mail_input.send_keys(mail)

        password_input = browser.find_element_by_css_selector(login_password_field)
        password_input.click()
        password_input.send_keys(password)

        log_in_btn = browser.find_element_by_css_selector(login_btn_on_login_page)
        log_in_btn.click()

        # Assert
        greeting_alert_after_login = browser.find_element_by_css_selector(greeting_alert)
        assert greeting in greeting_alert_after_login.text, \
            "Page after login does not contain greeting message - login unsuccessfully"

    finally:
        browser.quit()


test_go_to_login_page()
test_user_login_succesfully()
