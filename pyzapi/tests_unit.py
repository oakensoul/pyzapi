import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import PyzapiViews

        request = testing.DummyRequest()
        inst = PyzapiViews(request)
        response = inst.home()

        self.assertEqual('Home View', response['name'])

    def test_hello(self):
        from .views import PyzapiViews

        request = testing.DummyRequest()
        inst = PyzapiViews(request)
        response = inst.hello()

        self.assertEqual('Hello View', response['name'])
