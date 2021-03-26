from django.test import TestCase
from unittest.mock import patch
from instagramProfile.services import InstagramScraperService
from instagramProfile.logic import InstagramScraperLogic
from mock import Mock

class instagramProfileTestCase(TestCase):

    @patch('instaloader.Instaloader')
    def test_loginShouldReturnOkIfParamsAreCorrect(self, instaloader_Instaloader_mock):
        
        user_login = 'magnus_carlsen'
        password_login = 'e5Ac5Cf3O-O'

        def login(a, b):
            pass

        mock = Mock()
        login_attribute = {"login": login}
        mock.configure_mock(**login_attribute)

        instaloader_Instaloader_mock.return_value = mock
        response = InstagramScraperService.login(user_login, password_login)
        self.assertEquals(response, mock)

    @patch('instaloader.Profile')
    def test_get_instagram_profilesShouldReturnOkIfParamsAreCorrect(self, instaloader_Profile_mock):

        user_name = 'thenotoriousmma'
        scraper = Mock()

        def get_posts():
            return 'posts'

        mock = Mock()
        get_posts_attribute = {"get_posts": get_posts}
        mock.configure_mock(**get_posts_attribute)


        instaloader_Profile_mock.from_username.return_value = mock
        response = InstagramScraperService.get_instagram_profiles(user_name, scraper)
        self.assertEquals(response[0], mock)
        self.assertEquals(response[1], 'posts')
