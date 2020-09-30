import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='steamspypi',
    version='1.0.1',
    author='Wok',
    author_email='wok@tuta.io',
    description='SteamSpy API on PyPI',
    keywords=['steam', 'steamspy', 'api'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/woctezuma/steamspypi',
    download_url='https://github.com/woctezuma/steamspypi/archive/1.0.1.tar.gz',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Games/Entertainment',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
