from flask_test import AbstractViewCase
import unittest

class TestHomeView(AbstractViewCase, unittest.TestCase):

    _url = '/'
    _template = 'index.html'
