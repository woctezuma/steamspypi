import json

from steamspypi.download import get_default_data_request, download
from steamspypi.utils import get_data_folder, get_cached_database_filename


def load(file_name=None, url=None):
    if file_name is None:
        file_name = get_data_folder() + get_cached_database_filename()

    try:
        with open(file_name, "r", encoding="utf8") as f:
            data = json.load(f)

    except FileNotFoundError:
        print("Downloading and caching data from SteamSpy to {}".format(file_name))
        data = download(get_default_data_request(), url=url)

        # Cache the json data to a local file
        print_data(data, save_filename=file_name)

    return data


def load_app_ids(file_name=None, url=None, verbose=True):
    data = load(file_name=file_name, url=url)

    app_ids = [int(app_id) for app_id in data.keys()]

    app_ids = sorted(app_ids, key=int)

    if verbose:
        print("#appIDs = {}".format(len(app_ids)))

    return app_ids


def prepare_data_before_saving_to_file(data_as_json):
    # Enforce double-quotes instead of single-quotes.
    # Reference: https://stackoverflow.com/a/8710579/
    data_as_str = json.dumps(data_as_json)

    return data_as_str


def print_data(data, save_filename=None):
    if save_filename is not None:
        with open(save_filename, "w", encoding="utf8") as f:
            json.dump(data, f)

    else:
        data_as_str = prepare_data_before_saving_to_file(data)
        printable_data = data_as_str.replace(', "', '\n"')

        print(printable_data)

    return True


if __name__ == "__main__":
    data = load()
    app_ids = load_app_ids()
