# Следует протестировать основные функции по получению информации о документах,
# добавлении и удалении элементов из словаря.
import unittest
from app import get_doc_owner_name, delete_doc, get_doc_shelf, add_new_doc, add_new_shelf


class TestFunc(unittest.TestCase):

    def setUp(self):
        print("===> setUp")

    def tearDown(self):
        print("===> tearDown")

    def test_add_new_doc(self):
        """Это метод тестирования функции добавления этиментов в словарь"""
        result = add_new_doc()
        etalon = '3'
        self.assertEqual(result, etalon)

    def test_delete_doc(self):
        """Это метод тестирования функции удаления элементов из словарь"""
        result = delete_doc()
        etalon = ('11-2', True)
        self.assertEqual(result, etalon)

    def test_get_doc_shelf(self):
        """Это метод тестирования функции для получения информации из словаря"""
        result = get_doc_shelf()
        etalon_3 = '1'
        self.assertEqual(result, etalon_3)

    def test_get_doc_owner_name(self):
        """Это метод тестирования функции для получения информации из словаря"""
        result = get_doc_owner_name()
        etalon = 'Аристарх Павлов'
        self.assertEqual(result, etalon)

    def test_add_new_shelf(self):
        """Это метод тестирования функции добавления этиментов в словарь directories"""
        result = add_new_shelf()
        etalon = ('4', True)
        self.assertEqual(result, etalon)

    def test_false_add_new_shelf(self):
        """Это метод тестирования функции добавления этиментов в словарь directories"""
        result = add_new_shelf()
        etalon = ('4', False)
        self.assertEqual(result, etalon)


if __name__ == '__main__':
    unittest.main()
