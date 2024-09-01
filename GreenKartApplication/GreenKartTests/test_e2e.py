import time
from GreenKartApplication.GreeenKartUtilities.BaseClass import BaseClass
from GreenKartApplication.GreenKartPOM.HomePage import GKHomePage
from GreenKartApplication.TestData.GreenKartData import HomePageData


class TestEndToEndGreenKart(BaseClass):
    def test_e2e(self):
        log = self.getTestLogger()
        homePage = GKHomePage(self.driver)

        total = 0
        expectedList = HomePageData.expected_data
        actualList = []

        homePage.searchitembyname().send_keys("ca")
        items = homePage.getallitemstext()
        time.sleep(2)
        i = -1
        for item in items:
            i = i+1
            actualList.append(item.text)
            item_name = item.text
            if item_name == "Cauliflower - 1 Kg":
                homePage.addToCart()[i].click()
        log.info("Printing actual list of items:")
        log.info(actualList)
        assert expectedList == actualList
        time.sleep(2)
        homePage.click_cart().click()
        checkoutPage = homePage.proceedToCheckout()

        checkoutPage.getpromocode().send_keys("rahulshettyacademy")
        checkoutPage.clickApply().click()
        self.verifyTextPresence()
        message = checkoutPage.getMessage().text
        log.info(message)
        assert message == 'Code applied ..!'
        prices = checkoutPage.getPrices()
        for price in prices:
            total = total + int(price.text)

        log.info("Total price: " + str(total))

        totalAmount = checkoutPage.getTotalAmount()
        newtotalamount = int(totalAmount.text)
        assert newtotalamount == total

        discountAmount = checkoutPage.getTotalDiscount()
        newdiscountamount = float(discountAmount.text)
        assert newdiscountamount < newtotalamount

        confirmPage = checkoutPage.clickPlaceOrder()
        countries = confirmPage.selectCountry()
        log.info("Length of countries: " + str(len(countries)))
        log.info("Selecting Country...")
        for country in countries:
            if country.text == "India":
                country.click()
                break
        log.info("India is selected")
        confirmPage.clickCheckbox().click()
        confirmPage.clickProceed().click()
        confirmationMessage = confirmPage.getMessage()
        log.info(confirmationMessage.text)