from page_objects.locators import ShoppingCartSummaryLocators
total_list = []


class ShoppingCartSummaryPage:
    def __init__(self, webdriver_obj):
        self.webdriver_obj = webdriver_obj
        self.total_product = self.webdriver_obj.find_element(*ShoppingCartSummaryLocators.TotalProduct)
        self.total_wrapping = self.webdriver_obj.find_element(*ShoppingCartSummaryLocators.TotalWrapping)
        self.total_shipping = self.webdriver_obj.find_element(*ShoppingCartSummaryLocators.TotalShipping)
        self.total_discount = self.webdriver_obj.find_element(*ShoppingCartSummaryLocators.TotalDiscount)
        self.actual_total_pricewithouttax = self.webdriver_obj.find_element(*ShoppingCartSummaryLocators.TotalPriceWithoutTax)
        self.total_tax = self.webdriver_obj.find_element(*ShoppingCartSummaryLocators.TotalTax)
        self.total_price = self.webdriver_obj.find_element(*ShoppingCartSummaryLocators.TotalPrice)

    def expected_total_price_equal_to_actual_total_price(self):
        expected_total_pricewithouttax = 0.00
        i = 0

        global total_list
        total_list = [self.total_product, self.total_wrapping, self.total_shipping, self.total_discount, self.actual_total_pricewithouttax, self.total_tax, self.total_price]
        for each_item in total_list:
            if each_item.text != '':
                total_list[i] = float(each_item.text[1:])
            else:
                total_list[i] = 0.00
            i=i+1
        expected_total_pricewithouttax = sum(total_list[0:4])
        assert total_list[4] == expected_total_pricewithouttax
        assert total_list[6] == total_list[4] + total_list[5]
