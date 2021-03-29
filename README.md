# SteamSpyPI: an API for SteamSpy

[![PyPI status][pypi-image]][pypi]
[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]
  
This repository contains Python code to download data through [SteamSpy API][steamspy-api-docs].

## Installation

The code is packaged for [PyPI][steamspy-pypi], so that the installation consists in running:

```bash
pip install steamspypi
```

## Usage

### Returns details for 1000 games. Data is sorted by decreasing number of owners.

A `page` parameter is now required for `all` requests, starting at `page=0`.
You will be able to retrieve 1000 games per `all` request.

Moreover, the API rate is now heavily limited for `all` requests.
You will be able to issue 1 `all` request per minute.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'all'
data_request['page'] = '0'

data = steamspypi.download(data_request)
```

### Returns details for 1000 games. This time, data is cached locally for offline reuse.

In this case, `page` is forcibly set to `0`, without any access to this parameter for the end-user.

Local cache is in `data/%Y%m%d_steamspy.json`, without mentioning `page` in the file name for backward compatibility.

```python
import steamspypi

data = steamspypi.load()
```

### Returns details for all of the games.

Please refer to [this for-loop][github-gist-download-all] to accomodate recent API rate-limits.

Alternatively, if you know the number of pages, which was about 40 in August 2020:

```python
import steamspypi

data = steamspypi.download_all_pages(num_pages=40)
```

### Returns details for a given application.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'appdetails'
data_request['appid'] = '730'

data = steamspypi.download(data_request)
```

### Returns all games in a given genre.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'genre'
data_request['genre'] = 'Early Access'

data = steamspypi.download(data_request)
```

### Returns all games with a given tag.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'tag'
data_request['tag'] = 'Early Access'

data = steamspypi.download(data_request)
```

### Returns Top 100 games, with respect to the number of players in the last two weeks.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'top100in2weeks'

data = steamspypi.download(data_request)
```

### Returns Top 100 games, with respect to the number of players since March 2009.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'top100forever'

data = steamspypi.download(data_request)
```

### Returns Top 100 games, with respect to the estimated number of owners.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'top100owned'

data = steamspypi.download(data_request)
```

## References

-   [`gamedatacrunch`][gamedatacrunch-api]@[PyPI][gamedatacrunch-pypi]: an API to download data through [GameDataCrunch API][gamedatacrunch].

<!-- Definitions -->

[gamedatacrunch]: <https://www.gamedatacrunch.com>
[steamspy-api]: <https://github.com/woctezuma/steamspypi>
[steam-api]: <https://steamapi.xpaw.me/#ISteamApps/GetAppList>

[steamspy-api-docs]: <https://steamspy.com/api.php>
[steamspy-pypi]: <https://pypi.org/project/steamspypi/>
[gamedatacrunch-api]: <https://github.com/woctezuma/gamedatacrunch>
[gamedatacrunch-pypi]: <https://pypi.org/project/gamedatacrunch/>

[github-gist-download-all]: <https://gist.github.com/woctezuma/a8a9cbde6b03868b8631d2f436bbcfab>

<!-- Definitions for badges -->

[pypi]: <https://pypi.python.org/pypi/steamspypi>
[pypi-image]: <https://badge.fury.io/py/steamspypi.svg>

[build]: <https://github.com/woctezuma/steamspypi/actions>
[build-image]: <https://github.com/woctezuma/steamspypi/workflows/Python package/badge.svg?branch=master>
[publish-image]: <https://github.com/woctezuma/steamspypi/workflows/Upload Python Package/badge.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/steamspypi/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/steamspypi/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/steamspypi/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/steamspypi>
[codecov-image]: <https://codecov.io/gh/woctezuma/steamspypi/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/steamspypi>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/9663fc7c6fda4b3fb8769d6e5e9725e5>
