# poetry-plugin-autosetup

This plugin creates (or rebuilds) the setup.py file

## Features

* Creates setup.py based on your data in pyproject.toml

## Contents
* [How install?](#how-install) 
* [How to work with it?](#how-to-work-with-it) 


## How install?

[Poetry](https://python-poetry.org/)

```sh
poetry self add git+https://github.com/axemanofic/poetry-plugin-setuppy.git
```

## How to work with it?

* Create a new project with ``poetry new <name_project>`` or in an existing project, enter ``poetry init``. 
    You should have a ``pyproject.toml`` file at the root of your project.

```sh
test_project
├── pyproject.toml
├── README.rst
├── test_project
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_test_project.py
```
* Use the ``poetry setuppy`` command in your project to generate a ``setup.py``
* Every time you change information in ``pyproject.toml`` use ``poetry setuppy`` to have the plugin update your ``setup.py``