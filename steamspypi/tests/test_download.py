import json
import unittest

import steamspypi


class TestDownloadMethods(unittest.TestCase):
    def get_api_error_message(self):
        return "SteamSpy API is down."

    def test_get_api_url(self):
        api_url = steamspypi.get_api_url()
        assert api_url == "https://steamspy.com"

    def test_get_api_endpoint(self):
        api_endpoint = steamspypi.get_api_endpoint()
        assert api_endpoint == "/api.php"

    def test_get_default_data_request(self):
        data_request = steamspypi.get_default_data_request()
        self.assertDictEqual(data_request, {"request": "all", "page": "0"})

    def test_download_all(self):
        data_request = {}
        data_request["request"] = "all"
        data_request["page"] = "0"

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        print(f"[Steam catalog] #games = {len(data)}")

        assert len(data) > 0

    def test_download_appdetails(self, appid=730):
        data_request = {}
        data_request["request"] = "appdetails"
        data_request["appid"] = str(appid)

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        print("[appID = {}] game name = {}".format(appid, data["name"]))

        expected_game_name = "Counter-Strike: Global Offensive"

        assert data["name"] in [expected_game_name, self.get_api_error_message()]

    def test_download_genre(self, genre="Early Access"):
        data_request = {}
        data_request["request"] = "genre"
        data_request["genre"] = genre

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        print(f"[genre = {genre}] #games = {len(data)}")

        assert len(data) > 0

    def test_download_tag(self, tag="Early Access"):
        data_request = {}
        data_request["request"] = "tag"
        data_request["tag"] = tag

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        print(f"[tag = {tag}] #games = {len(data)}")

        assert len(data) > 0

    def test_download_top100in2weeks(self):
        data_request = {}
        data_request["request"] = "top100in2weeks"

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        print("[request = {}] #games = {}".format(data_request["request"], len(data)))

        assert len(data) > 0

    def test_download_top100forever(self):
        data_request = {}
        data_request["request"] = "top100forever"

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        print("[request = {}] #games = {}".format(data_request["request"], len(data)))

        assert len(data) > 0

    def test_download_top100owned(self):
        data_request = {}
        data_request["request"] = "top100owned"

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        print("[request = {}] #games = {}".format(data_request["request"], len(data)))

        assert len(data) > 0

    def test_cancel_download(self):
        data_request = {}
        data_request["request"] = "Hello, world!"

        assert len(steamspypi.download(data_request)) == 0


if __name__ == "__main__":
    unittest.main()
