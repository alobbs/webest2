import time

from . import initializer

import selenium.common.exceptions


def save(fp_save, browser=None):        
    if not browser:
        browser = initializer.browser()

    ok  = False
    for _ in range(3):
        try:
            browser.get_screenshot_as_file(fp_save)
            ok = True
            break
        except selenium.common.exceptions.WebDriverException:
            time.sleep(2)

    return not ok



# import PIL.Image
    # crop = kwargs.pop('crop', None)

    # with browser.new_auto(url, **kwargs) as b:
    #     b.get_screenshot_as_file(fp)

    # if crop:
    #     assert(type(crop) == tuple)
    #     img = PIL.Image.open(fp)
    #     img_cropped = img.crop(crop)
    #     img_cropped.save(fp)