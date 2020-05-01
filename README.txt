stock_dashboard
==========
This program will allow a user with an Ally account to connect to Ally's API and retrieve stock information.  The information
will be displayed as a candlestick chart and various indicators can be enabled.

This program is not meant for trading.  Use at your own risk.


Getting Started
---------------

- Change directory into your newly created project.

    cd stock_dashboard

- Create a Python virtual environment.

    python3 -m venv venv

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools


- Create and edit config files from templates

    cp connectTEMPLATE.py connect.py
    -   You will need an account with Ally and register a Personal Program through the API.  Add credentials provided by
        Ally when the program was registered.
