import unittest

import steamspypi


class TestDownloadMethods(unittest.TestCase):
    def test_get_api_url(self):
        api_url = steamspypi.get_api_url()
        self.assertEqual(api_url, "https://steamspy.com")

    def test_get_api_endpoint(self):
        api_endpoint = steamspypi.get_api_endpoint()
        self.assertEqual(api_endpoint, "/api.php")

    def test_get_default_data_request(self):
        data_request = steamspypi.get_default_data_request()
        self.assertDictEqual(data_request, {"request": "all", "page": "0"})

    def test_download_all(self):
        data_request = dict()
        data_request["request"] = "all"
        data_request["page"] = "0"

        data = steamspypi.download(data_request)

        print("[Steam catalog] #games = {}".format(len(data)))

        self.assertGreater(len(data), 0)

    def test_download_appdetails(self, appid=730):
        data_request = dict()
        data_request["request"] = "appdetails"
        data_request["appid"] = str(appid)

        data = steamspypi.download(data_request)

        print("[appID = {}] game name = {}".format(appid, data["name"]))

        expected_game_name = "Counter-Strike: Global Offensive"

        self.assertEqual(expected_game_name, data["name"])

    def test_download_genre(self, genre="Early Access"):
        data_request = dict()
        data_request["request"] = "genre"
        data_request["genre"] = genre

        data = steamspypi.download(data_request)

        print("[genre = {}] #games = {}".format(genre, len(data)))

        self.assertGreater(len(data), 0)

    def test_download_tag(self, tag="Early Access"):
        data_request = dict()
        data_request["request"] = "tag"
        data_request["tag"] = tag

        data = steamspypi.download(data_request)

        print("[tag = {}] #games = {}".format(tag, len(data)))

        self.assertGreater(len(data), 0)

    def test_download_top100in2weeks(self):
        data_request = dict()
        data_request["request"] = "top100in2weeks"

        data = steamspypi.download(data_request)

        print("[request = {}] #games = {}".format(data_request["request"], len(data)))

        self.assertGreater(len(data), 0)

    def test_download_top100forever(self):
        data_request = dict()
        data_request["request"] = "top100forever"

        data = steamspypi.download(data_request)

        print("[request = {}] #games = {}".format(data_request["request"], len(data)))

        self.assertGreater(len(data), 0)

    def test_download_top100owned(self):
        data_request = dict()
        data_request["request"] = "top100owned"

        data = steamspypi.download(data_request)

        print("[request = {}] #games = {}".format(data_request["request"], len(data)))

        self.assertGreater(len(data), 0)

    def test_cancel_download(self):
        data_request = dict()
        data_request["request"] = "Hello, world!"

        self.assertEqual(len(steamspypi.download(data_request)), 0)


if __name__ == "__main__":
    unittest.main()
