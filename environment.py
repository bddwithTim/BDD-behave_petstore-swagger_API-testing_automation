import time
import re

from pathlib import Path
from behave.model import Scenario

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from petstore_swagger_bdd import get_config
from petstore_swagger_bdd.browser import chrome_options
from petstore_swagger_bdd.context import PetStoreContext



def before_all(context: PetStoreContext):
    data = get_config()
    context.driver = webdriver.Chrome(
        chrome_options=chrome_options()
    )
    context.base_url = data["browser"]["url"]
    context.wait = WebDriverWait(context.driver, 20)


def after_all(context: PetStoreContext):
    context.driver.quit()

def before_scenario(context: PetStoreContext, scenario: Scenario):
    context.scenario_start_time = time.time()


def after_scenario(context: PetStoreContext, scenario: Scenario):
    if scenario.status == "failed":
        scenario_error_dir = Path("logs")
        scenario_error_dir.mkdir(exist_ok=True)
        base_name = time.strftime("%Y-%m-%d_%H%M%S_{}".format(re.sub(r'[/\\:*?"<>#]', "", scenario.name)[:60]))
        log_file_path = scenario_error_dir / "{}.txt".format(base_name)
        for step in scenario.steps:
            if step.status in ["failed", "undefined"]:
                log_file_path.write_text(
                    "Scenario: {}\nStep: {} {}\nError Message: {}".format(
                        scenario.name, step.keyword, step.name, step.error_message
                    )
                )
                break
        else:
            log_file_path.write_text("Scenario: {}\nStep: N/A".format(scenario.name))
