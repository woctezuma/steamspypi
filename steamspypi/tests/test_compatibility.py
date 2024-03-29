import unittest

import steamspypi


class TestCompatibilityMethods(unittest.TestCase):
    def test_fix_request_page(self):
        data_request = {}
        data_request["page"] = 0
        data_request = steamspypi.fix_request(data_request)
        assert data_request["page"] == "0"

    def test_fix_request_appid(self):
        data_request = {}
        data_request["appid"] = 730
        data_request = steamspypi.fix_request(data_request)
        assert data_request["appid"] == "730"

    def test_fix_request_genre(self):
        data_request = {}
        data_request["genre"] = "Early+Access"
        data_request = steamspypi.fix_request(data_request)
        assert data_request["genre"] == "Early Access"

    def test_fix_request_tag(self):
        data_request = {}
        data_request["tag"] = "Early+Access"
        data_request = steamspypi.fix_request(data_request)
        assert data_request["tag"] == "Early Access"

    def test_check_wrong_request_field(self):
        data_request = {}
        data_request["Hello, world!"] = "appdetails"

        assert not steamspypi.check_request(data_request)

    def test_check_wrong_request_value(self):
        data_request = {}
        data_request["request"] = "Hello, world!"

        assert not steamspypi.check_request(data_request)

    def test_check_incomplete_request(self):
        data_request = {}
        data_request["request"] = "appdetails"

        assert not steamspypi.check_request(data_request)

    def test_check_missing_main_request(self):
        data_request = {}
        data_request["appid"] = "730"

        assert not steamspypi.check_request(data_request)


if __name__ == "__main__":
    unittest.main()
