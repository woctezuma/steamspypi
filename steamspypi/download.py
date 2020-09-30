import requests

from steamspypi.compatibility import check_request, fix_request


def get_api_url():
    api_url = "https://steamspy.com"

    return api_url


def get_api_endpoint():
    api_endpoint = "/api.php"

    return api_endpoint


def get_default_data_request():
    # Download Steam's whole catalog of applications
    data_request = dict()
    data_request["request"] = "all"
    data_request["page"] = "0"

    print(
        "Limited to 1000 games for this request (page={})".format(data_request["page"])
    )

    return data_request


def download(data_request, url=None):
    if url is None:
        url = get_api_url() + get_api_endpoint()

    is_request_correct = check_request(data_request)

    data_request = fix_request(data_request)

    if is_request_correct:
        response = requests.get(url=url, params=data_request)
    else:
        response = None
        print("Incorrect request: download is cancelled.")

    if response is not None and response.ok:
        data = response.json()
    else:
        data = dict()

    return data


if __name__ == "__main__":
    data = download({"request": "appdetails", "appid": "573170"})

    print(data)
