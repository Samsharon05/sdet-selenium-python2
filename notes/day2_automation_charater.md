
##  Smoke Tests

| ID | Title | Type | Priority | Description | Reason |
|----|------|------|----------|-------------|--------|
| TC_001 | Verify login with valid credentials | UI | High | User logs in with valid credentials and is redirected to the home page | Ensures user can successfully access the application |
| TC_002 | Verify login with invalid credentials | UI | High | User logs in with invalid credentials and an error message is displayed | Ensures proper validation and prevents unauthorized access |
| TC_003 | Verify user can add items to cart | UI | High | User adds items to the cart and cart is updated successfully | Ensures core add-to-cart functionality |
| TC_004 | Verify user can remove items from cart | UI | High | User removes a product from the cart and cart is updated accordingly | Ensures proper cart management |
| TC_005 | Verify navigation to checkout page | UI | High | User clicks on checkout and is redirected to checkout page with selected products | Ensures correct checkout navigation |
| TC_006 | Verify successful order placement | UI | High | User places the order and order confirmation is displayed | Ensures end-to-end purchase flow works correctly |

---

## Regression Tests

| ID | Title | Type | Priority | Description | Reason |
|----|------|------|----------|-------------|--------|
| TC_007 | Verify product opens on clicking image | UI | Medium | User clicks on product image and is redirected to product detail page | Ensures correct product navigation |
| TC_008 | Verify product opens on clicking name | UI | Medium | User clicks on product name and is redirected to the correct product detail page | Ensures correct product mapping |
| TC_009 | Verify correct cart items are displayed | UI | High | Products added to cart are displayed with correct details | Ensures cart accuracy |
| TC_010 | Verify checkout button is clickable | UI | Medium | Checkout button is visible and clickable on cart page | Ensures usability of checkout flow |
| TC_011 | Verify product data consistency after refresh | UI | Medium | Product details remain unchanged after page refresh | Ensures data consistency |
| TC_012 | Verify add to cart works for all products | UI | High | User is able to add multiple products to cart successfully | Ensures consistent functionality |
| TC_013 | Verify add to cart button state change | UI | Medium | Add to cart button changes to "Remove" after clicking | Ensures correct UI feedback |
| TC_014 | Verify sorting by name (Z-A) | UI | Medium | Products are sorted in descending alphabetical order | Ensures sorting functionality |
| TC_015 | Verify sorting by price (low to high) | UI | Medium | Products are sorted in ascending order based on price | Ensures correct sorting logic |
| TC_016 | Verify login with empty credentials | UI | High | User attempts login without entering credentials and validation message is displayed | Ensures mandatory field validation |
| TC_017 | Verify cart count updates correctly | UI | Medium | Cart icon count updates when items are added or removed | Ensures accurate cart tracking |
| TC_018 | Verify continue shopping from cart | UI | Medium | User clicks "Continue Shopping" and is redirected to product page | Ensures smooth navigation |
| TC_019 | Validate login API response status | API | Medium | Login API returns correct status for valid and invalid credentials | Enables faster backend validation |
| TC_020 | Verify user logout functionality | UI | Medium | User logs out and is redirected to login page | Ensures session termination and security |

---