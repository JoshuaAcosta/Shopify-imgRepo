"""Test suite """
import requests

class TestClass(object):

    def test_main_page(self):
        """Checks status code and response text in mainpage """
        response = requests.get('http://localhost:5000/')
        assert response.status_code == 200
        assert "Welcome to imgRepo" in response.text

    def test_registration_page(self):
        """Checks status code and response text in registration page """
        response = requests.get('http://localhost:5000/register')
        assert response.status_code == 200
        assert "Register to begin uploading images" in response.text

    def test_login_page(self):
        """Checks status code and response text in login page """
        response = requests.get('http://localhost:5000/login')
        assert response.status_code == 200
        assert "Login to view your images" in response.text

    def test_user_registration_proper_login(self):
        formdata = {'first_name': 'Joshua', 'last_name': 'Acosta', 'email': "testemail@gmail.com", "passphrase":"TestPassword123456!"}
        response = requests.post('http://localhost:5000/register', params=formdata)
        assert response.status_code == 200
