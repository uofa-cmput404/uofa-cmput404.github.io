Title: Django Lab
date: 2024-09-05
tags: labs
authors: Alireza Azimi, Mo Adel Abdelghany
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

The purpose of this lab is to familiarize you with setting up a virtual environment, developing with Django, and using npm to incorporate external packages like an emoji picker and a markdown editor. By the end of this lab, you will build a simple web app where users can add emojis and edit content using Markdown.

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
python3.11 -m virtualenv --help
```

Either `venv` or `virtualenv` will work. 

If you don't have either, install `virtualenv` using pip.

```bash
python -m pip install --user virtualenv
```

### Create Virtual Environment

Run `venv` or `virtualenv` and tell it to create a virtual environment directory, called `venv`.

Note the first `venv` or `virtualenv` is the name of the Python module.
The second `venv` is the name of a directory (folder) you'd like it to create.

```bash
python -m venv venv
# or
python -m virtualenv venv
```

### Activate Virtual Environment:

To activate the virtual environment:

```bash
source venv/bin/activate
```

## Installing Node.js and npm

To install Node.js, download the LTS version from the [Node.js website](https://nodejs.org/en/download). The installation will include npm as well, which we will use to manage JavaScript packages.

---

# Lab Instructions

## Django Setup

We will use [Django](https://www.djangoproject.com/), a high-level Python web framework. It simplifies web development by providing a built-in ORM, an admin panel, and much more. The [official documentation](https://docs.djangoproject.com/en/5.0/) is a valuable resource.

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

We will create a Django webapp called `emojis` to build a simple emoji picker app.

1. Create a new app:
   ```
   python manage.py startapp emojis
   ```

2. In `emojis/views.py`, add the following code:

   ```
   from django.http import HttpResponse

   def index(request):
       return HttpResponse("This is the emoji app.") #
   ```

3. Create a `urls.py` file inside `emojis` and add the following code:
   
   ```
   from django.urls import path
   from . import views

   urlpatterns = [
       path("", views.index, name="index"),
   ]
   ```

4. Update `lab2/urls.py` to include the new app:

   ```
   from django.urls import include, path
   urlpatterns = [
       path("emojis/", include("emojis.urls")),
       path("admin/", admin.site.urls),
   ]
   ```



## Adding HTML Templates

Django allows you to render HTML templates. Let’s create an HTML page to display the emoji picker.

1. Inside the `emojis` directory, create a `templates` directory.
2. Inside `templates`, create an `index.html` file with the following boilerplate:
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
   

3. Update `emojis/views.py` to render the template:
   ``` 
   from django.shortcuts import render

   def index(request):
       return render(request, "index.html")
   ```

Now, visiting `localhost:8000/emojis` will display the HTML template.

---

## Adding Markdown Editor

In this section, we will integrate a **Markdown editor** so that users can write content in Markdown format and see it rendered as HTML in the browser. We'll use the popular npm package `marked` for parsing Markdown content and converting it to HTML.

### Steps to Add the Markdown Editor:

1. Install the `marked` package using npm:
   ```bash
   npm install --save-dev marked
   ```

2. Update your `main.js` file to incorporate both the Markdown editor and the emoji picker:

```js
import { Picker } from "emoji-mart"; // Import the emoji picker
import { marked } from "marked"; // Import the markdown converter

// Set up emoji picker
const pickerOptions = { onEmojiSelect: (emoji) => {
  const textarea = document.getElementById('markdown-editor');
  textarea.value += emoji.native; // Add selected emoji to the editor
}};
const picker = new Picker(pickerOptions);
document.getElementById('emoji-picker').appendChild(picker); // Add emoji picker to the DOM

// Handle Markdown conversion and rendering
document.getElementById('convert-btn').addEventListener('click', () => {
  const markdownText = document.getElementById('markdown-editor').value;
  const htmlOutput = marked(markdownText); // Convert markdown to HTML
  document.getElementById('markdown-output').innerHTML = htmlOutput; // Display HTML content
});
```

3. Modify your `index.html` file to include both the Markdown editor and the emoji picker:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Markdown and Emoji App</title>
</head>
<body>
    <h1>Welcome to the Markdown and Emoji App!</h1>
    
    <div id="emoji-picker"></div> <!-- Emoji Picker -->

    <div>
        <h3>Markdown Editor</h3>
        <textarea id="markdown-editor" rows="10" cols="50" placeholder="Write in Markdown..."></textarea>
        <button id="convert-btn">Convert to HTML</button>
    </div>

    <h3>Output</h3>
    <div id="markdown-output"></div> <!-- Rendered HTML output -->
    


    <script src="{% static 'main.min.js' %}"></script> <!-- Load bundled JS -->
</body>
</html>
```

4. Bundle the `main.js` file again using esbuild:

```bash
npx esbuild main.js --bundle --minify --sourcemap --outfile=./emojis/static/main.min.js
```

---

## Integrating with Django Models (ORM)

Now that we have a Markdown editor and emoji picker set up, let’s store the content users create in a Django model.

1. Update `emojis/models.py` to create a model for storing user-created pages:

```python
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Markdown content
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

2. In `emojis/views.py`, create a new view to handle saving the Markdown content to the database:

```python
from django.shortcuts import render
from django.http import JsonResponse
from .models import Page

def index(request):
    return render(request, "index.html")

def save_page(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Untitled')
        content = request.POST.get('content', '')
        Page.objects.create(title=title, content=content)
        return JsonResponse({'status': 'success'})
```

3. In `emojis/urls.py`, add the new route for saving content:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save/", views.save_page, name="save_page"),
]
```

4. Modify the HTML form in `index.html` to send data to the server and save the page:

```html
<form id="save-form" method="POST">
    <input type="text" name="title" id="page-title" placeholder="Page Title">
    <textarea id="markdown-editor" name="content" rows="10" cols="50"></textarea>
    <button id="save-btn" type="submit">Save Page</button>
</form>
```

5. In `main.js`, handle the form submission using JavaScript and send the content via a POST request:

```js
document.getElementById('save-btn').addEventListener('click', function(e) {
    e.preventDefault();

    const title = document.getElementById('page-title').value;
    const content = document.getElementById('markdown-editor').value;

    fetch('/save/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') //  CSRF token
        },
        body: JSON.stringify({title: title, content: content})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response from the server
    });
});
```

---

## Serving Static Files with Whitenoise

Now that we have a Django app with Markdown editing, emoji picking, and content storage, we need to serve static files efficiently. We'll use **Whitenoise** for this.

1. Install Whitenoise:
   ```
   pip install whitenoise
   ```

2. Update `settings.py` to use Whitenoise:

```
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # line for middleware
    # other middleware...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

3. Run `collectstatic` to gather all static files:
   ```
   python manage.py collectstatic
   ```

4. Restart the Django server, and now Whitenoise will handle serving static files, including the JavaScript bundle.

---

## Conclusion and Submission

At the end of this lab, you will have built a fully functioning web app with the following features:
- An emoji picker using the `emoji-mart` npm package.
- A Markdown editor where users can write content and convert it to HTML.
- Content storage in a Django model using the ORM.
- Efficient serving of static files with Whitenoise.

### Submission Instructions
1. Push your code to GitHub Classroom **before the deadline**.
2. Ensure your repository contains only the necessary files, and your `.gitignore` excludes built files (`venv/`, `node_modules/`, `main.min.js`).

Submit your repository link on eClass.

---

### Further Tips
- If you encounter issues with static files, ensure your file paths are correct and that Django’s `STATIC_URL` is configured properly.
- For more detailed error handling or improving the user interface, consider adding feedback when content is saved or emoji selection is confirmed.
