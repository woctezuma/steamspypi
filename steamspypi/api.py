import requests


def fix_request(data_request):
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
        if element not in get_api_parameters():
            print('Requested {} is not standard.'.format(element))
            is_request_correct = False

    main_request = data_request['request']

    for required_element in get_api_request_requirements()[main_request]:
        if required_element not in data_request:
            print('Required {} is missing.'.format(required_element))
            is_request_correct = False

    return is_request_correct


def download(data_request):
    is_request_correct = check_request(data_request)

    data_request = fix_request(data_request)

    if is_request_correct:
        response = requests.get(get_steamspy_api_url(), params=data_request)
        data = response.json()
    else:
        print('Incorrect request: download is cancelled.')
        data = dict()

    return data


def get_steamspy_api_url():
    steamspy_api_url = 'https://steamspy.com/api.php'

    return steamspy_api_url


def get_example_api_parameters():
    default_api_parameters = {
        'request': 'all',
        'appid': '730',
        'genre': 'Early Access',
    }

    return default_api_parameters


def get_api_parameters():
    api_parameters = [
        'request',
        'appid',
        'genre',
    ]

    return api_parameters


def get_api_request_requirements():
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


def prepare_data_before_saving_to_file(data_as_json):
    import json

    # Enforce double-quotes instead of single-quotes. Reference: https://stackoverflow.com/a/8710579/
    data_as_str = json.dumps(data_as_json)

    return data_as_str


def main():
    data_request = dict()
    data_request['request'] = 'appdetails'
    data_request['appid'] = '730'

    data = download(data_request)

    print(data)

    return True


if __name__ == '__main__':
    main()
