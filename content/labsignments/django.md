Title: Django Lab
date: 2024-09-05
tags: labs
authors: Alireza Azimi, Mo Adel Abdelghany, William Qi
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking
----

<style>
    html body main {
        background-image: url("/theme/draft.png");
        background-repeat: repeat;
        background-size: 100%;
    }
</style>

[TOC]

---

# Description

The purpose of this lab is to familiarize you with setting up a virtual environment, developing with Django, and using npm to incorporate external packages like an emoji picker and a markdown editor. By the end of this lab, you will build a simple wiki app where users can add emojis, likes, edit content using Markdown, and delete content.

# Getting Started

### Introduction to HTML and JavaScript

Before diving into Django and npm, let’s go over some basics of HTML and JavaScript.

### HTML Basics

HTML is the structure of a webpage. It defines elements such as **headings** (`<h1>`, `<h2>`, etc.), **paragraphs** (`<p>`), and **divs** (`<div>`) to organize content.

#### Example HTML Structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <div>
        <p>This is a paragraph inside a div.</p>
    </div>
</body>
</html>
```

- **Headings** help organize content by importance. Use `<h1>` for the most important heading and `<h6>` for the least important.
- **Divs** are containers that group elements together. You can style or manipulate all content inside a div.

### JavaScript Basics

JavaScript is used to add interactivity to a web page. You can manipulate the **DOM** (Document Object Model), which represents the structure of the page, to change content, styles, or even add new elements.

#### Example JavaScript:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JS Example</title>
</head>
<body>
    <h1 id="heading">Hello, World!</h1>
    <button id="changeTextBtn">Change Text</button>

    <script>
        const button = document.getElementById('changeTextBtn');
        button.addEventListener('click', function() {
            document.getElementById('heading').textContent = 'You clicked the button!';
        });
    </script>
</body>
</html>
```

---

## Prepare your Repo

1. Get the GitHub classroom link from eClass, create your assignment, and clone it.
2. Create an appropriate `.gitignore` file to prevent unwanted files from being committed to your repository. 

Place this `.gitignore` file in the root of your project. You can combine [this one](https://github.com/github/gitignore/blob/main/Python.gitignore), [this one](https://github.com/github/gitignore/blob/main/Node.gitignore), and [this one](https://github.com/django/django/blob/main/.gitignore) for your Django + Node project. Use `git status` to ensure you're not staging any unwanted files before committing.

## Create the Virtual Environment

A virtual environment is a tool for managing Python dependencies specific to your project. Each project may have different requirements, and a virtual environment helps you manage these dependencies independently.

### Setting up Python:

If you have multiple versions of Python installed, always specify the version number:

```bash
python3.11 -m venv venv
```

### Check for pip and venv/virtualenv:

To verify if you have pip:

```bash
python3.11 -m pip
```

To check if `venv` or `virtualenv` is installed:

```bash
python3.11 -m venv --help
```

If you don't have `venv`, install it using pip:

```bash
python -m pip install --user virtualenv
```

### Activate Virtual Environment:

To activate the virtual environment:

```bash
source venv/bin/activate
```



---

## Installing Node.js and npm

To install Node.js, download the LTS version from the [Node.js website](https://nodejs.org/en/download). The installation will include npm as well, which we will use to manage JavaScript packages.

---

# Lab Instructions

## Django Setup

We will use [Django](https://www.djangoproject.com/), a high-level Python web framework. It simplifies web development by providing a built-in ORM, an admin panel, and much more. The [official documentation](https://docs.djangoproject.com/en/5.0/) is a valuable resource and **you will find it very helpful** to reference it during this lab for anything that is unclear.

### Steps to Set Up Django:

1. Create a virtual environment and install Django:

```
virtualenv venv --python=python3
source venv/bin/activate
echo "Django>=5.0.1" > requirements.txt
python -m pip install -r requirements.txt
```

2. Start a new Django project:

```
django-admin startproject lab2
cd lab2
python manage.py runserver 0.0.0.0:8000
```

You should see a "Congratulations!" page when visiting `localhost:8000`.

### Creating a Django Webapp

We will create a Django webapp called `wiki` to build a simple wiki app.

**Create a new app:**
```
python manage.py startapp wiki
```

**Modify `lab2/settings.py` to register your new wiki app to Django**
```py
INSTALLED_APPS = [
    'wiki', # Add this line!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**In `wiki/views.py`, add the following code:**

```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the wiki app.")
```

**Create a `urls.py` file inside `wiki` and add the following code:**
   
```py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

**Update `lab2/urls.py` to include the new app:**

```py
from django.urls import include, path
urlpatterns = [
    path("wiki/", include("wiki.urls")),
    path("admin/", admin.site.urls),
]
```

## Adding HTML Templates

Django allows you to render HTML templates. Let’s create an HTML page to display a homepage.

1. Inside the `wiki` directory, create a `templates` directory.
2. Inside `templates`, create an `index.html` file with the following boilerplate:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Wiki App</title>
    </head>
    <body>
        <h1>Welcome to your wiki!</h1>
    </body>
</html>
```

3. Update `wiki/views.py` to render the template:
```py
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```

Now, visiting `localhost:8000/wiki` will display the HTML template.

## Adding Markdown Editor

In this section, we will integrate a **Markdown editor** so that users can write content in Markdown format and see it rendered as HTML in the browser. We'll use the popular npm package `marked` for parsing Markdown content and converting it to HTML.

### Steps to Add the Markdown Editor:

Install the `marked` package in the root directory of your repository:
```bash
npm install --save-dev marked
```

Create a new directory in the root directory called `webapp` and create a `markdown-editor.js` file in it.

Update your `markdown-editor.js` file to the following:
```js
import { marked } from "marked"; // Import the markdown converter

// Handle Markdown conversion and rendering
document.getElementById('convert-btn').addEventListener('click', e => {
  e.preventDefault();   // Prevents native functionality for this event
  const markdownText = document.getElementById('markdown-editor').value;
  const htmlOutput = marked(markdownText); // Convert markdown to HTML
  document.getElementById('markdown-output').innerHTML = htmlOutput; // Add the generated HTML code to the output div element
});
```

This file (`webapp/markdown-editor.js`) depends on a node dependency and needs to be bundled with a tool called `esbuild` to make it ready to be able to run on a browser.

In your **base repository directory**, run the following command to use `esbuild` to bundle your `markdown-editor.js` file.
`npx esbuild ./webapp/markdown-editor.js --bundle --minify --sourcemap --outfile=./lab2/wiki/static/markdown-editor.min.js`

This command bundles your `markdown-editor.js` file and all the imports that it needs into one huge file called `markdown-editor.min.js`. It is now ready to be included into your Django application!

### Django Integration

While we do have the JavaScript for our markdown editor, we still need the HTML for the editor! Create a new HTML file called `editor.html` in `lab2/wiki/templates/` and add the following content:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>New Wiki Page</title>
</head>
<body>
    <h1>Welcome to the Wiki App!</h1>

    <div>
        <h3>Markdown Editor</h3>
        <textarea id="markdown-editor" rows="10" cols="50" placeholder="Write in Markdown..."></textarea>
        <button id="convert-btn">Convert to HTML</button>
    </div>

    <h3>Output</h3>
    <div id="markdown-output"></div> <!-- Rendered HTML output -->
    
    <script src="{% static 'markdown-editor.min.js' %}"></script> <!-- Load bundled JS -->
</body>
</html>
```

Add a new view function that will render this template in `wiki/views.py`
```py
def editor(request):
    return render(request, "editor.html")
```

In `wiki/urls.py`, add the new route for our markdown editor:

```py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.editor, name="add"),
]
```

If you navigate to `localhost:8000/add/` you should see your markdown editor!

We now have a visible markdown editor, but we have no way of actually storing data yet. So let’s store the content users create in a Django model.

Update `wiki/models.py` to create a model for storing user-created pages:

```python
from django.db import models

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()  # Markdown content
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.id} - {self.title}"
```

After creating the model, run `python3.11 manage.py makemigrations` and `python3.11 manage.py migrate` to create/update and apply our database schema.

### TASK - Backend For Storing Wiki Pages

Update the contents of `wiki/templates/editor.html` to this: **(DO NOT MODIFY THE HTML)**
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>New Wiki Page</title>
</head>
<body>
    <h1>Welcome to the Wiki App!</h1>

    <form id="save-form" method="POST" action="/wiki/save/">
        <input type="text" name="title" id="page-title" placeholder="Page Title"><br>
        <textarea id="markdown-editor" name="content" rows="10" cols="50"></textarea><br>
        <button id="convert-btn">Convert to HTML</button><br>
        <br>
        <button id="save-btn" type="submit">Save Page</button>
        {% csrf_token %}
    </form>

    <h3>Output</h3>
    <div id="markdown-output"></div> <!-- Rendered HTML output -->
    
    <script src="{% static 'markdown-editor.min.js' %}"></script> <!-- Load bundled JS -->
</body>
</html>
```

**Your task** is to create the backend logic for handling the submission of the add wiki page. Your logic **MUST** use the `Page` model that we created earlier in the lab and your logic **MUST** be run when sending a POST request to `/wiki/save/`. It **MUST** redirect to `/wiki/` after saving the page.

## Displaying Wiki Pages

While it's great that we can store wiki pages, we need a way to access them ourselves.

### Homepage

Change the `index.html` template in `wiki/templates`. Replace its contents with the following code snippet in it:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>My Wiki | Home</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>My Wiki Pages</h1>
        <a href="/wiki/add/">Add Article</a><br>
        <ul>
            {% for page in pages %}
                <li><a href="{{ page.url }}">{{ page.title }}</a></li>
            {% endfor %}
        </ul>
    </body>
</html>
```

Modify `wiki/views.py` to replace the `index` function and also add a new function:
```py
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Page

def index(request):
    pages = []

    page_objects = Page.objects.all()
    for page in page_objects:
        pages.append({
            "title": page.title,
            "url": reverse("view", kwargs={ "id": page.id })
        })
    return render(request, "index.html", { "pages": pages })

def view_page(request, id):
    page = get_object_or_404(Page, pk=id)
    return render(request, "page.html", { "title": page.title, "content": page.content, "id": id })
```

Modify `wiki/urls.py` to include our new view function.
```py
path("page/<int:id>/", views.view_page, name="view")
```

### Wiki Page

Create a new file `wiki/templates/page.html` and paste the following snippet in:
```html
{% load static %}
<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body> 
        <div id="content" style="display: none;">{{ content }}</div>
        <div>
            <a href="/wiki/">&lt; Go Back</a>
        </div>
    </body>
    <script src="{% static 'markdown-renderer.min.js' %}"></script> <!-- Load bundled JS -->
</html>
```

In the `webapp` folder, create a new file called `markdown-renderer.js` and paste the following snippet in:
```js
import { marked } from "marked"; // Import the markdown converter

// Handle rendering
window.addEventListener('load', () => {
    const markdownText = document.body.textContent;
    const htmlOutput = marked(markdownText);
    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = htmlOutput;
    contentDiv.style.display = 'block';
});
```

`esbuild` it with this command and then your website should now have a functional wiki!
`npx esbuild ./webapp/markdown-renderer.js --bundle --minify --sourcemap --outfile=./lab2/wiki/static/markdown-renderer.min.js`

## Serving Static Files with Whitenoise

Now that we have a Django app with Markdown editing and content storage, we need to configure our static hosting middleware. In a production environment, Django will not export static files which is why we need to use a static middleware. Changing the `DEBUG` variable in `lab2/settings.py` to `False`, running `python3 manage.py runserver`, and then navigating to `localhost:8000/wiki/add/` will not allow you to preview any markdown code. We can use **Whitenoise** (a static file middleware) to resolve this. You can learn more about [Whitenoise here](https://whitenoise.readthedocs.io/en/latest/django.html). 

1. Install Whitenoise:
```
pip install whitenoise
```

2. Navigate to the root directory in your repository and add Whitenoise to your `requirements.txt`
```
pip freeze requirements.txt
```

2. Update `lab2/settings.py` to use Whitenoise:

```py
MIDDLEWARE = [
    # ...
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # MAKE SURE IT'S AFTER THE SECURITY MIDDLEWARE!
    # ...
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

3. Run `collectstatic` to gather all static files:
```py
python manage.py collectstatic
```

4. Restart the Django server, and now Whitenoise will handle serving static files, including the JavaScript bundles.

## TASK - Emoji Picker

Add a new file to `webapp` called `emoji-editor.js` and paste the following code in it:
```js
import { Picker } from "emoji-mart"; // Import the emoji picker

const pickerOptions = { onEmojiSelect: (emoji) => {
  const textarea = document.getElementById('markdown-editor');
  textarea.value += emoji.native; // Add selected emoji to the editor
}};
const picker = new Picker(pickerOptions);
document.getElementById('emoji-picker').appendChild(picker); // Add emoji picker to the DOM
```

Navigate to the root directory in your repository and then install `emoji-mart` from npm.
```bash
npm install --save-dev emoji-mart
```

Update `wiki/templates/editor.html` to the following:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>New Wiki Page</title>
</head>
<body>
    <h1>Welcome to the Wiki App!</h1>

    <div id="emoji-picker"></div>
    <br>

    <form id="save-form" method="POST" action="/wiki/save/">
        <input type="text" name="title" id="page-title" placeholder="Page Title"><br>
        <textarea id="markdown-editor" name="content" rows="10" cols="50"></textarea><br>
        <button id="convert-btn">Convert to HTML</button><br>
        <br>
        <button id="save-btn" type="submit">Save Page</button>
        {% csrf_token %}
    </form>

    <h3>Output</h3>
    <div id="markdown-output"></div> <!-- Rendered HTML output -->
    
    <script src="{% static 'markdown-editor.min.js' %}"></script>
    <script src="{% static 'emoji-editor.min.js' %}"></script>
</body>
</html>
```

**Your task** is to esbuild `emoji-editor.js` into `wiki/static/emoji-editor.min.js`. After esbuilding, Check `localhost:8000/wiki/add/` to confirm that there is a working emoji picker.

## TASK - Adding Likes

Update `wiki/templates/page.html` to the following:
```html
{% load static %}
<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body> 
        <div>
            <form action="/wiki/page/{{ id }}/like/" method="POST">
                <input type="submit" value="Like Post ({{ like_count }} likes)" />
                {% csrf_token %}
            </form>
        </div>
        <br>
        <div id="content" style="display: none;">{{ content }}</div>
        <div>
            <a href="/wiki/">&lt; Go Back</a>
        </div>
    </body>
    <script src="{% static 'markdown-renderer.min.js' %}"></script> <!-- Load bundled JS -->
</html>
```

**Your task** is to update the backend code to store likes and when each like was created. It should pass a `like_count` to the context dictionary when calling `render` in the `view_page` view. The route and logic to add a like should be accessible when a POST request is sent to `/wiki/page/<id>/like/`. After liking the page, it must redirect to the same wiki page.

## TASK - Displaying Likes

Add a new file in `wiki/templates/` called `likes.html` and paste in the following:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }} | Likes</title>
    </head>
    <body>
        <h1>Likes for {{ title }}</h1>
        <ol>
            {% for like_date in likes %}
                <li>{{ like_date }}</li>
            {% endfor %}
        </ol>
        <br>
        <a href="/wiki/page/{{ id }}/">&lt; Go Back</a>
    </body>
</html>
```

Replace the contents of `wiki/templates/page.html` with
```html
{% load static %}
<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body> 
        <div>
            <form action="/wiki/page/{{ id }}/like/" method="POST">
                <input type="submit" value="Like Post ({{ like_count }} likes)" /><br><br>
                <a href="/wiki/page/{{ id }}/likes/">View All Likes</a>
                {% csrf_token %}
            </form>
           
        </div>
        <br>
        <div id="content" style="display: none;">{{ content }}</div>
        <div>
            <a href="/wiki/">&lt; Go Back</a>
        </div>
    </body>
    <script src="{% static 'markdown-renderer.min.js' %}"></script> <!-- Load bundled JS -->
</html>
```

**Your task** is to render a list of every single like a specific wiki page recieved and when they were created. This route should be accessible at `/wiki/page/<id>/likes/`, and it should render the `likes.html` template.

When rendering the `likes.html` template, you will need to pass in to the context argument the following:
```json
{
    "id": 0,        // id of the wiki page
    "title": "",    // title of the wiki page,
    "likes": []     // list of STRING representations of the date of each like that was received for this specific wiki page
}
```

## Requirements

* Must use Python3
* Must run on Ubuntu (Use the undergrad lab machines, for example the ones in CSC 2-29 or install an Ubuntu VM to check this)
* A working Django 5 application
    * using the latest Django version from pypi
        * downloaded with pip into a virtualenv
    * with a wiki homepage that displays all wiki pages created at `/wiki/`
    * with a wiki page creation page at `/wiki/add/`
        * must have a markdown editor and emoji picker
        * must have used esbuild to compile the markdown editor/emoji picker into the code
        * when saving a wiki page, it should make a POST Request to `/wiki/save/` and then redirect to `/wiki/`
    * with individual wiki pages that display their respective content in markdown at `/wiki/page/<id>/`
        * must have the functionality to add a like to a wiki page when a POST request is sent to `/wiki/page/<id>/like/`
            * must redirect to the same wiki page that was liked
        * must have a likes list page that shows when each like for that specific page was created at `/wiki/page/<id>/likes/`
    * using Django's ORM system to store wiki pages and likes
    * with correctly setup Whitenoise middleware
* A git repository that does not contain built (compiled, transpiled, bundled) or downloaded artifacts, including but not limited to:
    * `virtualenv` `venv` etc.
    * `.pyc` files, `__pycache__` directories.
    * `node_modules`
    * `*.min.js`
    * `*.min.js.map`
    * `db.sqlite3` or any other databases.
        * `db.sqlite3` *should never leave your computer.* It is for local development only.
* Your git repository SHOULD contain:
    * The code you worked on during the lab.

## Conclusion and Submission

At the end of this lab, you will have built a fully functioning web app with the following features:
- An emoji picker using the `emoji-mart` npm package.
- A Markdown editor where users can write content and convert it to HTML.
- Content storage in a Django model using the ORM.
- A working wiki website
- A working like system for each wiki page
- Efficient serving of static files with Whitenoise.

Please confirm you have completed **the four tasks** in this lab.
- Creating the backend for storing wiki pages
- Adding an emoji picker to the markdown editor
- Adding support for liking wiki pages
- Adding support for viewing all of the likes a wiki page received (and when they were created)

### Submission Instructions
1. Push your code to GitHub Classroom **before the deadline**.
2. Ensure your repository contains only the necessary files, and your `.gitignore` excludes built files (`venv/`, `node_modules/`, `*.min.js`, `*.min.js.map`, `db.sqlite3`, etc).

Submit your repository link on eClass.

---

### Further Tips
- If you encounter issues with static files, ensure your file paths are correct and that Django’s `STATIC_URL` is configured properly.
- For more detailed error handling or improving the user interface, consider adding feedback when content is saved or emoji selection is confirmed.
- Consult the [Django Documentation](https://docs.djangoproject.com/en/5.1/).
