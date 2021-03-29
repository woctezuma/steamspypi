# Reference: https://gist.github.com/woctezuma/a8a9cbde6b03868b8631d2f436bbcfab

import json
import time
from pathlib import Path

from steamspypi.download import download


def get_cooldown():
    cooldown = 70  # 1 minute plus a cushion

    return cooldown


def get_some_sleep():
    cooldown = get_cooldown()
    print("Sleeping for {} seconds on {}".format(cooldown, time.asctime()))

    time.sleep(cooldown)

    return


def download_a_single_page(page_no=0):
    print("Downloading page={} on {}".format(page_no, time.asctime()))

    data_request = dict()
    data_request["request"] = "all"
    data_request["page"] = str(page_no)

    data = download(data_request)

    return data


def get_file_name(page_no):
    # Get current day as yyyymmdd format
    date_format = "%Y%m%d"
    current_date = time.strftime(date_format)

    file_name = "{}_steamspy_page_{}.json".format(current_date, page_no)

    return file_name


def download_all_pages(num_pages):
    actual_num_pages = num_pages

    # Download

    for page_no in range(num_pages):
        file_name = get_file_name(page_no)

        if not Path(file_name).is_file():
            page_data = download_a_single_page(page_no=page_no)

            if len(page_data) == 0:
                # The for-loop starts at page_no==0, so the number of pages is page_no after an empty response.
                actual_num_pages = page_no
                print(f'Setting the number of pages from {num_pages} (input) to {actual_num_pages} (actual).')
                break

            with open(file_name, "w", encoding="utf8") as f:
                json.dump(page_data, f)

            if page_no != (num_pages - 1):
                get_some_sleep()

    # Aggregate

    data = dict()

    for page_no in range(actual_num_pages):
        file_name = get_file_name(page_no)

        with open(file_name, "r", encoding="utf8") as f:
            page_data = json.load(f)

            data.update(page_data)

    return data


if __name__ == "__main__":
    # Caveat: one has to figure out the number of pages.
    # NB: there are exactly 44 pages as of March 29, 2021.
    data = download_all_pages(num_pages=44)
