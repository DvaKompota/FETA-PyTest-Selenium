# Theorem Job Interview Prototype Task
<br/>

## Things to be added ASAP:
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
<br/>

---
## Things to be clarified with the Client:
#### 1. General Priorities: wider and deeper coverage or better usability and reporting?
- Broader coverage: more test cases per feature; more validations per test case, etc., or
- Better usability of the test framework: easy to read test cases (e.g. in Gherkin); easy to manage test data; easy to read reporting of test executions, etc.?
#### 2. Headers, footers, contacts, links (some lead to Prestashop), product cards and quick-view, prices are not mentioned in the task description - if they are to be tested, there should be additional TCs written for that
#### 3. Requirements and acceptance criteria for specific tests:
- Account creation: functional only or input validations are required? e.g. not allowing special chars, or password requirements. AC?
- Browsing: should breadcrums and left navigation panel be tested? what is the most important way of browsing? AC?
- Searching: search field has an autocomplete - should it be tested itself? search page has an extensive navigation panel - should it be tested itself? AC?
- Sharing via social media: should product card links (require social media platforms login) be tested and if yes - to what extent? AC?
- Shoping cart: should numbers and math be validated or this is managed by back-end testing? Address validation shown in the cart?
- Checkout: any special acceptance criteria for addresses and shipping? no CC payment? What is the AC: success screen? order shown in Order history? Invoice PDF attached/downloadable/has proper content?
