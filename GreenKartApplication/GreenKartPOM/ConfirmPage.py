from selenium.webdriver.common.by import By


class GKConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    dropdown = (By.TAG_NAME, "select")
    countries = (By.XPATH, '//select/option')
    checkbox = (By.CSS_SELECTOR, '.chkAgree')
    submit = (By.TAG_NAME, "button")
    message = (By.XPATH, "//div[@class = 'wrapperTwo']/span")

    def clickDropdown(self):
        return self.driver.find_element(*GKConfirmPage.dropdown)

    def selectCountry(self):
        return self.driver.find_elements(*GKConfirmPage.countries)

    def clickCheckbox(self):
        return self.driver.find_element(*GKConfirmPage.checkbox)

    def clickProceed(self):
        return self.driver.find_element(*GKConfirmPage.submit)

    def getMessage(self):
        return self.driver.find_element(*GKConfirmPage.message)