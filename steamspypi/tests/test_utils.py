import unittest

import steamspypi


class TestUtilsMethods(unittest.TestCase):
    def test_get_data_folder(self):
        data_folder = steamspypi.get_data_folder()
        self.assertEqual(data_folder, "data/")

    def test_get_current_day_as_str(self):
        dummy_day_as_str = "20200923"
        current_day_as_str = steamspypi.get_current_day_as_str()
        self.assertEqual(len(current_day_as_str), len(dummy_day_as_str))

    def test_get_file_name_suffix(self):
        file_name_suffix = steamspypi.get_file_name_suffix()
        self.assertEqual(file_name_suffix, "_steamspy.json")

    def test_get_cached_database_filename(self):
        json_filename = steamspypi.get_cached_database_filename()
        self.assertIn(".json", json_filename)


if __name__ == "__main__":
    unittest.main()
