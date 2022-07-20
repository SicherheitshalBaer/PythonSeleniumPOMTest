from selenium.webdriver.common.by import By


class LoginPageLocators:

    element_username_by_name = (By.NAME, "uname")
    element_password_by_name = (By.NAME, "pass")
    element_LoginButton_by_class = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tbody/tr/td[4]/table[2]/tbody/tr/td/table/tbody/tr/td/form/input[2]")
