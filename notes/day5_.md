## DAY-5

---

## Folder Structure
pages/
login_page.py
home_page.py

tests/
test_login_regression.py
test_login_parameterization.py
Test_login.py

config.py
conftest.py
pytest.ini

---

## Sample Fixture (conftest.py)

```python
import pytest
from selenium import webdriver
from utils.config import Configdata

data = Configdata()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.link)
    driver.maximize_window()
    yield driver
    driver.quit()