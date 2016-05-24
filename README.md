# Project for AvtoZip backend API and admin

## Badges
[![Circle CI](https://circleci.com/gh/AvtoZip/api-avtozip.svg?style=shield)](https://circleci.com/gh/AvtoZip/api-avtozip)
[![codecov.io](https://codecov.io/github/AvtoZip/api-avtozip/coverage.svg)](https://codecov.io/github/AvtoZip/api-avtozip)
[![Coverage Status](https://coveralls.io/repos/github/AvtoZip/api-avtozip/badge.svg)](https://coveralls.io/github/AvtoZip/api-avtozip)

## Component Stack

| Component         | Version |
|:-----------------:|:-------:|
| Python            |     3.5 |
| Django            |     1.9 |
| PostgreSQL        |     9.5 |
| TastyPie REST API |    0.13 |
| NVM               |  0.31.4 |
| npm               | 2.14.20 |
| bower             |   1.8.0 |

## Installation instructions

1. **Preparation:**

  - *MacOS:*

    HomeBrew: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

1. **Install `Python3`:**

  - *MacOS:*

    ```bash
    brew install python3
    ```

  - *Linux (Ubuntu):*

    ```bash
    apt-get install python3
    ```

  - *Windows:*

    Download from [Python.ORG](https://www.python.org/downloads/) and install

1. **Install `PostgreSQL`:**

 - *MacOS:*

    ```bash
    brew install postgresql
    ```

  - *Linux (Ubuntu):*

    ```bash
    apt-get install postgresql
    ```

  - *Windows:*

    Download from [Postgresql.ORG](http://www.postgresql.org/download/windows/) and install

1. **Configure Python's virtual environment:**

  - *Installation (All platforms):*

    `pip install virtualenv`

  - *Creation of project's environment:*

    `virtualenv env` inside your project's root folder

  - *Activating virtual environment:*

    `. env/bin/activate` or `source env/bin/activate`

1. **Build and install packages:**

  - *Install NVM (virtual Node.js env):*

    Please install NVM from [here] https://github.com/creationix/nvm and execute described steps

  - *Expand NVM with specific version of Node.js:*

    `nvm install 4.4.1`

  - *Install npm:*

    `npm install`

  - *Install Bower:*

    `npm install -g bower`

  - *Makefile:*

    `make` inside project's root

1. **Configuration of PostgreSQL:**

  - *Either create user/password/database according to:*

    `api-avtozip/avtozip/avtozip/settings/development.py`

  - *Or override settings using `local.py.tmpl` file and save it:*

    `api-avtozip/avtozip/avtozip/settings/local.py`

1. **Run development server:**

  `make devserver`
