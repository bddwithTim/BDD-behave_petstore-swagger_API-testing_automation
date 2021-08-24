from selenium.webdriver.chrome.options import Options as ChromeOptions
from petstore_swagger_bdd import get_config


def chrome_options():
    _chrome_options = ChromeOptions()
    config = get_config()

    extensions = config["browser"]["extensions"],
    gpu = config["browser"]["gpu"],
    headless = config["browser"]["headless"]
    window_size = config["browser"]["size"]

    if not extensions:
        _chrome_options.add_argument("--disable-extensions")
    if not gpu:
        _chrome_options.add_argument("--disable-gpu")
    if window_size:
        _chrome_options.add_argument("--window-size={}".format(window_size))
    if headless:
        _chrome_options.add_argument("--headless")
        _chrome_options.add_argument("--load-images=no")
        _chrome_options.add_argument("--window-position=1,0")
        # driver.manage().window().maximize() doesn't work
        # in headless mode. Therefore setting the window size directly.
        # sample sizes: 1024x768, 1920x1080
        if not window_size:
            _chrome_options.add_argument("--window-size=1200,1100")
    else:
        if not window_size:
            _chrome_options.add_argument("--start-maximized")
        _chrome_options.add_argument("--disable-infobars")

    return _chrome_options
