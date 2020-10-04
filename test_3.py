from flask_test import AbstractViewCase
import unittest

class TestInscricaoView(AbstractViewCase, unittest.TestCase):

    _url = '/inscrever/'
    _template = 'inscrever.html'
