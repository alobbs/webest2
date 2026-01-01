import time
import atexit
import contextlib

from selenium.common.exceptions import WebDriverException

from . import initializer
from . import screenshot
from . import exceptions
from .obj import *

DEFAULT_BROWSER = 'firefox'


def cleanup():
    if not initializer.is_init_done():
        return
    initializer.cleanup()


def init(browser_name=DEFAULT_BROWSER, reuse=False, **kwargs):
    """
    Initialize browser with one retry attempt if WebDriverException occurs.
    
    Args:
        browser_name: Browser to use (defaults to DEFAULT_BROWSER)
        reuse: Whether to reuse existing browser instance
        **kwargs: Additional arguments to pass to initializer
    """
    if not initializer.is_init_done():
        try:
            initializer.do(browser_name, reuse, **kwargs)
        except WebDriverException as e:
            # Log the exception (optional)
            print(f"WebDriverException occurred: {e}. Retrying in 2 seconds...")
            
            # Wait before retrying
            time.sleep(2)
            
            # Final attempt
            initializer.do(browser_name, reuse, **kwargs)

    atexit.register(cleanup)


@contextlib.contextmanager
def init_context(reuse=False, *args, **kwargs):
    init(*args, **kwargs)
    yield
    if not reuse:
        cleanup()


def load(url, browser=None):
    if not browser:
        browser = initializer.browser()

    # Fix URL?
    if not any(url.startswith(s) for s in ('https://', 'http://')):
        url = f"https://{url}"

    # Load URL
    browser.get(url)


def get_title():
    browser = initializer.browser()
    return browser.title


def set_window_size(*args):
    browser = initializer.browser()
    browser.set_window_size(*args)
