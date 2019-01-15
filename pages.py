from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from locators import *


class HomePageYandex(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = HomePageYandexLockators

    def check_presence_search_field(self):
        try:
            self.driver.find_element(*self.locator.SEARCH_FIELD)
        except NoSuchElementException as e:
            print(e.msg)
            return False
        return True

    def put_in_search(self, item):
        """
        :param item: Фраза которую вбиваем в поиск
        """
        search_field = self.driver.find_element(*self.locator.SEARCH_FIELD_IN_FOR_TEXT)
        return search_field.send_keys(item)

    def check_suggest_in_page(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.locator.SUGGEST),
                message='Таблица с подсказками не появилась (suggest)')
        except TimeoutException as e:
            print(e.msg)
            return False
        return True

    def click_on_enter(self):
        self.driver.find_element(*self.locator.SEARCH_FIELD_IN_FOR_TEXT).send_keys(Keys.ENTER)
        return ResultPage(self.driver)

    def click_link_pictures(self):
        self.driver.find_element(*self.locator.LINK_PICTURES).click()
        return YandexImagePage(self.driver)


class ResultPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = ResultPageLockators

    def first_link(self):
        return self.driver.find_element(*self.locator.FIRST_LINK_YANDEX).text


class YandexImagePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = ImagePageLockators

    def open_first_image(self):
        image = self.driver.find_element(*self.locator.FIRST_IMAGE)
        hover = ActionChains(self.driver).move_to_element(image).pause(0.5)
        hover.click(image)
        hover.perform()

    def check_open_image(self):
        try:
            self.driver.find_element(*self.locator.CHECK_OPEN_IMAGE)
        except NoSuchElementException as e:
            #print(e.msg)
            return False
        return True

    def image_src(self):
        return self.driver.find_element(*self.locator.IMAGE_SRC).get_attribute("src")

    def click_next_image_button(self):
        return self.driver.find_element(*self.locator.NEXT_IMAGE_BUTTON).click()

    def click_back_image_button(self):
        return self.driver.find_element(*self.locator.BACK_IMAGE_BUTTON).click()
