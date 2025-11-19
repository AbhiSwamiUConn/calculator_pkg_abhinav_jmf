Informational Badges:

[![PyPI version](https://badge.fury.io/py/calculator_pkg_abhinav_jmf.svg)](https://badge.fury.io/py/calculator_pkg_abhinav_jmf)
![PyPy](https://img.shields.io/badge/PyPy-7.3.17-blue)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/calculator_pkg_abhinav_jmf)](https://pypi.org/project/calculator_pkg_abhinav_jmf/)
![Tests](https://github.com/AbhiSwamiUConn/calculator_pkg_abhinav_jmf/actions/workflows/tests.yml/badge.svg)
![Linux](https://img.shields.io/badge/os-Linux-blue.svg)
![macOS Intel](https://img.shields.io/badge/os-macOS_Intel-lightgrey.svg)
![macOS ARM](https://img.shields.io/badge/os-macOS_ARM-lightgrey.svg)

Some Linting Badges (Where I could find them):

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2A6DBA.svg)](http://mypy-lang.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint/tree/main)
[![try/except style: tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)

# calculator\_pkg\_abhinav\_jmf


### If you like the repo, it would be awesome if you could add a star to it! It really helps out the visibility. Also for any questions at all we'd love to hear from you at abhinav.swaminathan@uconn.edu

* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [Licence](#license)

## Package Description

Calculator stuff that demos pybind11

## Usage
* [calculator\_pkg\_abhinav\_jmf](#calculator\_pkg\_abhinav\_jmf)

from a script:

```python
from calculator_pkg_abhinav_jmf import FileCalculator

print(FileCalculator().sum_file())
```

## Installation
* [calculator\_pkg\_abhinav\_jmf](#calculator\_pkg\_abhinav\_jmf)

Install python and pip if you have not already.

Then run:

```bash
pip3 install pip --upgrade
pip3 install wheel
```

For production:

```bash
pip3 install calculator_pkg_abhinav_jmf
```

This will install the package and all of it's python dependencies.

If you want to install the project for development:
```bash
git clone https://github.com/AbhiSwamiUConn/calculator_pkg_abhinav_jmf.git
cd calculator_pkg_abhinav_jmf
pip3 install -e .[test]
pre-commit install
```

To test the development package: [Testing](#testing)


## Testing
* [calculator\_pkg\_abhinav\_jmf](#calculator\_pkg\_abhinav\_jmf)

To test the package after installation:

```
cd calculator_pkg_abhinav_jmf
pytest calculator_pkg_abhinav_jmf
ruff check calculator_pkg_abhinav_jmf
ruff format calculator_pkg_abhinav_jmf
mypy calculator_pkg_abhinav_jmf
```

If you want to run it across multiple environments, and have python 3.10 and 3.11 installed:

```
cd calculator_pkg_abhinav_jmf
tox --skip-missing-interpreters
```


## Development/Contributing
* [calculator\_pkg\_abhinav\_jmf](#calculator\_pkg\_abhinav\_jmf)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Test it
5. Run tox
6. Commit your changes: `git commit -am 'Add some feature'`
7. Push to the branch: `git push origin my-new-feature`
8. Ensure github actions are passing tests
9. Email me at abhinav.swaminathan@uconn.edu if it's been a while and I haven't seen it

NOTE: all contributions from other contributors are listed under the existing license for this repo unless stated otherwise, and by contributing to this repo you agree to those terms and conditions.

## License
* [calculator\_pkg\_abhinav\_jmf](#calculator\_pkg\_abhinav\_jmf)

BSD License (see license file)
# calculator_pkg_abhinav_jmf
