# project/test_basic.py

import os
import unittest
from app import app


class BasicTests(unittest.TestCase):

    def test_main_page(self):
        web = app.test_client()

        rv = web.get('/')
        assert rv.status == '200 OK'
        assert rv.data == b'Hello World!'

    if __name__ == "__main__":
        unittest.main()
