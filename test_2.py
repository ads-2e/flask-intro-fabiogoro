from flask_test import AbstractViewCase
import unittest

class TestEntrarView(AbstractViewCase, unittest.TestCase):

    _url = '/entrar/'
    _template = 'entrar.html'
