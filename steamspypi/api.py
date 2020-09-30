def get_api_parameters():
    api_parameters = [
        "request",
        "appid",
        "genre",
        "tag",
        "page",
    ]

    return api_parameters


def get_api_request_requirements():
    # For each acceptable request value, specify the required API parameters to be filled in.
    api_request_values = {
        "appdetails": ["appid"],
        "genre": ["genre"],
        "tag": ["tag"],
        "top100in2weeks": [],
        "top100forever": [],
        "top100owned": [],
        "all": ["page"],
    }

    return api_request_values


if __name__ == "__main__":
    api_parameters = get_api_parameters()
    api_request_values = get_api_request_requirements()

    print(api_parameters)
    print(api_request_values)
