import unittest


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyzapi import main

        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_plain_without_name(self):
        res = self.testapp.get('/plain', status=200)
        self.assertIn(b'No Name Provided', res.body)

    def test_plain_with_name(self):
        res = self.testapp.get('/plain?name=Jane%20Doe', status=200)
        self.assertIn(b'Jane Doe', res.body)

    def test_identities_with_id(self):
        res = self.testapp.get('/identities/42', status=200)
        self.assertIn(b'id: 42', res.body)