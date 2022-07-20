# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

import unittest
from yandex_main import create_yandex_folder


class TestFunc(unittest.TestCase):
    def setUp(self):
        print("===> setUp")

    def tearDown(self):
        print("===> tearDown")

    def test_success_create_yandex_folder(self):
        result = create_yandex_folder('https://cloud-api.yandex.net/v1/disk/resources', 'yandex_test_5')
        etalon = 201
        self.assertEqual(result, etalon)

    def test_passed_create_yandex_folder(self):
        result = create_yandex_folder('https://cloud-api.yandex.net/v1/disk/resources', 'yandex_test_3')
        etalon = 409
        self.assertEqual(result, etalon)


if __name__ == '__main__':
    unittest.main()