Title: Django Lab
date: 2026-09-09
tags: labs
authors: Alireza Azimi, Mo Adel Abdelghany, William Qi, Kalvin Eng
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking
----

[TOC]

---

# Description

The purpose of this lab is to familiarize you with setting up a virtual environment, developing with Django, and using NPM to incorporate external packages like an emoji picker and a markdown editor. By the end of this lab, you will build a simple wiki app where users can add emojis, likes, and edit content using Markdown.

### Expected Outcomes

By the end of this lab, your web application will include:

- An emoji picker using the `emoji-mart` NPM package.
- A Markdown editor where users can write content and convert it to HTML.
- Content storage in a Django model using the ORM.
- A working wiki website.
- A working like system for each wiki page.
- Efficient serving of static files with WhiteNoise.

---

# Getting Started

<details markdown="1">
<summary><b>Click to expand/collapse setup instructions</b></summary>

## 1. Environment & Prerequisites

[Make sure you have a working development environment with these instructions!]({filename}/general/environment.md)

<details markdown="1">
<summary><b>Refresher: Introduction to HTML & JavaScript (Click to Expand)</b></summary>

Before diving into Django and NPM, let’s go over some basics of HTML and JavaScript.

### HTML Basics
HTML is the structure of a webpage. It defines elements such as **headings** (`<h1>`, `<h2>`, etc.), **paragraphs** (`<p>`), and **divs** (`<div>`) to organize content.

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
</details>

---

## 2. Prepare your Repo

1. Get the GitHub classroom link from Canvas, create your assignment, and clone it.
2. Create an appropriate `.gitignore` file in the root of your repository folder to prevent unwanted files from being committed.

<div class="longInfo">
  <p>
    You can combine
    <a href="https://github.com/github/gitignore/blob/main/Python.gitignore">Python.gitignore</a>,
    <a href="https://github.com/github/gitignore/blob/main/Node.gitignore">Node.gitignore</a>,
    and
    <a href="https://github.com/django/django/blob/main/.gitignore">Django.gitignore</a>.
  </p>

  <p>
    Use <code>git status</code> to ensure you're not staging unwanted files
    before committing.
  </p>
</div>


---

## 3. Create the Virtual Environment

A virtual environment manages Python dependencies specific to your project independently. Each project may have different requirements, and a virtual environment helps you manage these dependencies independently.

<div class="longInfo">
  <p>
    <strong>Windows Users Note:</strong>
    The commands below assume Linux or macOS. On Windows, we strongly recommend
    using WSL2 to run Ubuntu in a VM. Follow
    <a href="{filename}/general/environment.md#ubuntu-on-windows">
      these Ubuntu on Windows instructions
    </a>.
  </p>
</div>


### Check Python Version

Check your Python version:

```bash
python3 --version

```

If you have multiple versions of Python installed, always specify the version number.
For example, on the lab machines there are multiple versions of Python installed. We can see for ourselves on the lab machines with these commands:

```txt
hazelcam@innisfree:~> python --version
Python 2.7.18
hazelcam@innisfree:~> python3 --version
Python 3.8.10
hazelcam@innisfree:~> python3.12 --version
Python 3.12.11

```

*To run Python 3.12 on lab machines, execute commands using `python3.12` instead of `python3` or `python`.*

### Check & Install `venv` / `virtualenv`

Check if `venv` or `virtualenv` is available:

```bash
python -m venv --help
python -m virtualenv --help

```

If missing, install `virtualenv` via pip:

```bash
python -m pip install --user virtualenv

```

### Create and Activate Virtual Environment

Create the directory named `venv` with the following commands:

```txt
python -m venv venv
# or
python -m virtualenv venv

```
Note the first `venv` or `virtualenv` is the name of the Python module.
The second `venv` is the name of a directory (folder) you'd like it to create.

Activate the environment:

```bash
source venv/bin/activate

```

When active, your prompt will show `(venv)`:

```txt
hazelcam@innisfree:~> source venv/bin/activate
(venv) hazelcam@innisfree:~>

```

<p class="warning">Remember to never commit your virtual environment directory (folder) to git.
Make sure it is listed in the <code>.gitignore</code>.
</p>

---

## 4. Install Node.js & NPM

Download and install the LTS version from the [Node.js website](https://nodejs.org/en/download). The installation will include NPM as well, which we will use to manage JavaScript packages.
</details>

---

# Lab Instructions

## Django Setup

We will use [Django](https://www.djangoproject.com/), a high-level Python web framework. It simplifies web development by providing a built-in ORM, an admin panel, and much more. The [official documentation](https://docs.djangoproject.com/en/6.1/) is a valuable resource, and **you will find it very helpful** to reference it during this lab for anything that is unclear.
### Install Django

With your virtual environment activated, run the following commands:

```bash
echo "Django>=6" > requirements.txt
python -m pip install -r requirements.txt

```

<div class="longInfo pad-y">
  <p>
    If you are encountering an issue with this command in regards to a library called `html5lib` you will need to update your pip version first.
  </p>

  <pre><code>wget https://bootstrap.pypa.io/get-pip.py -O ./get-pip.py
python3.12 ./get-pip.py</code></pre>
</div>


### Ubuntu VM / WSL Networking Note

If using WSL or a VM (such as UTM), access your server via the VM's internal IP address instead of `localhost` or `127.0.0.1`. Find your IP using `ip addr show`:

```txt
hazelcam@Roxanne:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:8c:d5:00 brd ff:ff:ff:ff:ff:ff
    inet 172.23.110.83/20 brd 172.23.111.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fe8c:d500/64 scope link
       valid_lft forever preferred_lft forever
```

In this case the VM's address is `172.23.110.83`.
So later when I want to see my Django site,
I will need to put `http://172.23.110.83:8000/` into my browser, instead of `localhost`.

---

### Optional Django Warm-Up

Follow the official [Django Tutorial](https://docs.djangoproject.com/en/6.1/intro/tutorial01/) (not graded).

---

### Start a New Django Project

From the **root directory** of your repository:

```bash
django-admin startproject lab1-project lab1
cd lab1
python manage.py runserver 0.0.0.0:8000

```
The command above creates a directory `lab1` with a project called `lab1-project`.
By using `cd lab1` you are changing directory to the `lab1` directory.
`python manage.py runserver 0.0.0.0:8000` starts a test web server to serve the Django project.

Visiting `http://localhost:8000` in your browser should now display Django's "Congratulations!" landing page.

---

### Creating a Django Webapp

We will create a Django webapp called `wiki` to build a simple wiki app.

From inside the `lab1` directory:

1\. **Create the app:**
```bash
python manage.py startapp wiki

```


2\. **Register your new wiki app to Django in `lab1-project/settings.py`:**
```python
INSTALLED_APPS = [
    'wiki',  # Add this line
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```


3\. **Add index request handling logic in `wiki/views.py`:**
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the wiki app.")

```


4\. **Create `wiki/urls.py` to manage how app can be accessed from the browser via url:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]

```


5\. **Update the project root url handling in `lab1-project/urls.py`:**
```python
from django.urls import include, path

urlpatterns = [
    path("wiki/", include("wiki.urls")),
    path("admin/", admin.site.urls),
]

```



---

## Adding HTML Templates

Django allows you to render HTML templates. Let’s create an HTML page to display a homepage.

Working from inside the `lab1` directory:

1\. Create a new `templates` directory inside the `wiki` directory, the structure should be `wiki/templates/`.

2\. Inside the `templates` directory, create an `index.html` file with the following boilerplate:
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
```python
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

```



Now when you visit `http://localhost:8000/wiki/`, it will render the HTML template you just created.

---

## Adding Markdown Editor

In this section, we will integrate a **Markdown editor** so that users can write content in Markdown format and see it rendered as HTML in the browser. We'll use the popular NPM package `marked` for parsing Markdown content and converting it to HTML. This involves bundling the package into a minified file that will be served by the Django app.

### 1. Install & Bundle JS

Run from the **root directory** of your repository:

```bash
npm install --save-dev marked
npm install --save-dev esbuild

```
This will install the `marked` and `esbuild` into the `node_modules` folder in your root directory.

Create a new folder `webapp/` at root and create a `webapp/markdown-editor.js` within it with the following code:

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

```bash
npx esbuild ./webapp/markdown-editor.js --bundle --minify --sourcemap --outfile=./lab1/wiki/static/markdown-editor.min.js

```

This command bundles your `markdown-editor.js` file and all the imports that it needs into one huge file called `markdown-editor.min.js`. It is now ready to be included into your Django application!

---

### 2. Django Template & View Integration

While we do have the JavaScript for our markdown editor, we still need the HTML for the editor!

Create a new HTML file `lab1/wiki/templates/editor.html` and add the following content:

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

Add a new view function that will render this template in `wiki/views.py`:

```python
def editor(request):
    return render(request, "editor.html")

```

In `wiki/urls.py`, add the new route for our markdown editor:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.editor, name="add"),
]

```

If you navigate to `localhost:8000/wiki/add/` you should see your markdown editor!

Examples of how to use markdown can be found [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) if you would like to test it out yourself.

We now have a visible markdown editor, but we have no way of actually storing data yet. So let’s store the content users create in a Django model.

---

### 3. Create Wiki Page Model

Update `wiki/models.py` to create a model for storing user-created pages:

```python
from django.db import models

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()  # Stores raw Markdown
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.id} - {self.title}"

```

After creating the model, the changes to the database are not automatically applied. You will have to manually apply database migrations:

```bash
python3.12 manage.py makemigrations
python3.12 manage.py migrate

```

---

<div class="longTaskbox" id="task1">
  <p><strong>TASK 1: Backend for Storing Wiki Pages</strong></p>

  <ol>
    <li>
      Replace the contents of <code>wiki/templates/editor.html</code> with:
      <pre><code>{% load static %}
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;New Wiki Page&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Welcome to the Wiki App!&lt;/h1&gt;

    &lt;form id="save-form" method="POST" action="/wiki/save/"&gt;
        &lt;input type="text" name="title" id="page-title" placeholder="Page Title"&gt;&lt;br&gt;
        &lt;textarea id="markdown-editor" name="content" rows="10" cols="50"&gt;&lt;/textarea&gt;&lt;br&gt;
        &lt;button id="convert-btn"&gt;Convert to HTML&lt;/button&gt;&lt;br&gt;
        &lt;br&gt;
        &lt;button id="save-btn" type="submit"&gt;Save Page&lt;/button&gt;
        {% csrf_token %}
    &lt;/form&gt;

    &lt;h3&gt;Output&lt;/h3&gt;
    &lt;div id="markdown-output"&gt;&lt;/div&gt; &lt;!-- Rendered HTML output --&gt;

    &lt;script src="{% static 'markdown-editor.min.js' %}"&gt;&lt;/script&gt; &lt;!-- Load bundled JS --&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
    </li>

    <li>
      Create the backend view logic to handle forms submitted via
      <strong><code>POST /wiki/save/</code></strong>.
    </li>

    <li>
      It <strong>MUST</strong> save the incoming data using the <code>Page</code> model created above.
    </li>

    <li>
      It <strong>MUST</strong> redirect the request to <strong><code>/wiki/</code></strong> after saving the page.
    </li>
  </ol>
</div>


---

## Displaying Wiki Pages

While it's great that we can store wiki pages, we need a way to access them ourselves.

### 1. Update Homepage Template & Views

Replace `wiki/templates/index.html` with the following code snippet:

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

```python
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

Modify `wiki/urls.py` to include our new view function:

```python
path("page/<int:id>/", views.view_page, name="view")

```

---

### 2. Client-Side Wiki Page Rendering Setup

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

In the `webapp` folder that houses you markdown editor javascript code, create a new file called `markdown-renderer.js` and paste the following snippet in:

```javascript
import { marked } from "marked"; // Import the markdown converter

// Handle rendering
window.addEventListener('load', () => {
    const markdownText = document.getElementById('content').innerHTML;
    const htmlOutput = marked(markdownText);
    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = htmlOutput;
    contentDiv.style.display = 'block';
});
```

Use `esbuild` to transpile it with this command:
```bash
npx esbuild ./webapp/markdown-renderer.js --bundle --minify --sourcemap --outfile=./lab1/wiki/static/markdown-renderer.min.js

```

Your website should now have a functional wiki!

---

## Serving Static Files with WhiteNoise

Now that we have a Django app with Markdown editing and content storage, we need to configure our static hosting middleware. In a production environment, Django will not serve static files which is why we need to use a static file middleware such as **WhiteNoise** to resolve this. You can learn more about [WhiteNoise here](https://whitenoise.readthedocs.io/en/latest/django.html). 

To simulate a production environment for testing, you can change the `DEBUG` variable in `settings.py`. To do so, assume that you are in your Django `lab1` directory, and not your repository root directory. By changing the `DEBUG` variable in `lab1-project/settings.py` to `False`, running `python3 manage.py runserver`, and then navigating to `localhost:8000/wiki/add/` will not allow you to preview any Markdown code. 

<div class="longInfo">
<p>
  Note that you will also have to update
  <code>ALLOWED_HOSTS</code> to <code>['*']</code> if you would like to see it
  yourself, as Django in production mode restricts the host/domain a site can
  be served to.
</p>
</div>


1\. **Install WhiteNoise:**
```bash
pip install whitenoise

```


2\. Navigate to the root directory in your repository and add WhiteNoise to your `requirements.txt`
```bash
pip freeze > requirements.txt

```


3\. **Configure your project `lab1-project/settings.py` to use WhiteNoise:**
```python
MIDDLEWARE = [
    # ...
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # MAKE SURE IT'S AFTER THE SECURITY MIDDLEWARE!
    # ...
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

```


4. **Gather All Static Files for Django Project:**
```bash
python manage.py collectstatic

```


5. Restart your Django development server in production mode, , and now WhiteNoise will handle serving static files, including the JavaScript bundles.

---

<div class="longTaskbox" id="task2">
  <p><strong>TASK 2: Emoji Picker</strong></p>

  <p>
    Add a new file to <code>webapp</code> called
    <code>emoji-editor.js</code> and paste the following code into it:
  </p>

  <pre><code>import { Picker } from "emoji-mart"; // Import the emoji picker

const pickerOptions = { onEmojiSelect: (emoji) =&gt; {
  const textarea = document.getElementById('markdown-editor');
  textarea.value += emoji.native; // Add selected emoji to the editor
}};
const picker = new Picker(pickerOptions);
document.getElementById('emoji-picker').appendChild(picker); // Add emoji picker to the DOM</code></pre>

  <p>
    Navigate to the root directory in your repository and install
    <code>emoji-mart</code> from NPM:
  </p>

  <pre><code>npm install --save-dev emoji-mart</code></pre>

  <p>
    Update <code>wiki/templates/editor.html</code> to the following:
  </p>

  <pre><code>{% load static %}
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;New Wiki Page&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Welcome to the Wiki App!&lt;/h1&gt;

    &lt;div id="emoji-picker"&gt;&lt;/div&gt;
    &lt;br&gt;

    &lt;form id="save-form" method="POST" action="/wiki/save/"&gt;
        &lt;input type="text" name="title" id="page-title" placeholder="Page Title"&gt;&lt;br&gt;
        &lt;textarea id="markdown-editor" name="content" rows="10" cols="50"&gt;&lt;/textarea&gt;&lt;br&gt;
        &lt;button id="convert-btn"&gt;Convert to HTML&lt;/button&gt;&lt;br&gt;
        &lt;br&gt;
        &lt;button id="save-btn" type="submit"&gt;Save Page&lt;/button&gt;
        {% csrf_token %}
    &lt;/form&gt;

    &lt;h3&gt;Output&lt;/h3&gt;
    &lt;div id="markdown-output"&gt;&lt;/div&gt; &lt;!-- Rendered HTML output --&gt;

    &lt;script src="{% static 'markdown-editor.min.js' %}"&gt;&lt;/script&gt;
    &lt;script src="{% static 'emoji-editor.min.js' %}"&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>

  <p>
    Transpile <code>emoji-editor.js</code> into
    <code>wiki/static/emoji-editor.min.js</code> using
    <code>esbuild</code>. After bundling, visit
    <code>http://localhost:8000/wiki/add/</code> to confirm that the emoji
    picker works.
  </p>
</div>



---

<div class="longTaskbox" id="task3">
  <p><strong>TASK 3: Adding Likes</strong></p>

  <ol>
    <li>
    Replace the contents of <code>wiki/templates/page.html</code> with the following:
  <pre><code>{% load static %}
&lt;!DOCTYPE html&gt;
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;{{ title }}&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;div&gt;
            &lt;form action="/wiki/page/{{ id }}/like/" method="POST"&gt;
                &lt;input type="submit" value="Like Post ({{ like_count }} likes)" /&gt;&lt;br&gt;&lt;br&gt;
                &lt;a href="/wiki/page/{{ id }}/likes/"&gt;View All Likes&lt;/a&gt;
                {% csrf_token %}
            &lt;/form&gt;
        &lt;/div&gt;
        &lt;br&gt;
        &lt;div id="content" style="display: none;"&gt;{{ content }}&lt;/div&gt;
        &lt;div&gt;
            &lt;a href="/wiki/"&gt;&amp;lt; Go Back&lt;/a&gt;
        &lt;/div&gt;
    &lt;/body&gt;
    &lt;script src="{% static 'markdown-renderer.min.js' %}"&gt;&lt;/script&gt;
    &lt;!-- Load bundled JS --&gt;
&lt;/html&gt;</code></pre>
    </li>

    <li>
    Update the backend code to store likes and the time each like was created.
    Pass a <code>like_count</code> value to the context dictionary when calling
    <code>render</code> in the <code>view_page</code> view.
    </li>

    <li>
    Add a route and view that handle a <code>POST</code> request to
    <code>/wiki/page/&lt;id&gt;/like/</code>. After the page is liked, redirect
    the user back to the same wiki page.
    </li>

    <li>
    If you are unsure how to proceed, consult the Django Tutorial and the documentation linked above.
    </li>
   </ol>
</div>


---

<div class="longTaskbox" id="task4">
  <p><strong>TASK 4: Displaying Likes</strong></p>
  <p>
  Render a list of every like received by a specific wiki page, including the
  date and time when each like was created. The route must be accessible at
  <code>/wiki/page/&lt;id&gt;/likes/</code> and must render the
  <code>likes.html</code> template.
</p>

  <ol>
    <li>
      Add a new file in <code>wiki/templates/</code> called
      <code>likes.html</code> and paste in the following:

      <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;{{ title }} | Likes&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;Likes for {{ title }}&lt;/h1&gt;
        &lt;ol&gt;
            {% for like_date in likes %}
                &lt;li&gt;{{ like_date }}&lt;/li&gt;
            {% endfor %}
        &lt;/ol&gt;
        &lt;br&gt;
        &lt;a href="/wiki/page/{{ id }}/"&gt;&amp;lt; Go Back&lt;/a&gt;
    &lt;/body&gt;
&lt;/html&gt;</code></pre>
    </li>

    <li>
      Replace the contents of <code>wiki/templates/page.html</code> with:

      <pre><code>{% load static %}
&lt;!DOCTYPE html&gt;
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;{{ title }}&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;div&gt;
            &lt;form action="/wiki/page/{{ id }}/like/" method="POST"&gt;
                &lt;input type="submit" value="Like Post ({{ like_count }} likes)" /&gt;&lt;br&gt;&lt;br&gt;
                &lt;a href="/wiki/page/{{ id }}/likes/"&gt;View All Likes&lt;/a&gt;
                {% csrf_token %}
            &lt;/form&gt;
        &lt;/div&gt;
        &lt;br&gt;
        &lt;div id="content" style="display: none;"&gt;{{ content }}&lt;/div&gt;
        &lt;div&gt;
            &lt;a href="/wiki/"&gt;&amp;lt; Go Back&lt;/a&gt;
        &lt;/div&gt;
    &lt;/body&gt;
    &lt;script src="{% static 'markdown-renderer.min.js' %}"&gt;&lt;/script&gt; &lt;!-- Load bundled JS --&gt;
&lt;/html&gt;</code></pre>
    </li>

    <li>
      Add a route accessible at
      <code>/wiki/page/&lt;id&gt;/likes/</code> that renders the
      <code>likes.html</code> template.
    </li>

    <li>
      Update the backend logic to retrieve every like for the specified wiki
      page, including the date and time when each like was created.
    </li>

    <li>
      When rendering the <code>likes.html</code> template, pass the following values to the <code>likes.html</code> template context:

      <pre><code>{
    "id": 0,
    "title": "",
    "likes": []
}</code></pre>

      <ul>
        <li><code>id</code>: The ID of the wiki page.</li>
        <li><code>title</code>: The title of the wiki page.</li>
        <li>
          <code>likes</code>: A list of STRING representations of the dates
          when likes were received for this specific wiki page.
        </li>
      </ul>
    </li>
  </ol>
</div>


---

## Cleaning Repository & `.gitignore` Guidelines

Generally there are two kinds of files:

* Files which are rebuilt/generate/download with the standard build/deploy steps should NOT be in the repo and SHOULD be in `.gitignore`.
* Files which are modified by developer or only generated once (not every build/deploy) SHOULD be in the repo and should NOT be in `.gitignore`.

<details markdown="1">
<summary><strong>Click here to find a detailed explanation of what you should be ignoring</strong></summary>
The standard build/deploy steps for a C project would be something like `configure`, `make`, `make install`. For Java in CMPUT 301 that would be rebuilding from the IDE. For Django+NPM we have commands like `virtualenv venv`, `pip install -r requirements.txt`, `npm install` (with no arguments), `django-admin migrate` and `manage.py collectstatic`. 

Generally commands like `npm install --save-dev somedependency` modifies the `package.json` and `package.lock` files, so their results need to be committed, and they're only run once (not every time we build/deploy). The same thing applies to `django-admin makemigrations`, which generates the migrations files that are needed to migrate an old database schema. This allows the database to follow the model updates. They would not be necessary if you plan on deleting the entire database and its contents (all users, all posts...) every time you update your app, but usually you don't want to lose all of your users and content! Also, the migrations are different depending on when you run `makemigrations` (they are based on the previous migrations generated by previous `makemigrations`). Each migration is only generated once ever, so we should keep them in git.

It's not immediately clear whether the static files for the admin site should be committed or not, and it's not immediately clear to me either. However, the test remains the same: will a standard build/deploy command like `collectstatic` recreate them? If so, we should add them to `.gitignore` and remove them from our repository. So, if my `STATIC_ROOT` is set to `staticfiles` then `collectstatic` will create files such as `./staticfiles/admin/img/icon-no.svg`. And, if I delete it, and run `collectstatic` again, it reappears. So I should ignore `./staticfiles/admin/img/icon-no.svg` and remove it from my repository.

The database holds users and content (wiki pages people have made, posts, likes...). The users and content will be different on every different server, even if the source code is the same. Later, when we deploy to Heroku, we will have our local sqlite database, and our production postgres database (which is not held in a file) on Heroku. They will contain different users and content. The local sqlite database will contain testing data, and the production postgres database will contain production data. Our python source code should be the same on our local machine and a production webserver once we deploy. So, we **do** want the model source code in git, but we **do not** want the database in git. But we **do** want the migrations required to update the database to match the model in our source code.
</details>

Ensure you clean up build output before committing your repository. Below is a summary table of files and folders to keep/ignore.

| Ignore from Git (`.gitignore`) | Commit to Git Repository |
| --- | --- |
| Rebuilt/generated files (`venv/`, `node_modules/`) | Modified source files (`*.py`, `*.js`, `templates/`) |
| Compiled bundles (`*.min.js`, `*.min.js.map`) | Source dependencies list (`package.json`, `package-lock.json`) |
| Local database files (`db.sqlite3`) | Database migration files (`wiki/migrations/`) |
| Collected static assets (`staticfiles/`) | Raw configuration files (`settings.py`, `urls.py`) |

---

## Requirements

* Must use Python3.12+
* Must run on Ubuntu (Use the undergrad lab machines, for example the ones in UCommons 2030 or install an Ubuntu VM to check this)
* Must checkout the big hex commit (e.g. `git checkout 95df41a777e5a5b5cda1e5d6c38953d26549f702`) and successfully be able to run the app
* A working Django 6 application
    * using the latest Django version from [PyPI](https://pypi.org/)
        * downloaded with pip into a virtual environment
    * with a wiki homepage that displays all wiki pages created at `/wiki/`
    * with a wiki page creation page at `/wiki/add/`
        * must have a markdown editor and emoji picker
        * must have used `esbuild` to transpile the markdown editor/emoji picker into the code
        * when saving a wiki page, it should make a POST Request to `/wiki/save/` and then redirect to `/wiki/`
    * with individual wiki pages that display their respective content in Markdown at `/wiki/page/<id>/`
        * must have the functionality to add a like to a wiki page when a POST request is sent to `/wiki/page/<id>/like/`
            * must redirect back to the same wiki page that was liked
        * must have a likes list page that shows when each like for that specific page was created at `/wiki/page/<id>/likes/`
    * using Django's ORM system to store wiki pages and likes
    * with correctly setup WhiteNoise middleware
* A git repository that does not contain built (compiled, transpiled, bundled) or downloaded artifacts, including but not limited to:
    * `virtualenv` `venv` or other virtual environments, etc.
    * `.pyc` files, `__pycache__` directories.
    * `node_modules`
    * `*.min.js`
    * `*.min.js.map`
    * Databases like `db.sqlite3` or any other databases.
        * The `db.sqlite3` database *should never leave your computer.* It is for local development only.
* Your git repository SHOULD contain:
    * The code you worked on during the lab.

---

## Further Tips
- If you encounter issues with static files, ensure your file paths are correct and that Django’s `STATIC_URL` is configured properly.
- If you're still not seeing static files, did you run `python manage.py collectstatic`?
- Consult the [Django Documentation](https://docs.djangoproject.com/en/6.1/).

---

## Conclusion & Submission

Please confirm you have completed **the four tasks** in this lab and the [requirements](#requirements).

* [**Task 1:**](#task1) Creating the backend for storing wiki pages
* [**Task 2:**](#task2) Adding an emoji picker to the markdown editor
* [**Task 3:**](#task3) Adding support for liking wiki pages
* [**Task 4:**](#task4) Adding support for viewing all the likes a wiki page received (and when they were created)
* [**Clean Repo:**](#cleaning-repository-gitignore-guidelines) Ensure your repository contains only the necessary files, and your `.gitignore` excludes built files (`venv/`, `node_modules/`, `*.min.js`, `*.min.js.map`, `db.sqlite3`, etc).

### Submission Instructions

1. Push your final updates to your git repository **BEFORE the deadline**.
2. Submit a link to your repository in the form `https://github.com/uofa-cmput404/s25-labsignment-django-yourgithubname/commit/bunch-of-numbers` on Canvas. When you click the link you should see the files that were changed in the commit. **Do not** submit a link to a branch, a file, or the clone URL.

You can submit and then resubmit as many times as you want before the deadline, so submit early and often.

* Refer to [How to avoid Force Push & Rebase]({filename}/general/dontforcepush.md) if needed.

<div class="warning pad-y">If you do not submit a link to your COMMIT on Canvas on time using the correct format in step 2 above, you will get a zero.</div>

<div class="longInfo pad-y">
  <p>
    <strong>Important:</strong>
    Do not leave additional comments on Canvas. Any comments made on the
    submission after the due date will be removed.
  </p>

  <p>
    Any submission attempt that abuses Canvas by adding a comment containing
    your repository link after the due date will also be removed.
  </p>

  <p>
    If you have a question about your grade, do not comment on the canvas assignment page. Instead, use
    the instructor contact form on the website's help page within 10 days of
    receiving your marks back. TAs are not allowed to change grades.
  </p>
</div>

