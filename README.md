[![Build](https://github.com/martinjanssenn/Xtendis-Demo/actions/workflows/build_test.yml/badge.svg)](https://github.com/martinjanssenn/Xtendis-Demo/actions/workflows/build_test.yml)

# Xtendis Test repository
This repository is used as a proof-of-concept for a happy flow with testing, docker, CI-CD and automatic deployment


## Setup
To use this repository, you should have the latest version of [Python](https://www.python.org/downloads/) and [Docker](https://docs.docker.com/engine/install/) installed.

After installing these components, install Pip3 by downloading the get-pip Python file from [this site](https://bootstrap.pypa.io).
On Windows run:
`python3 get-pip.py`

On Mac run:
`brew install pip3`

On Linux run:
```
sudo apt update
sudo apt install python3-pip
```

## Installation
To install all npm packages, run:
`npm install`

To install the necessary Python components and libraries, first create a virtual Python environment.

To create the virtual environment, run:
`python3 -m venv venv`

This creates the folder venv where the virtual environment lives.

To activate the virtual environment, run the following commands:

On Windows:
`venv\Scripts\activate.bat`

On Mac/Linux:
`source venv/bin/activate`

This should be run <b>every</b> time you start working with the Python project again. It's visible in your terminal if the virtual environment is active.

## Run the application

On the first go, or after updates to the project have been made, run:
`pip3 install -r requirements.txt`

This will ensure that all necessary packages and libraries as defined in requirements.txt will be installed in your virtual environment. 

You can now go ahead and run:
`python3 src/app.py`

This will start the Flask application on your local machine. 

## Test the application
To test the backend application, run:
`pytest`

This will unittest the full application.

To test the frontend application, run:
`npx cypress run`

