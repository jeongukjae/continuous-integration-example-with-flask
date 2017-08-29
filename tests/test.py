import unittest
from app import create_app

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app = self.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert 'Sign In' in rv.data.decode('utf8')

    def test_login(self):
        rv = self.app.post('/auth/signin', data=dict(
            name='jeongukjae',
            email='jeongukjae@gmail.com'
        ), follow_redirects=True)

        assert 'You were logged in' in rv.data.decode('utf-8')

if __name__ == '__main__':
    unittest.main()