def _fix_request(data_request):
    if 'appid' in data_request:
        # Make sure appid are strings, not integers.
        data_request['appid'] = str(data_request['appid'])

    if 'genre' in data_request:
        # Make sure genres are submitted with space characters, not with '+' as shown in SteamSpy API documentation.
        data_request['genre'] = data_request['genre'].replace('+', ' ')

    return data_request


def check_request(data_request):
    is_request_correct = True

    for element in data_request:
        if element not in _get_api_parameters():
            print('Requested {} is not standard.'.format(element))
            is_request_correct = False

    try:
        main_request = data_request['request']

        for required_element in _get_api_request_requirements()[main_request]:
            if required_element not in data_request:
                print('Required {} is missing.'.format(required_element))
                is_request_correct = False
    except KeyError:
        print('No request field could be found.')
        is_request_correct = False

    return is_request_correct


def download(data_request):
    import requests

    is_request_correct = check_request(data_request)

    data_request = _fix_request(data_request)

    if is_request_correct:
        response = requests.get(_get_steamspy_api_url(), params=data_request)
        data = response.json()
    else:
        print('Incorrect request: download is cancelled.')
        data = dict()

    return data


def _get_steamspy_api_url():
    steamspy_api_url = 'https://steamspy.com/api.php'

    return steamspy_api_url


def get_example_api_parameters():
    default_api_parameters = {
        'request': 'all',
        'appid': '730',
        'genre': 'Early Access',
    }

    return default_api_parameters


def _get_api_parameters():
    api_parameters = [
        'request',
        'appid',
        'genre',
    ]

    return api_parameters


def _get_api_request_requirements():
    # For each acceptable request value, specify the required API parameters to be filled in.
    api_request_values = {
        'appdetails': ['appid'],
        'genre': ['genre'],
        'top100in2weeks': [],
        'top100forever': [],
        'top100owned': [],
        'all': [],
    }

    return api_request_values


def _prepare_data_before_saving_to_file(data_as_json):
    import json

    # Enforce double-quotes instead of single-quotes. Reference: https://stackoverflow.com/a/8710579/
    data_as_str = json.dumps(data_as_json)

    return data_as_str


def print_data(data_as_json, save_filename=None):
    data_as_str = _prepare_data_before_saving_to_file(data_as_json)

    if save_filename is None:

        printable_data = data_as_str.replace(', \"', '\n\"')

        print(printable_data)

    else:
        with open(save_filename, 'w', encoding="utf8") as cache_json_file:
            print(data_as_str, file=cache_json_file)

    return True


def get_cached_database_filename():
    import time

    json_filename_suffix = "_steamspy.json"

    # Get current day as yyyymmdd format
    date_format = "%Y%m%d"
    current_date = time.strftime(date_format)

    # Database filename
    json_filename = current_date + json_filename_suffix

    return json_filename


def get_data_folder():
    data_path = "data/"
    return data_path


def load(json_filename=None, data_request=None):
    import pathlib
    import json

    # Data folder
    data_path = get_data_folder()
    # Reference of the following line: https://stackoverflow.com/a/14364249
    pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)

    if json_filename is None:
        json_filename = get_cached_database_filename()

    if data_request is None:
        # Download Steam's whole catalog of applications
        data_request = dict()
        data_request['request'] = 'all'

    data_filename = data_path + json_filename

    try:
        with open(data_filename, 'r', encoding="utf8") as in_json_file:
            data = json.load(in_json_file)
    except FileNotFoundError:
        print("Downloading and caching data from SteamSpy to {}".format(data_filename))

        data = download(data_request)

        # Cache the json data to a local file
        print_data(data, data_filename)

    return data


if __name__ == '__main__':
    downloaded_data = download({'request': 'appdetails', 'appid': '573170'})

    print_data(downloaded_data)
