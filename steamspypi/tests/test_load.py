import unittest

import steamspypi


class TestLoadMethods(unittest.TestCase):
    def test_load(self):
        # Download
        data = steamspypi.load()
        self.assertGreater(len(data), 0)

        # Load from cache
        data = steamspypi.load()
        self.assertGreater(len(data), 0)

    def test_load_app_ids(self):
        app_ids = steamspypi.load_app_ids()
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

        data = steamspypi.download(data_request)

        self.assertTrue(steamspypi.print_data(data))


if __name__ == "__main__":
    unittest.main()
