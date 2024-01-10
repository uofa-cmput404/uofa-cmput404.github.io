title: HTTP Lab
date: 2024-01-06
tags: curl, http
authors: Hazel Victoria Campbell
status: published

----

[TOC]

# Submission Instructions

Submit a link to your repo in the form `https://github.com/uofa-cmput404/f23-assignment-ajax-hazelcam` on eClass. **Do not** submit a link to a branch, a file, or the clone url.

Your submission needs to pass the free tests (included) and the secret tests (you don't have these).


# Tips

## Ubuntu on Windows

Install Ubuntu on Windows using WSL2. 

## For macOS with homebrew:

1. `brew install git`
2. `brew install python@3`
3. `sudo pip3 install virtualenv`

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

