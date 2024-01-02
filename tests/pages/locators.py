from selenium.webdriver.common.by import By


class PageLocators:


    username_login = (By.ID, 'user-name')
    password_login = (By.ID, 'password')
    cta_login = (By.ID, 'login-button')
    add_item_cta = (By.ID, 'add-to-cart-sauce-labs-onesie')
    remove_item_cta = (By.ID, 'remove-sauce-labs-onesie')
    item_title = (By.CSS_SELECTOR, 'a .inventory_item_name')
    item_description = (By.CSS_SELECTOR, '.cart_item_label .inventory_item_desc')
    item_quantity = (By.CSS_SELECTOR, '.cart_item .cart_quantity')

    add_to_cart_cta = (By.CSS_SELECTOR, '.product:nth-child(1) a.button')
    cart_item = (By.CSS_SELECTOR, '.cart_item')
    coupon_code_field = (By.ID, 'coupon_code')
    coupon_code_cta = (By.NAME, 'apply_coupon')
    coupon_code_confirmation_msg = (By.CSS_SELECTOR, '.woocommerce-message')
    checkout_cta = (By.CSS_SELECTOR, '.checkout-button')
    checkout_username = (By.ID, 'billing_first_name')
    checkout_country = (By.ID, 'billing_country')
    item_cart_name = (By.CSS_SELECTOR, '.product:nth-child(1) h2.woocommerce-loop-product__title')
    view_cart_cta = (By.CSS_SELECTOR, '.added_to_cart')
