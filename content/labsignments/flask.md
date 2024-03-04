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

Create model class(es) to represent the state of the outline.
Think about what you learned in CMPUT 301.

Your class for outline items must be nestable (a tree) so that any item in the outline can have items inside of it.
Each item needs to be able to store some text and sub-items.
Your code must remember which items go inside of other items and the order of the items.

It does not need to save this to a database or file, it's fine to just keep it in memory.

## Create API for Model

Each item in the outline and each author needs a URL in the Flask backend that is accessible by the JS frontend.

* `GET /outline/` should get a JSON respresentation of the root item.
* `GET /outline/1/2/3/` should get a JSON representation of the 4th item in the 3rd item in 2nd item in the root item.
* `POST /outline/4/` should create a new item inside of the 5th item inside of the root item.
    * It should return the appropriate HTTP status code, along with the JSON representation of the new item.
* `PUT /outline/5/6/` should modify the text of the 7th item inside of the 6th item inside of the outline.
    * It should return the appropriate HTTP status code.
    * It should return the new JSON representation of the 6th item inside of the 5th item inside of the outline.
* `DELETE /outline/7/` should delete the 8th item inside of the root item.\
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

You can use UUIDs instead of integers if you want, just as long as each outline item has a unique URL.

**Do not** have the API send the entire tree at once, it should only send the URLs for each child item.

## Create the UI in JS

Create JS code to:

1. Remove the "Loading...".
    * **Hint:** Use `window.addEventListener('load', someFunction)` to run a function once the page has loaded.
2. Fill in the page.

There are *at least* three different ways to do this.
Using `document.createElement`, `appendChild`, and `remove` to manipulate the DOM directly is probably the easiest.
You can also use `innerHTML` to add multiple elements at the same time to the DOM. Using `innerHTML` creates potential security problems that we will discuss during the lectures on security later in the semester.
A third approach is to register custom elements and add them to the DOM, or even using  Web Components & Templates in combination with one of the two previous approaches.

**Hint:** Using proper OOAD will save you a lot of work. Apply the skills you learned in CMPUT 301.
I suggest making model proxy classes that are responsible for synchronizing with the model objects in the Flask backend, by making calls using the Fetch API. 
If you only use "own properties" for things the server sends, you can serialize the model proxy objects to JSON for sending, and apply updates directly to the model proxy objects from deserialized JSON when recieving.

**Hint:** Using the "event.preventDefault();" on form `submit` events will prevent the browser from trying to submit the form,
so you can handle form submission in your custom JS code instead.

**Hint:** A single DOM object can only be added to the DOM once.

## Call the backend

* To get an item, GET the item's URL on the backend.
    * GET should return JSON for the item. The item's children should be represented as an array or object with URLs of the children, **not** the full representation of the children.
* To add an outline item, POST to the item's parent's URL on the backend.
    * POST should return JSON for the new child item including the new child's URL, text, etc. This should be the same contents as a GET that immediately follows the POST to the URL of the new child item.
* To update an item's text, PUT to the item's URL on the backend.
    * PUT should return JSON for the item including the updated information. This should be the same contents as a GET that immediately follows the PUT.
* To delete an item, DELETE to the item's URL on the backend.
    * Backend can respond with HTTP 204 No Content if successful.

## Add polling

Add polling in your code to get live updates. 
Use `fetch()` and promises, not the old `XMLHttpRequest`.

Each browser window that has the outline open should be able to see all the changes that the other browser windows make in a reasonable amount of time (less than a few seconds).

Make sure that the updates don't "clobber" or overwrite or reset whatever the user is typing. The easiest way to do that is to remember what the server sent previously for an item, and not update the HTML DOM unless the server sends something different from what it sent the last time.

For simplicity, you can ignore the conflict problem when two people are editing the same outline item at the same time.

Use Fetch API, **not XMLHttpRequest**.

**Hint:** The `input` event of a `text` type `<input>` will happen every time the text changes at all (every keypress if the user istyping.) The `change` event only happens when the user changes their focus to a different element.

## Optimize Communications

Optimize communications so that the frontend doesn't have to ask the backend for the details of unchanged items.

* One way to do this is:
    * Each time the outline is changed in the backend, record the URL of the changed item in a list in the backend.
    * Add an endpoint that can `GET` a list of updated items, with a `since` query parameter that takes a time.
    * Then, in your JS, poll the list of updated items, then only poll the items changed since the last poll to update the UI.

Optional: Also consider adding code to make sure the frontend doesn't make another request to the same endpoint while the first request is still in progress. You can do this by using the `finally()` method on a promise to run code whether or not the promise resolves or rejects.

Optional: Also consider adding code to batch updates to the backend, e.g. instead of every keypress while typing, limit PUT requests to one update per second while typing.

## Make it look nice

Add CSS to make your outline look nice. You should give it your own personal style, but it should be pleasing and easy-to-use.

# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* All of your Python code must be in `outliner.py`.
* All of your CSS code must be in `style.css`.
* All of your JS code must be in `main.js`.
* All of your elements must be created dynamically using plain JS to manipulate the DOM in `main.js`.
    * You must not modify `ui.html`.
    * `ui.html` must be the only HTML served by flask (on the route `/`).
* Using of any frontend frameworks, CSS libraries, JS libraries or frameworks is forbidden. 
  * You must write plain JS, CSS and HTML. 
  * You must not use JS libraries, frameworks, preprocessors, or transpilers.
  * You must not use CSS libraries, frameworks, preprocessors or transpilers.
  * You must not use frontend frameworks, HTML frameworks, preprocessors or transpilers. 
* If you borrow CSS from examples online, always cite the author, give the source URL, and the date you downloaded it.
* You **must not** modify the HTML.
    * Use JS to modify the DOM.
    * You must not modify the `ui.html` or add other HTML files.
    * You must not have flask send any other HTML.

# Requirements

* A functioning outline editor 
    * Has a root item
    * Can add items under any item
    * Can delete items
    * Can add text to items
    * Changes in one window are reflected in a few seconds on all the other windows.
    * Changes aren't overwritten by old data.
    * Demonstrates correct usage of promises.
    * Demonstrates live modification of elements of the DOM.
* A git repository that does not contain built (compiled, transpiled, bundled) or downloaded artifacts, including but not limited to:
    * `virtualenv` `venv` etc.
    * `.pyc` files, `__pycache__` directories.
* A flask app `outline.py` that serves the files `ui.html`, `main.js`, `favicon.ico`, and `style.css`.
    * Maintains a model of the outline in memory.
    * Makes the outline available by JSON API endpoints.
    * Demonstrates GET POST PUT and DELETE functionality.
    * It doesn't send multiple items at once, instead it sends URLs to child items which must be fetched separately.

# Submission Instructions

Make sure you push to github classroom **BEFORE 4PM on the day of your lab section!** You will not be able to push after that!

Submit a link to your repo in the form `https://github.com/uofa-cmput404/w24-h0x-labsignment-flask-yourgithubname`. **Do not** submit a link to a branch, a file, or the clone url. If you do not do this we will not know which github submission is yours.

# Collaboration

* You may consult with others (exchange high-level ideas) but the submission should be your own source code.
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/labs.md#lab-marking)

