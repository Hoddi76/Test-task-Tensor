from selenium.webdriver.common.by import By


class HomePageYandexLockators(object):

    SEARCH_FIELD                = By.CLASS_NAME, 'search2'
    SEARCH_FIELD_IN_FOR_TEXT    = By.ID, 'text'
    SUGGEST                     = By.CLASS_NAME, 'suggest2'
    LINK_PICTURES               = By.LINK_TEXT, 'Картинки'


class ResultPageLockators(object):

    FIRST_LINK_YANDEX           = By.CLASS_NAME, 'organic__subtitle'


class ImagePageLockators(object):

    FIRST_IMAGE                 = By.CLASS_NAME, 'cl-teaser__link'
    NEXT_IMAGE_BUTTON           = By.CLASS_NAME, 'layout__nav__right'
    BACK_IMAGE_BUTTON           = By.CLASS_NAME, 'layout__nav__left'
    IMAGE_SRC                   = By.CLASS_NAME, 'image__image'
    CHECK_OPEN_IMAGE            = By.CLASS_NAME, 'image_layout'
