import unittest

from exceptions import HTTPRequestException
from utils import get_http_response

from matrix_finder import get_matrix


class TestMatrixFinder(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
        self.traversal = [
            10, 50, 90, 130,
            140, 150, 160, 120,
            80, 40, 30, 20,
            60, 100, 110, 70,
        ]

    async def test_get_matrix_positive_result(self):
        result = await get_matrix(self.url)
        self.assertEqual(result, self.traversal)

    async def test_get_matrix_negative_result(self):
        result = [1, 2, 3]
        self.assertFalse(result == self.traversal)

    async def test_get_http_response_negative(self):
        with self.assertRaises(HTTPRequestException) as context:
            await get_http_response('wrong-url')

        self.assertIn('Некорректно указан адрес', str(context.exception))
