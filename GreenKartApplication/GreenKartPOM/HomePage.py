from selenium.webdriver.common.by import By

from GreenKartApplication.GreenKartPOM.CheckoutPage import GKCheckoutPage


class GKHomePage:
    def __init__(self, driver):
        self.driver = driver

    searchitem = (By.XPATH, "//input[@type='search']")
    itemstext = (By.XPATH, "//div[@class='product']/h4")
    additemstocart = (By.XPATH, "//div[@class='products']/div/div/button")
    cart_image = (By.CSS_SELECTOR, ".cart-icon")
    checkout = (By.XPATH, "(//div[@class='action-block'])[1]")

    def searchitembyname(self):
        return self.driver.find_element(*GKHomePage.searchitem)

    def getallitemstext(self):
        return self.driver.find_elements(*GKHomePage.itemstext)

    def addToCart(self):
        return self.driver.find_elements(*GKHomePage.additemstocart)

    def click_cart(self):
        return self.driver.find_element(*GKHomePage.cart_image)

    def proceedToCheckout(self):
        self.driver.find_element(*GKHomePage.checkout).click()
        checkoutPage = GKCheckoutPage(self.driver)
        return checkoutPage