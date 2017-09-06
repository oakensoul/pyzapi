import unittest


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyzapi import main
        app = main({})
        from webtest import TestApp

        self.test_app = TestApp(app)

    def test_home(self):
        res = self.test_app.get('/', status=200)
        self.assertIn(b'<body>Visit', res.body)

    def test_hello(self):
        res = self.test_app.get('/howdy', status=200)
        self.assertIn(b'<body>Go back', res.body)
