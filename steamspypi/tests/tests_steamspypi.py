import time
import unittest

import steamspypi


class TestSteamSpyPiMethods(unittest.TestCase):

    def test_download_all(self):
        data_request = dict()
        data_request['request'] = 'all'
        data_request['page'] = '0'

        data = steamspypi.download(data_request)

        print('[Steam catalog] #games = {}'.format(len(data)))

        self.assertGreater(len(data), 0)

    def test_download_appdetails(self, appid=730):
        data_request = dict()
        data_request['request'] = 'appdetails'
        data_request['appid'] = str(appid)

        data = steamspypi.download(data_request)

        print('[appID = {}] game name = {}'.format(appid, data['name']))

        expected_game_name = 'Counter-Strike: Global Offensive'

        self.assertEqual(expected_game_name, data['name'])

    def test_download_genre(self, genre='Early Access'):
        data_request = dict()
        data_request['request'] = 'genre'
        data_request['genre'] = genre

        data = steamspypi.download(data_request)

        print('[genre = {}] #games = {}'.format(genre, len(data)))

        self.assertGreater(len(data), 0)

    def test_download_tag(self, tag='Early Access'):
        data_request = dict()
        data_request['request'] = 'tag'
        data_request['tag'] = tag

        data = steamspypi.download(data_request)

        print('[tag = {}] #games = {}'.format(tag, len(data)))

        self.assertGreater(len(data), 0)

    def test_download_top100in2weeks(self):
        data_request = dict()
        data_request['request'] = 'top100in2weeks'

        data = steamspypi.download(data_request)

        print('[request = {}] #games = {}'.format(data_request['request'], len(data)))

        self.assertGreater(len(data), 0)

    def test_download_top100forever(self):
        data_request = dict()
        data_request['request'] = 'top100forever'

        data = steamspypi.download(data_request)

        print('[request = {}] #games = {}'.format(data_request['request'], len(data)))

        self.assertGreater(len(data), 0)

    def test_download_top100owned(self):
        data_request = dict()
        data_request['request'] = 'top100owned'

        data = steamspypi.download(data_request)

        print('[request = {}] #games = {}'.format(data_request['request'], len(data)))

        self.assertGreater(len(data), 0)

    def test_load(self):
        # Because of rate-limits, try to ensure that test_download_all() was called at least 1 minute ago:
        cooldown_duration = 70  # 1 minute plus cushion
        time.sleep(cooldown_duration)
        # Download
        self.assertTrue(steamspypi.load())
        # Load from cache
        self.assertTrue(steamspypi.load())

    def test_check_wrong_request_field(self):
        data_request = dict()
        data_request['Hello, world!'] = 'appdetails'

        self.assertFalse(steamspypi.check_request(data_request))

    def test_check_wrong_request_value(self):
        data_request = dict()
        data_request['request'] = 'Hello, world!'

        self.assertFalse(steamspypi.check_request(data_request))

    def test_check_incomplete_request(self):
        data_request = dict()
        data_request['request'] = 'appdetails'

        self.assertFalse(steamspypi.check_request(data_request))

    def test_check_missing_main_request(self):
        data_request = dict()
        data_request['appid'] = '730'

        self.assertFalse(steamspypi.check_request(data_request))

    def test_cancel_download(self):
        data_request = dict()
        data_request['request'] = 'Hello, world!'

        self.assertEqual(len(steamspypi.download(data_request)), 0)

    def test_get_example_api_parameters(self):
        example_api_parameters = steamspypi.get_example_api_parameters()
        self.assertTrue(all([request in example_api_parameters for request in ['request', 'appid', 'genre', 'tag', 'page']]))

    def test_print_data(self):
        data_request = dict()
        data_request['request'] = 'appdetails'
        data_request['appid'] = '573170'

        data = steamspypi.download(data_request)

        self.assertTrue(steamspypi.print_data(data))


if __name__ == '__main__':
    unittest.main()
