import unittest
from app import create_app


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_user_can_register_successfully(self, email="app@test.com", password="apptest"):
        user_data = {'email': email, 'password': password}
        request = self.client().post(
            '/api/v1/register',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(user_data)
        )
        result = json.loads(request.data.decode())
        self.assertEqual(result['message'], 'successfully created user')
        self.assertEqual(result.status_code, 201)