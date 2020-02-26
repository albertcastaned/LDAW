import os
import unittest

from app import app

class TestCase(unittest.TestCase):
    def test_prueba(self):
        assert 1 == 1

if __name__ == '__main__':
    unittest.main()
    