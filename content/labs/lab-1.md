Title: Lab 1 - virtualenv & curl
Date: 2019-01-04 15:24
Category: Lab

----

Introduction to CMPUT 404 labs. Setup [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) and understand basic usage of [curl](https://curl.haxx.se/).

Create a text file `lab1-${ccid}.txt` containing answers to the questions and submit to *Lab 1* on eClass. For example, if your ccid is `bob`, the text file should be `lab1-bob.txt`.

### Git and GitHub

1. Make a GitHub account or log in to your existing GitHub account.

    **Question 1**: What is your GitHub URL?

### virtualenv

1. Create a new directory for this lab (`mkdir`).
1. `cd` into the created directory and initialize a new git repository (`git init`).
1. Try installing [requests](https://pypi.org/project/requests/).

    `pip install requests`

1. Make a Python script that prints out the version of the requests library.

    **Question 2**: What version is the requests library installed on the system?

1. Create a virtualenv.

    `virtualenv venv --python=python3`

1. Activate the python virtual environment.

    `source venv/bin/activate`

1. Try installing [requests](https://pypi.org/project/requests/) into your virtual environment.
1. Run your Python script that prints out the version of the requests library in your virtualenv.

    **Question 3**: What version is the requests library installed in the virtualenv?

1. Open a new terminal.
1. Run the script in your new terminal.

    **Question 4**: Does your script print out the same version? Why?

### curl

1. Use `curl` to get the Google homepage: [http://www.google.com/](http://www.google.com/)
1. This time, use `curl -i` to get the Google homepage.

    **Question 5**: What status code is returned? What URL must you visit to get a 200 status code?

1. Curl the Google home page with `-iL` and examine the headers.
1. Curl the Google Teapot page: [https://www.google.com/teapot](https://www.google.com/teapot)
1. Modify your Python script to GET the Google homepage.

    **Question 6**: What status code is returned this time? Is it the one returned by `curl -i` or `curl -iL`?

1. Try `curl -i https://webdocs.cs.ualberta.ca/~hindle1/1.py`
1. Try it again `curl -i -X POST -d "X=Y"`

    **Question 7**: What changed in the output of [https://webdocs.cs.ualberta.ca/~hindle1/1.py](https://webdocs.cs.ualberta.ca/~hindle1/1.py) when you used `-X POST`? What is this method useful for?

1. Commit your Python script and push it to GitHub.
1. Find the raw URL to your Python script on GitHub.
1. Modify your Python script so that it downloads itself from GitHub and prints out its own source code **from GitHub**.
1. Push the new version of your Python script to GitHub.

    **Question 8**: What is the raw URL to your Python script on GitHub?
