import time
from pathlib import Path


def get_data_folder():
    data_folder = "data/"
    # Reference: https://stackoverflow.com/a/14364249
    Path(data_folder).mkdir(exist_ok=True, parents=True)

    return data_folder


def get_current_day_as_str(date_format="%Y%m%d"):
    current_day_as_str = time.strftime(date_format)

    return current_day_as_str


def get_file_name_suffix():
    file_name_suffix = "_steamspy.json"

    return file_name_suffix


def get_cached_database_filename():
    json_filename = get_current_day_as_str() + get_file_name_suffix()

    return json_filename


if __name__ == "__main__":
    data_folder = get_data_folder()
    json_filename = get_cached_database_filename()

    print(data_folder + json_filename)
