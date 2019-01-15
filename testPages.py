import unittest
from selenium import webdriver
from pages import *


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://yandex.ru/')

    def testSearchYandex(self):
        home_page = HomePageYandex(self.driver)
        self.assertTrue(home_page.check_presence_search_field(), msg='Поля "поиск" нет на странице')
        home_page.put_in_search("Тензор")
        home_page.check_suggest_in_page()  # self.assertTrue(home_page.check_suggest_in_page())
        result_page = home_page.click_on_enter()
        self.assertIn('tensor.ru', result_page.first_link(), msg='Первая ссылка не ведет на сайт tenzor.ru')

    def testPicturesOnYandex(self):
        home_page = HomePageYandex(self.driver)
        image_page = home_page.click_link_pictures()
        image_page.open_first_image()
        self.assertTrue(image_page.check_open_image(), msg='Картинка не открылась')
        src_first_image = image_page.image_src()
        image_page.click_next_image_button()
        image_page.click_back_image_button()
        src_result_image = image_page.image_src()
        self.assertEqual(src_first_image, src_result_image)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
