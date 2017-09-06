import unittest


class TutorialFunctionalTests(unittest.TestCase):
    def __init__(self):
        self.testapp = None

    def setUp(self):
        from pyzapi import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_hello_world(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hello Rob!</h1>', res.body)