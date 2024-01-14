title: HTTP Lab
date: 2024-01-06
tags: curl, http
authors: Hazel Victoria Campbell
status: published

----

[TOC]

# Description

Your task is to build a partially HTTP 1.1 compliant webserver. Your webserver will serve static content from the www directory in the same directory that you start the webserver in.

You are meant to understand the very basics of HTTP by having a hands-on ground up understanding of what it takes to have an HTTP connection.

# Collaboration

* You may consult with others (exhange high-level ideas) but the submission should be your own source code
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/lab.md#lab-marking)

# User Stories

* As a user I want to view files in ./www via a webbrowser, so I can see my website.
* As a user I want to view files in ./www via curl, so I can test my website.
* As a webserver admin I want to serve HTML and CSS files from ./www, so I don't have to deal with other file types.
* As a webserver admin I want ONLY files in ./www and deeper to be served, so I don't get hacked.

# Requirements

* The webserver can serve files from ./www
* The webserver can be run from the `free-tests.py` file
* The webserver can pass all the tests in `free-tests.py` file
* The webserver can pass all the tests in `secret-tests.py` file
    * You don't have this, but it is similar to `free-tests.py`: this is used to check against defeating the `free-tests.py` by modifying it, hardcoding responses, etc.
* The webserver supports mime-types for HTML
* The webserver supports mime-types for CSS
* The webserver can return index.html from directories (paths that end in /)
* The webserver can serve 404 errors for paths not found
* The webserver works with Firefox and Chomium-based browsers (Chrome/Edge/etc.)
* The webserver can serve CSS properly so that the front page has an orange h1 header.
* The webserver returns a `405 Method Not Allowed` for any method it cannot handle (POST/PUT/DELETE).
* The webserver uses a `301 Moved Permanently` to correct paths that go to directories but don't end in a '/' like they should.
* I can check out the source code via an HTTP git URL.
* Tests must execute within 60 seconds.
* The webserver must be started by calling the main function.

# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* Must run on Ubuntu (Use the undergrad lab machines, for example the ones in CSC 2-29 or install an Ubuntu VM to check this)
* The only allowed imports are `socketserver` and `pathlib`: You will recieve a zero mark for using any other imports.
* Your code must not modify the code out of its scope (must not do dependency injection), must not run anything at the top level (outside of functions/classes/defining constants), and must not try to work around or modify the test suite.

# Submission Instructions

Submit a link to your repo in the form `https://github.com/uofa-cmput404/f23-assignment-ajax-hazelcam` on eClass. **Do not** submit a link to a branch, a file, or the clone url. If you do not do this we will not know which github submission is yours.

# Tips

## Ubuntu on Windows

Install Ubuntu on Windows using WSL2. 

## Ubuntu on macOS ARM:
1. Install UTM for macOS: https://mac.getutm.app/
2. Download Ubuntu image for ARM: https://ubuntu.com/download/server/arm
3. Open the UTM app and Select "Create a New Virtual Machine"
4. Select "Virtualize" followed by "Linux"
5. Browse for the Ubuntu iso file you downloaded
6. Select your desired VM memory and CPU configs
7. Give your VM a name and select "Save"
8. Run the VM
9. Follow the onscreen prompts, default options are sufficient
10. Once the configuration is complete, shutdown the VM and dismount the iso file
11. Start and log into your VM
12. Run: `sudo apt install ubuntu-desktop` and `reboot`
You should now have access to Ubuntu desktop.

For more details, you can read [this](https://jun1okamura.medium.com/install-ubuntu-on-mac-m1-powered-by-utm-499aba3ba7e9).

## For macOS with homebrew:

1. `brew install git`
2. `brew install python@3`
3. `sudo pip3 install virtualenv`
4. In your repository directory, `virtualenv venv --python=python3`
5. Activate the virtual environment: `source venv/bin/activate`
6. Install requests: `pip3 install requests`


## For Windows 10 with pip:

In cmd (not powershell):

1. pip install requests
2. pip install virtualenv
3. In your repository directory, `virtualenv venv --python=python3`
    * if you get the error "virtualenv not found" try forcing a reinstall with pip install virtualenv --force-reinstall
4 To activate: venv\Scripts\activate

As of 2018 all Windows 10 machines come pre-installed with curl, so you should have it already.  

## Ubuntu Lab Computers

Connect to one of the lab machines at the University if needed. 

They are named like `ug01.cs.ualberta.ca`, `ug02.cs.ualberta.ca`, all the way up to `ug34.cs.ualberta.ca`:

`ssh yourccid@ugXX.cs.ualberta.ca``

For example:

`ssh hazelcam@ug15.cs.ualberta.ca`

To quit the ssh connection to the lab machine, use the exit command or press control-D on a blank prompt. If that does not work you can force close the connection by pressing enter, then ~, then .

**Want to view stuff in terminal but it scrolled off the top of the page?**

Try using the more command to scroll page by page. For example, you can pipe the output of curl to more to scroll through the output of curl page by page:

curl -s url | more

(The -s option to curl prevents curl from displaying download progress. You can combine it with other curl options like -i and -L.)

