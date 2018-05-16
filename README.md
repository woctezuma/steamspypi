# SteamSpyPI: an API for SteamSpy

[![PyPI status][PyPI image]][PyPI] [![Build status][Build image]][Build] [![Updates][Dependency image]][PyUp] [![Python 3][Python3 image]][PyUp] [![Code coverage][Coveralls image]][Coveralls] [![Code coverage BIS][Codecov image]][Codecov]

  [PyPI]: https://pypi.python.org/pypi/steamspypi
  [PyPI image]: https://badge.fury.io/py/steamspypi.svg

  [Build]: https://travis-ci.org/woctezuma/steamspypi
  [Build image]: https://travis-ci.org/woctezuma/steamspypi.svg?branch=master

  [PyUp]: https://pyup.io/repos/github/woctezuma/steamspypi/
  [Dependency image]: https://pyup.io/repos/github/woctezuma/steamspypi/shield.svg
  [Python3 image]: https://pyup.io/repos/github/woctezuma/steamspypi/python-3-shield.svg

  [Coveralls]: https://coveralls.io/github/woctezuma/steamspypi?branch=master
  [Coveralls image]: https://coveralls.io/repos/github/woctezuma/steamspypi/badge.svg?branch=master

  [Codecov]: https://codecov.io/gh/woctezuma/steamspypi
  [Codecov image]: https://codecov.io/gh/woctezuma/steamspypi/branch/master/graph/badge.svg

This repository contains Python code to download data through [SteamSpy API](https://steamspy.com/api.php).

## Installation

The code is packaged for [PyPI](https://pypi.org/project/steamspypi/), so that the installation consists in running:

```bash
pip install steamspypi
```

## Usage

### Returns details for every game. Data is sorted by decreasing number of owners.

```python
import steamspypi

data_request = dict()
data_request['request'] = 'all'

data = steamspypi.download(data_request)
```

### Returns details for every game. This time, data is cached locally for offline reuse.

```python
import steamspypi

data = steamspypi.load()
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