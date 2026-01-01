import selenium
from selenium.common.exceptions import *


def is_retry_exception(exception):
    allowed_exceptions = (
        selenium.common.exceptions.UnexpectedAlertPresentException,
        selenium.common.exceptions.WebDriverException
    )
    return any(isinstance(exception, e) for e in allowed_exceptions)
