import requests

from typing import Optional
from behave.runner import Context

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class PetStoreContext(Context):
    """Dummy type used for assistance with static analysis."""

    driver: WebDriver
    wait: WebDriverWait
    http_response: Optional[requests.Response]
    pet_store_object: Optional[dict]
    scenario_start_time: float
