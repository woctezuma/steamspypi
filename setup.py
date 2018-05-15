from distutils.core import setup

# noinspection PyUnresolvedReferences
import setuptools

setup(
    name='steamspypi',
    packages=['steamspypi'],
    install_requires=[
        'requests',
    ],
    version='0.8',
    description='SteamSpy API on PyPI',
    long_description='SteamSpyPI: an API for SteamSpy, written in Python 3.',
    long_description_content_type='text/x-rst',
    author='Wok',
    author_email='wok@tuta.io',
    url='https://github.com/woctezuma/steamspypi',
    download_url='https://github.com/woctezuma/steamspypi/archive/0.8.tar.gz',
    keywords=['steam', 'steamspy', 'api'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
