
class CartLocators:
    baseURL = "https://www.demoblaze.com/index.html"
    cart_link_locator_linkText = "Cart"
    cart_delete_link_locator_linktext = "Delete"
    cart_total_price_id = "totalp"
    cart_place_order_xpath = "//button[contains(text(),'Place Order')]"
    place_order_name_field_id = "name"
    place_order_country_field_id = "country"
    place_order_city_field = "city"
    place_order_credit_card_field_id = "card"
    place_order_month_filed_id = "month"
    place_order_year_field_id = "year"
    place_order_purchase_button_xpath = "//button[contains(text(),'Purchase')]"
    place_order_close_button_xpath = "//body/div[@id='orderModal']/div[1]/div[1]/div[3]/button[1]"
    sample_product_1_link_text = "Samsung galaxy s6"
    add_to_cart_button_xpath = "//a[contains(text(),'Add to cart')]"
    sample_product_name_within_cart_xpath = "//tbody/tr[1]/td[2]"
    sample_product_price_within_cart_xpath = "//tbody/tr[1]/td[3]"
    place_order_confirmation_message_xpath = "//h2[contains(text(),'Thank you for your purchase!')]"