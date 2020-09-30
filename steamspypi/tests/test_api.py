import unittest

import steamspypi


class TestApiMethods(unittest.TestCase):
    def test_get_api_parameters(self):
        ground_truth = [
            "request",
            "appid",
            "genre",
            "tag",
            "page",
        ]

        api_parameters = steamspypi.get_api_parameters()

        for parameter in ground_truth:
            self.assertIn(parameter, api_parameters)

    def test_get_api_request_requirements(self):
        ground_truth = {
            "appdetails": ["appid"],
            "genre": ["genre"],
            "tag": ["tag"],
            "top100in2weeks": [],
            "top100forever": [],
            "top100owned": [],
            "all": ["page"],
        }

        api_request_values = steamspypi.get_api_request_requirements()

        for parameter, requirement in ground_truth.items():
            self.assertIn(parameter, api_request_values.keys())
            self.assertListEqual(requirement, api_request_values[parameter])


if __name__ == "__main__":
    unittest.main()
