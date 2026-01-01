from enum import Enum
import logging
from selenium import webdriver

globals = dict(init_done = False)


def _init_firefox(path_geckodriver=None, headless=True):
    global globals

    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options    

    # Firefox setup
    firefox_options = Options()
    if headless:
        firefox_options.add_argument("--headless")

    firefox_service = Service(path_geckodriver)
    firefox_driver = webdriver.Firefox(service=firefox_service,
                                       options=firefox_options)

    logging.info(f"Instanced Firefox: {firefox_driver}")
    globals['browser_name'] = 'firefox'
    globals['service_mod'] = Service
    globals['service_obj'] = firefox_service
    globals['options'] = firefox_options
    globals['driver'] = firefox_driver


def _init_chrome(headless=True):
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--start-minimized")
    chrome_driver = webdriver.Chrome(options=chrome_options)

    logging.info(f"Instanced Chrome: {chrome_driver}")
    globals['browser_name'] = 'chrome'
    globals['driver'] = chrome_driver
    globals['options'] = chrome_options


def do(browser_name: str, reuse: bool, **kwargs):
    global globals
    if globals['init_done']:
        return

    if reuse and globals.get('driver') is not None:
        return

    browser_l = browser_name.lower()

    if browser_l == "firefox":
        _init_firefox(**kwargs)
    elif browser_l in ("chrome", "chromium"):
        _init_chrome(**kwargs)
    else:
        assert False, f"Unsupported browser: `{browser_name}`"

    logging.info (f"Browser ({browser_l}) initialized")
    globals['init_done'] = True


def is_init_done():
    return globals.get('init_done', False)


def browser():
    return globals.get('driver')


def cleanup():
    global globals

    # Quick browser
    if (b := browser()):
        logging.info (f"Quitting browser ({b})")        
        b.quit()

    # Globals
    for k in set(globals.keys()):
        del(globals[k])

    globals['init_done'] = False
