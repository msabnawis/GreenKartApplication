from selenium.webdriver.common.by import By

from GreenKartApplication.GreeenKartUtilities.BaseClass import BaseClass
from GreenKartApplication.GreenKartPOM.ConfirmPage import GKConfirmPage


class GKCheckoutPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    codetext = (By.CSS_SELECTOR, '.promoCode')
    apply = (By.CSS_SELECTOR, '.promoBtn')
    message = (By.CSS_SELECTOR, '.promoInfo')
    price = (By.CSS_SELECTOR, 'tr td:nth-child(5) p')
    totalAmount = (By.CSS_SELECTOR, 'span[class = "totAmt"]')
    discountAmount = (By.CSS_SELECTOR, 'span[class = "discountAmt"]')
    placeorder = (By.XPATH, '//button[contains(text(),"Place Order")]')

    def getpromocode(self):
        return self.driver.find_element(*GKCheckoutPage.codetext)

    def clickApply(self):
        return self.driver.find_element(*GKCheckoutPage.apply)

    def getMessage(self):
        return self.driver.find_element(*GKCheckoutPage.message)

    def getPrices(self):
        return self.driver.find_elements(*GKCheckoutPage.price)

    def getTotalAmount(self):
        return self.driver.find_element(*GKCheckoutPage.totalAmount)

    def getTotalDiscount(self):
        return self.driver.find_element(*GKCheckoutPage.discountAmount)

    def clickPlaceOrder(self):
        self.driver.find_element(*GKCheckoutPage.placeorder).click()
        confirmPage = GKConfirmPage(self.driver)
        return confirmPage
