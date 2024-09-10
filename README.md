#  Project

### Chitai_Gorod (https://www.chitai-gorod.ru/)

## Description

This project is designed for testing the functionality of finding books in the search box, using filters,
check for error messages. The project uses Selenium WebDriver for browser automation and `pytest` for writing and
executing test cases. The testing is done on the Google Chrome browser.

## Development Environment

- ***IDE:*** PyCharm Community Edition 2024.2
- ***Python Version:*** 3.12
- ***Test Framework:*** `pytest==8.2.2`
- ***Web Driver:*** Google ChromeDriver
- ***Browser Version:*** Google Chrome 128

## Frameworks

- ***selenium***
- ***pytest***
- ***requests***
- ***allure***

## Installing Libraries

```
pip install selenium
```
---
```
pip install pytest
```
---

```
pip install allure-pytest
```
---

```
pip install allure-python-commons
```
---

```
pip install requests
```

---

## Project Structure

The project is organized as follows:

### 1. `constants.py`

This file contains constants used throughout the project such as:

- Main url to connect on the website

```python
BASE_URL = "https://www.chitai-gorod.ru/"
```
---

- Main url to send requests on the backend
```python
API_URL = "https://web-gate.chitai-gorod.ru/api/"
```
---
- Authorization token to get access to backend
```python
API_KEY = {
    'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
                      'eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjg'
                      '2NjAxMDksImlhdCI6MTcyNTgyNTQzOSwiZXhwIjoxNzI1ODI5MD'
                      'M5LCJ0eXBlIjoyMH0.yR3gupbRENxGwgOlIs6r9IlUqLAXFmwu5HvEwUxpKhM'
}
```

### 2. `pages_api/ApiCollection.py`

This file contains a class with methods to interact with api requests.

### 3. `pages_ui/MainPage.py`

This file includes methods for writing text, clicking on items (with or without actions),
and retrieving text information

### 4. `tests/test_api.py`

This file contains the actual test cases that use the methods from the `pages_api` directory to perform
automated testing on the backend. It utilizes the fixtures defined in `conftest.py` to manage
the ApiCollection instance.

### 5. `tests/test_ui.py`

This file contains the actual test cases that use the methods from the `pages_ui` directory to perform
automated testing on the website. It utilizes the fixtures defined in `conftest.py` to manage the WebDriver and 
MainPage instances.

### 6. `test/conftest.py`

This file is used to define shared fixtures and setup code for the `pytest` framework. In this project, it contains 
the configuration for the:
- Chrome WebDriver:

```python
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()
```

- MainPage.py: 

```python
@pytest.fixture
def main_page(browser):
    main_page = MainPage(browser)
    return main_page
```
- ApiCollection.py: 

```python
@pytest.fixture
def api():
    api = ApiCollection()
    return api
```


## Dependencies and Imports

This project relies on Selenium WebDriver for browser automation.
Below are the specific imports used within the project:

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import Severity
import allure
import pytest
import requests


```

## Setup Instructions


### 1. Clone the repository to your local machine:

```
git clone https://github.com/Mrnobody231/City_Read_SkyPro.git>
```

### 2. Navigate to the project directory:

```
cd <project-directory>
```

### 3. Install all required dependencies, use the following command:

```
pip install -r requirements.txt
```

### 4. Run the test cases using pytest:

```
pytest
```
### 5. Run the test cases using pytest to get more information:

```
pytest -v
```

## Warnings

The API access token is temporary and works for approximately 20 minutes. To obtain a new token, a person must be
authorized on the website (https://www.chitai-gorod.ru/). Using DevTools/Network, find the authorization field in the
response headers. Copy its value and replace it in `constants.py` under `API_KEY`.