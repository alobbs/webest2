import selenium
from selenium.common.exceptions import *
import urllib3


def is_retry_exception(exception):
    allowed_exceptions = (
        selenium.common.exceptions.UnexpectedAlertPresentException,
        selenium.common.exceptions.WebDriverException,
        urllib3.exceptions.ReadTimeoutError
    )
    return any(isinstance(exception, e) for e in allowed_exceptions)
