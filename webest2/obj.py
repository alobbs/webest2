import retrying
import selenium
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By

from . import exceptions as ex
from . import initializer


@retrying.retry(wait_fixed=1000, retry_on_exception=ex.is_retry_exception)
def get_obj(selector, not_found=None, browser=None):
    if not browser:
        browser = initializer.browser()

    try:
        obj = browser.find_element(By.CSS_SELECTOR, selector)
    except selenium.common.exceptions.NoSuchElementException:
        return not_found
    return obj


@retrying.retry(wait_fixed=1000, retry_on_exception=ex.is_retry_exception)
def get_objs(selector, not_found=None, browser=None):
    if not browser:
        browser = initializer.browser()

    try:
        objs = browser.find_elements(By.CSS_SELECTOR, selector)
    except selenium.common.exceptions.NoSuchElementException:
        return not_found
    return objs


@retrying.retry(wait_fixed=1000, retry_on_exception=ex.is_retry_exception)
def is_visible(selector, browser=None):
    if not browser:
        browser = initializer.browser()

    try:
        obj = browser.find_element(By.CSS_SELECTOR, selector)
    except selenium.common.exceptions.NoSuchElementException:
        return False
    return obj.is_displayed()


@retrying.retry(wait_fixed=1000, retry_on_exception=ex.is_retry_exception)
def is_enabled(selector, browser=None):
    if not browser:
        browser = initializer.browser()

    try:
        obj = browser.find_element(By.CSS_SELECTOR, selector)
    except selenium.common.exceptions.NoSuchElementException:
        return False
    return obj.is_enabled()


def get_text(selector, not_found=None, browser=None):
    if not browser:
        browser = initializer.browser()

    obj = get_obj(selector, not_found=not_found, browser=browser)
    if obj:
        return obj.text
    return not_found


def obj_attr(selector, attr, not_found=None, browser=None):
    if not browser:
        browser = initializer.browser()

    obj = get_obj(selector, not_found=not_found, browser=browser)
    if obj:
        re = obj.get_attribute(attr)
        if re is None:
            return not_found
        return re
    return not_found


def wait_for_obj(selector, timeout=30, browser=None):
    if not browser:
        browser = initializer.browser()

    wait = ui.WebDriverWait(b, timeout)
    wait.until(lambda driver, s=selector: get_obj(s, browser=browser))
    return get_obj(selector, browser=browser)


def wait_for_any_obj(selectors, timeout=30, browser=None):
    def check_func(b):
        return any([get_obj(s, browser=browser) for s in selectors])

    if not browser:
        browser = initializer.browser()

    wait = ui.WebDriverWait(browser, timeout)
    wait.until(check_func)

    for s in selectors:
        obj = get_obj(s, browser=browser)
        if obj:
            return obj
        

def wait_while_obj(selector, timeout=30, browser=None):
    if not browser:
        browser = initializer.browser()

    wait = ui.WebDriverWait(b, timeout)
    wait.until(lambda driver, s=selector: not get_obj(s, browser=browser))
    return get_obj(selector, browser=browser)


def wait_while_visible(selector, timeout=30, browser=None):
    if not browser:
        browser = initializer.browser()

    wait = ui.WebDriverWait(browser, timeout)
    wait.until(lambda driver, s=selector: not get_obj(s, browser=browser))
    return get_obj(selector, browser=browser)


def wait_while_hiden(selector, timeout=30, browser=None):
    if not browser:
        browser = initializer.browser()

    wait = ui.WebDriverWait(browser, timeout)
    wait.until(lambda driver, s=selector: get_obj(s, browser=browser))
    return get_obj(selector, browser=browser)
