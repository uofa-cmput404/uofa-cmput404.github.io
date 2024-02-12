Title: Flask and AJAX Lab
date: 2024-02-07
tags: labs
authors: Hazel Campbell
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking
----

[TOC]

# Description

Your task is to build a live, collaborative outline editing service.

# Getting Started

1. Get the github classroom link from eClass and clone it.
2. Use virtualenv/pip to install flask.
3. Create an appropriate `.gitignore` file to prevent unwanted files from being added to your repository.
3. Follow the first steps of the [Flask Quickstart guide](https://flask.palletsprojects.com/en/latest/quickstart/): "A Minimal Application". 
    * Name your app `outliner.py`.

In order to connect to your flask server inside WSL or another VM from outside WSL/VM, use `flask --app outliner run --host 0.0.0.0 --debug`.

# User Stories

* As a user, I want to add items to any existing item in the outline, so I can grow my outline.
* As a user, I want to edit items in the outline, so I can update my outline.
* As a user, I want to delete items from the outline, becuase I don't want them anymore.
* As a user, I want the outline to remember the order of outline items, because the order is important to me.
* As a user, I want my friend to be able to edit the same outline that I am editing, so that we can collaborate.
* As a user, I want to see what my friends are typing in my outline while they type it, so I can be up to date.
* As a user, I want my outline to have a single root item, so I can name my outline.

#  Lab Instructions

## Have Flask Serve Files

* Flask should serve the `ui.html` file at path `/`.
* Flask should serve the `style.css` file at path `/style.css`.
* Flask should serve the `main.js` file at path `/main.js`.
* Flask should serve the `favicon.ico` file at path `favicon.ico`.

You will need to send the correct Content-Type with each file. 
In flask you can do this by `from flask import Response` then returning from your handler like:

```.py
    return Response(icon_bytes, mimetype='image/x-icon')
```

After this step is complete you should be able to view the HTML in the browser,
without getting errors in the browser.
Check the console to make sure you don't have any errors.

## Create Model Classes

Create model class(es) to represent the state of the outline and users.
Think about what you learned in CMPUT 301.

Your class for outline items must be nestable (a tree) so that any item in the outline can have items inside of it.
Each item needs to be able to store some text and sub-items.
Your code must remember which items go inside of other items, the order of the items, each authors color, and which item each author is editing.

It does not need to save this to a database or file, it's fine to just keep it in memory.

## Create API for Model

Each item in the outline and each author needs a URL in the Flask backend that is accessible by the JS frontend.

* `GET /outline/` should get a JSON respresentation of the root item.
* `GET /outline/1/2/3/` should get a JSON representation of the 3rd item in the 2nd item in 1st item in the root item.
* `POST /outline/4/` should create a new item inside of the 4th item inside of the root item.
    * It should return the appropriate HTTP status code, along with the JSON representation of the new item.
* `PUT /outline/5/6/` should modify the text of the 6th item inside of the 5th item inside of the outline.
    * It should return the appropriate HTTP status code.
    * It should return the new JSON representation of the 6th item inside of the 5th item inside of the outline.
* `DELETE /outline/7/` should delete the 7th item inside of the root item.\
    * It should return the appropriate HTTP status code.

In the JSON representation of the outline items, there must be an `id` key that gives the URL for the outline item.
For example, `GET /outline/8/9/` should return some JSON like:

```js
{
    url: '/outline/8/9`,
    text: 'text of the item',
    children: [
        '/outline/8/9/0',
        '/outline/8/9/1'
    ]
}
```

## Create the UI in JS

Create JS View and Controller classes to:

1. Remove the "Loading...".
    * **Hint:** Use `window.addEventListener('load', someFunction)` to run a function once the page has loaded.
2. Fill in the page.

**Hint:** Using proper OOAD will save you a lot of work. Apply the skills you learned in CMPUT 301.
I suggest making model proxy classes that are responsible for synchronizing with the model objects in the Flask backend,
by making calls using the Fetch API.

**Hint:** Using the "event.preventDefault();" on form `submit` events will prevent the browser from trying to submit the form,
so you can handle form submission in you custom JS code instead.

## Add polling

Add polling in your code to get live updates. 

Each time the outline is changed, record the URL of the changed item in a list.

Add an endpoint that can `GET` a list of updated items, with a `since` query parameter that takes a time.

Then, in your JS, use the list of updated items to request only the items changed since the last poll to update the UI.

# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* All of your Python code must be in `outliner.py`.
* All of your CSS code must be in `style.css`.
* All of your JS code must be in `main.js`.
* All of your HTML must be created dynamically using plain JS in `main.js`.
    * You must not modify `ui.html`.
    * `ui.html` must be the only HTML served by flask (on the route `/`).
* Using of any frontend frameworks, CSS libraries, JS libraries or frameworks is forbidden. 
  * You must write plain JS, CSS and HTML. 
  * You must not use JS libraries, frameworks, preprocessors, or transpilers.
  * You must not use CSS libraries, frameworks, preprocessors or transpilers.
  * You must not use frontend frameworks, HTML frameworks, preprocessors or transpilers. 
* If you borrow CSS from examples online, always cite the author, give the source URL, and the date you downloaded it.

