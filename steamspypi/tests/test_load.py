import json
import unittest

import steamspypi


class TestLoadMethods(unittest.TestCase):
    def get_api_error_message(self):
        return "SteamSpy API is down."

    def test_load(self):
        try:
            # Download
            data = steamspypi.load()
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}
        self.assertGreater(len(data), 0)

        try:
            # Load from cache
            data = steamspypi.load()
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}
        self.assertGreater(len(data), 0)

    def test_load_app_ids(self):
        try:
            app_ids = steamspypi.load_app_ids()
        except json.decoder.JSONDecodeError:
            app_ids = {self.get_api_error_message()}
        self.assertGreater(len(app_ids), 0)

    def test_prepare_data_before_saving_to_file(self):
        # fmt: off
        # Reference: https://github.com/psf/black#the-black-code-style

        # mixing single and double quotes
        # Reference: https://stackoverflow.com/a/8710579/
        input_data = {'jsonKey': 'jsonValue', "title": "hello world"}

        # fmt: on

        output_data = steamspypi.prepare_data_before_saving_to_file(input_data)
        self.assertEqual(output_data, str(input_data).replace("'", '"'))

    def test_print_data(self):
        data_request = dict()
        data_request["request"] = "appdetails"
        data_request["appid"] = "730"

        try:
            data = steamspypi.download(data_request)
        except json.decoder.JSONDecodeError:
            data = {"name": self.get_api_error_message()}

        self.assertTrue(steamspypi.print_data(data))


if __name__ == "__main__":
    unittest.main()
