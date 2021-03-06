"""Файл codeless_sample.py содержит автоматически сгенерированный Codeless-рекордером код"""

# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_test(self):
        self.driver.get("http://selenium1py.pythonanywhere.com/en-gb/")
        self.driver.set_window_size(1535, 824)
        self.driver.find_element(By.ID, "login_link").click()
        self.driver.find_element(By.ID, "id_registration-email").click()
        self.driver.find_element(By.ID, "id_registration-email").send_keys("luda11@mail.ru")
        self.driver.find_element(By.ID, "id_registration-password1").click()
        self.driver.find_element(By.ID, "id_registration-password1").send_keys("123456Test!")
        self.driver.find_element(By.ID, "id_registration-password2").click()
        self.driver.find_element(By.ID, "id_registration-password2").send_keys("123456Test!")
        self.driver.find_element(By.NAME, "registration_submit").click()
