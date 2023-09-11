Title: Virtualenv & cURL
Date: 2019-01-04 15:24
Modified: 2023-09-11 10:04
Category: Lab
Tags: virtualenv, curl
Authors: Alexander Wong, Hazel Victoria Campbell

----

# Virtualenv & Curl Lab

Introduction to CMPUT 404 labs. Setup [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) and understand basic usage of [curl](https://curl.haxx.se/).

Answers to the questions should be submitted to *Virtualenv Lab* on eClass.

## Git and GitHub

1. Make a GitHub account or log in to your existing GitHub account.

    * **Question 1**: What is your GitHub URL?

## Command-line Environment

* Windows Users
    * You should install Ubuntu on WSL2, then follow Ubuntu instructions below.
        * Each time it suggests opening a new terminal, open a new Ubuntu terminal.
        * [Guide for installing Ubuntu/WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)
* Mac Users
    * [pip install virtualenv](https://programwithus.com/learn/python/pip-virtualenv-mac)
    * Alternately: [use brew](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
* Ubuntu Users
    * `sudo apt install python3-virtualenv`

## virtualenv

1. Create a new directory for this lab (`mkdir`).
1. `cd` into the created directory and initialize a new git repository (`git init`).
1. Make a Python script that prints out the version of the requests library.

    * **Question 2**: What version is the requests library installed on the system? Is there none at all? Or is it already installed?

1. Create a virtualenv.

    `virtualenv venv --python=python3`

1. Activate the python virtual environment.

    `source venv/bin/activate`

1. Try installing [requests](https://pypi.org/project/requests/) into your virtual environment.
1. Run your Python script that prints out the version of the requests library in your virtualenv.

    * **Question 3**: Is requests installed? If so, what version is the requests library installed in the virtualenv?

1. Open a new terminal.
1. Run the script in your new terminal.

    * **Question 4**: What is the difference between the virtual environment and the not virtual environment python?

### curl

1. Use `curl` to get the Google homepage: [http://google.com/](http://google.com/)
1. This time, use `curl -i` to get the Google homepage.

    * **Question 5**: What status code is returned for `http://google.com` ? What URL must you visit to get a 200 status code?

1. Curl the Google home page with `-iL` and examine the headers.
1. Curl the Google Teapot page: [https://www.google.com/teapot](https://www.google.com/teapot)

    * **Question 6**: What status code is returned for `http://google.com/teapot`? Is it the one returned by `curl -i` or `curl -iL`? What happens when you curl `http://www.google.com/teapot`?

1. Modify your Python script to GET the Google homepage.

1. Try `curl -i https://webdocs.cs.ualberta.ca/~hindle1/1.py`
1. Try it again `curl -i -X POST -d "X=Y"`

    * **Question 7**: What changed in the output of [https://webdocs.cs.ualberta.ca/~hindle1/1.py](https://webdocs.cs.ualberta.ca/~hindle1/1.py) when you used `-X POST`? What is this method useful for?

1. Commit your Python script and push it to GitHub.
1. Find the raw URL to your Python script on GitHub.
1. Modify your Python script so that it downloads itself from GitHub and prints out its own source code **from GitHub**.
1. Push the new version of your Python script to GitHub.

    * **Question 8**: What is the raw URL to your Python script on GitHub?
