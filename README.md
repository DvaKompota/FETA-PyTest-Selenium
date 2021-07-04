# Pytest Front-end Test Automation Framework prototype 
<br/>

## Installation and running instructions:
#### 1. To install the framework on your local machine:
- clone the repo from GitHub
- open terminal in the local repo directory and run the following commands:<br/>
`pip3 install pytest PyYAML selenium`<br/>
`export PYTHONPATH=:.`<br/>
#### 2. To run tests
- to run all the tests in the repo run:<br/>
`pytest tests/`
- to run only tests for a specific feature add the filename to the command, e.g.:<br/>
`pytest tests/test_01_home_page.py`
- by default tests are running in headless browser mode; if you want to actually see the browser window, open `resources/test_data/data.yaml` file and change `web_driver_settings.headless` to `False`<br/>
<br/>

---
## Things to be added:
#### 1. A script file for the Client to trigger test runs without terminal commands
#### 2. A requirements.txt file to provide necessary documentation for the framework setup
#### 3. A Makefile to ease up the setup process within a pyenv
#### 4. Add 2 TCs for login:
- cart_contents_saved_in_account
- validate_order_history
#### 5. Add 2 TCs for shopping cart:
- add_product_to_cart_with_logged_in_customer
- change_quantity_and_delete_product_from_cart
#### 6. Add 7 TCs for checkout process:
- checkout_for_new_customer
- checkout_for_existing_customer
- validate_address_page_elements
- validate_shipping_page_elements
- validate_payment_page_elements
- validate_order_page_elements
- validate_confirmation_page_elements
#### 7. Jenkins file if the Client plans to use this test automation from a server
#### 8. Proper docstrings, in-line comments, and configuration documentation to provide easier transition for further development
