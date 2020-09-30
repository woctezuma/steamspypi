from steamspypi.api import get_api_parameters, get_api_request_requirements


def fix_request(data_request):
    if "page" in data_request:
        # Make sure pages are strings, not integers.
        data_request["page"] = str(data_request["page"])

    if "appid" in data_request:
        # Make sure appid are strings, not integers.
        data_request["appid"] = str(data_request["appid"])

    if "genre" in data_request:
        # Make sure genres are submitted with space characters, not with '+' as shown in SteamSpy API documentation.
        data_request["genre"] = data_request["genre"].replace("+", " ")

    if "tag" in data_request:
        # Make sure tags are submitted with space characters, not with '+' as shown in SteamSpy API documentation.
        data_request["tag"] = data_request["tag"].replace("+", " ")

    return data_request


def check_request(data_request):
    is_request_correct = True

    for element in data_request:
        if element not in get_api_parameters():
            print("Requested {} is not standard.".format(element))
            is_request_correct = False

    try:
        main_request = data_request["request"]

        for required_element in get_api_request_requirements()[main_request]:
            if required_element not in data_request:
                print("Required {} is missing.".format(required_element))
                is_request_correct = False
    except KeyError:
        print("No request field could be found.")
        is_request_correct = False

    return is_request_correct
