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
        self.assertEqual(response.status, '302 Found')

    def test_plain_without_name(self):
        from .views import PyzapiViews

        request = testing.DummyRequest()
        inst = PyzapiViews(request)
        response = inst.plain()
        self.assertIn(b'No Name Provided', response.body)

    def test_plain_with_name(self):
        from .views import PyzapiViews

        request = testing.DummyRequest()
        request.GET['name'] = 'Jane Doe'
        inst = PyzapiViews(request)
        response = inst.plain()
        self.assertIn(b'Jane Doe', response.body)

    def test_identities_with_id(self):
        from .views import PyzapiViews

        request = testing.DummyRequest()
        request.matchdict['identity'] = 42

        inst = PyzapiViews(request)
        response = inst.identities()
        self.assertIn(b'id: 42', response.body)
