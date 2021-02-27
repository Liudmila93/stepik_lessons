from selenium import webdriver
import time
link = "http://selenium1py.pythonanywhere.com/en-gb/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    login_btn = browser.find_element_by_css_selector("#login_link")
    login_btn.click()
    input_email = browser.find_element_by_css_selector("#id_registration-email")
    input_email.send_keys("ludo4ka@mail.ru")
    input_password = browser.find_element_by_css_selector("#id_registration-password1")
    input_password.send_keys("Test123!!")
    input_password_confirm = browser.find_element_by_css_selector("#id_registration-password2")
    input_password_confirm.send_keys("Test123!!")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[name='registration_submit']")
    button.click()
    time.sleep(5)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_css_selector(".alertinner.wicon")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Thanks for registering!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
