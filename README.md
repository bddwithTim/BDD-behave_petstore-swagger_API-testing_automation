## Purpose
This repository is for learning and practice purposes on authoring Gherkin scenarios in a BDD behave project.
The sample scenarios covers API related tests from the sample server [Petstore server](https://petstore.swagger.io).

For more coverage, feel free to add other API tests using the sample server.

## Prerequisites
For both test authoring and execution:

* [Python 3.7+](https://www.python.org)
  Ensure that you have python installed in your system preferably Python 3.7 or higher.	
  
Only for automated test execution:

* [Chrome](https://www.google.com/chrome)
* [Chrome web driver for Selenium](https://sites.google.com/a/chromium.org/chromedriver/downloads),
  which needs to be in your [PATH](https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/) environment variable.
  Ensure that the Chrome web driver you download is compatible to the chrome browser you are using.
  To check the version of your chrome browser, input this url in your chrome browser `chrome://settings/help`.
  The version should be displayed on that page.

## Configuration
Configuration is contained in config.yaml. Here are the available options:

* `browser:` General browser settings.
  * `url:` String. Base URL.
  * `headless:` Boolean. Whether to run the browser in headless mode.
  * `size:` String. Window dimensions in format `width,height` (e.g., `1920,1080`).
  * `extensions:` Boolean. Whether to allow the use of installed extensions.
  * `gpu:` Boolean. Whether to enable GPU acceleration.

You can also create a file named config.override.yaml to selectively override
a subset of the defaults without directly changing config.yaml, which is useful
when you want to avoid Git picking up those changes. Example override file:

```yaml
browser:
  headless: false
```

## Development
Prerequisites:

* [Poetry 1.0.0+](https://github.com/python-poetry/poetry)
  * Windows: `pip install poetry`
  * Linux/Mac: `pip3 install --user poetry`

After cloning, prepare your development environment like so:

* Set the virtual environment in your project locally: `poetry config virtualenvs.in-project true --local`
* Set up the Python virtual environment: `poetry install`
* Activate the pre-commit hooks: `poetry run pre-commit install`


## Test Execution
Test Execution commands:

* Run all scenarios: `poetry run behave`
* Running tag specific scenarios: `poetry run behave features --tags ~wip --tags @positive`
* Verify scenario syntax without actually running the tests: `poetry run behave --dry-run`




