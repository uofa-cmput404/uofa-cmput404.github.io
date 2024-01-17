Title: Django Lab
date: 2024-01-16
tags: labs
authors: Alireza Azimi
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking

----

[TOC]

# Description

The purpose of this lab is to familiarize you with setting up a virtual environment, developing in django and using npm.
By the end of this lab you will make a simple emoji picker app.

# Getting Started

## Installing venv with pip
Virtual environment is a CLI tool for managing python dependencies. Different projects have different dependencies, and version requirements. A virtual environment allows you to manage your dependencies specific to your project.

To install follow these steps (Note that you need pip installed and configured):

1. `python -m pip install --user virtualenv`
2. Check installation: `python -m virtualenv --help` 

For more info check [here](https://virtualenv.pypa.io/en/latest/installation.html).
To create and use a virtual environment:

1. `virtualenv venv --python=python3`
2. `source venv/bin/activate`

The first command will create a directory named `venv`. Contained in the directory is your
project dependecy installation and the `activate` script. Run `deactivate` to exit the virtual environment.


## Installing node JS and npm
To install node js, you can download the appropriate installer directly from the node js
[website](https://nodejs.org/en/download). Make sure to download the LTS version. The installation 
will include npm as well.

# Lab Instructions

The framework we will be using for this lab is [django](https://www.djangoproject.com/), a high-level python web framework. Django is a well documented framework, with a large developer community. The official django [documentation](https://docs.djangoproject.com/en/5.0/) is also an ideal place to learn more and look up specific features.

Get started by creating a virtual environment and installing django: 

1. Within your assignment directory create a virtual environment: `virtualenv venv --python=python3`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install django: `python -m pip install Django`
4. Verify installation by running a python shell and using: `import django`

To create a django project:

1. Run `django-admin startproject lab2`
2. Verify "lab2" directory containing project files is created
3. move into directory: `cd lab2`
4. Run `python manage.py runserver 0.0.0.0:8000`
5. In your browser access `localhost:8000`

If all went well you should see a "Congratulations!" with a rocket flying off.

In this lab we will be using an emoji picker package to display emojis on a django webpage. We will create a webapp called "emojis" using django. To create a new webapp inside your django project run `python manage.py startapp emojis`. This will create an `emojis` directory in your folder. Locate `emojis/views.py` and add the following code:

```python
from django.http import HttpResponse # Make sure to include this import


def index(request):
    return HttpResponse("This is the emoji app.")
```

Create a `urls.py` within the `emojis` directory, and add the following code:
```python
from django.urls import path

from . import views # . referes to the current module we are in

urlpatterns = [
    path("", views.index, name="index"),
]
```

Ensure your `lab2/urls.py` looks like this:

```python
from django.contrib import admin
from django.urls import include, path # make sure you have "include"

urlpatterns = [
    path("emojis/", include("emojis.urls")),
    path("admin/", admin.site.urls),
]
```

Make sure to register your app with the project by modifying `lab2/settings.py`:
```python
INSTALLED_APPS = [
    'emojis.apps.EmojisConfig', # don't forget to add this line !!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Access the emojis app using: `localhost:8000/emojis` from your browser.

Now it's pretty boring receiving a plain text response. Let's try rendering an html page. One way to achieve this using django is with `templates`:

1. Create `templates` directory inside `emojis`. Django will look for this directory by default.
2. Inside templates create a file called `index.html`.

Place the following html boilerplate inside `index.html`:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Emojis App</title>
    </head>
    <body>
        <h1>Welcome to Emojis!</h1>
    </body>
</html>
```

Go back to `emojis/views.py` and make sure to render this html template:
```python
from django.shortcuts import render # Import this shortcut function

def index(request):
    return render(request, "index.html")
```

Now you should get a big welcome message when you access `localhost:8000/emojis`.

Npm is a package manager for node JS. Node JS is a runtime environment for JavaScript. The node JS developer community use npm to distribute useful packages. For this lab we will be using [emoji-mart](https://www.npmjs.com/package/emoji-mart) to create a fun browser based emoji picker. 

To use the package we need to install the JavaScript modules using npm:

1. Run `npm install --save emoji-mart` in your project root where `manage.py` is.
2. This should create a new directory called `node_modules`
3. Locate `node_modules/emoji-mart/dist` which contains the JS files for the package
4. Create a directory called `static` inside `emojis`, where you made the `templates` directory
5. Copy `node_modules/emoji-mart` into that directory (Why?)

The reason why we didn't directly install `node_modules` inside `static` is mainly a safety practice. static files are accessible through the browser, therefore you need to make sure you are only allowing that for the files you want. Additionally, though not in the scope of this lab, some npm packages are designed to run in the node JS environment on a server; so, they are not suited for a browser.

Now that we have our static files ready to go, modify your `index.html` to load the static files.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Emojis App</title>
    </head>
    <body>
        <h1>Welcome to Emojis!</h1>
    </body>
    <script src="{% static 'emoji-mart/dist/browser.js' %}"></script>
    <script>
        // Add your code here
    </script> 
</html>
```

As part of your lab you need to write the code that will add the emoji picker to the dom using the package we have included. **You MUST NOT modify the body tag directly**. If successful, you should be able to see an emoji picker in your browser.

# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* Must run on Ubuntu (Use the undergrad lab machines, for example the ones in CSC 2-29 or install an Ubuntu VM to check this)

# Before You Submit
Make sure to include an appropriate `.gitignore` file, to prevent unwanted files being commited to your repository.
Place this gitignore within the root of your project. You can use [this one](https://github.com/django/django/blob/main/.gitignore) for your django project. Double check you're not staging any unwanted files before you commit. The `git status` command can help with that.

# Submission Instructions

Make sure you push to github classroom **BEFORE 4PM on the day of your lab section!** You will not be able to push after that!

Submit a link to your repo in the form `https://github.com/uofa-cmput404/w24-h0x-labsignment-django-yourgithubname` on eClass. **Do not** submit a link to a branch, a file, or the clone url. If you do not do this we will not know which github submission is yours.

# Collaboration

* You may consult with others (exchange high-level ideas) but the submission should be your own source code.
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/labs.md#lab-marking)

# Tips

Django is a complex framework and maybe overwhelming at times. You should consult the documentation should you run into any issues with the framework. 

If you're unable to load a static file or resource, it maybe because you're not referencing it correctly. It may be in a different directory or you have a typo when you are referencing that particular resource using its path. 

Another common problem is not being able to render the templates even though you're directory structure is correct. Make sure your app is registered in `settings.py` otherwise it may not render.