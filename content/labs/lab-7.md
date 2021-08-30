Title: Lab 7 - Flask
Date: 2019-02-19 09:52
Modified: 2019-02-19 09:52
Category: Lab
Tags: flask, python
Authors: Alexander Wong

----

Create a basic RESTful web application backend using [Flask](http://flask.pocoo.org/). Consume the API endpoints using [`cURL`](https://curl.haxx.se/) and [`httpie`](https://httpie.org/).

### Flask

Navigate to a new folder and initialize a new Python virtual environment.

```bash
mkdir cmput404lab7
cd cmput404lab7
virtualenv venv --python=python3
source venv/bin/activate
```

Install Flask.

```bash
pip install Flask
```

Create a new Python file named `hello.py` and edit its contents so it looks like this:

```python
#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)
```

Make the file executable and run the application. Navigate to the page in your browser.

```bash
chmod +x hello.py
./hello.py
# or
python3 hello.py

# In a new terminal
curl localhost:5000 # the port may be different on your machine
```

Modify the `hello.py` file to serve a RESTful api for managing a TODO list. First, install `flask_restful`.

```bash
pip install flask_restful
```

Update `hello.py` so it looks like the following.

```python
#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, "/")


if __name__ == "__main__":
    app.run(debug=True)
```

Run the server and see what it returns in your browser, or using cURL.

```bash
curl localhost:5000
```

Change the contents of `hello.py` to the following:

```python
#!/usr/bin/env python3

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("task")

TODOs = {
    1: {"task": "build an API"},
    2: {"task": "?????"},
    3: {"task": "profit"},
}


def abort_if_todo_not_found(todo_id):
    if todo_id not in TODOs:
        abort(404, message="TODO {} does not exist".format(todo_id))


def add_todo(todo_id):
    args = parser.parse_args()
    todo = {"task": args["task"]}
    TODOs[todo_id] = todo
    return todo


class Todo(Resource):
    """
    Shows a single TODO item and lets you delete a TODO item.
    """

    def get(self, todo_id):
        abort_if_todo_not_found(todo_id)
        return TODOs[todo_id]

    def delete(self, todo_id):
        abort_if_todo_not_found(todo_id)
        del TODOs[todo_id]
        return "", 204

    def put(self, todo_id):
        return add_todo(todo_id), 201


class TodoList(Resource):
    """
    Shows a list of all TODOs and lets you POST to add new tasks.
    """

    def get(self):
        return TODOs

    def post(self):
        todo_id = max(TODOs.keys()) + 1
        return add_todo(todo_id), 201


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")

if __name__ == "__main__":
    app.run(debug=True)

```

What does the browser show you when you navigate to `/todos` and `/todos/1`?

Try running the following `cURL` commands.

```bash
curl localhost:5000/todos
curl localhost:5000/todos/3
curl -v -X DELETE localhost:5000/todos/2
curl -v -X POST localhost:5000/todos -d "task=make sure to do lab 7 questions"
curl -v -X PUT localhost:5000/todos/3 -d "task=profit more"
```

### Httpie

In addition to using `cURL`, [`httpie`](https://httpie.org/) is specifically designed for interacting with RESTful JSON APIs. It has colour output and automatically pretty prints JSON for you.

```bash
pip install httpie
http localhost:5000/todos
http :5000/todos
http HEAD :5000/todos
http POST :5000/todos task="Try httpie!"
```

**Question 0**: What is the URL of your python flask_restfull code on github???

**Question 1**: How are Flask and Django different? What does Django provide for you that Flask does not?

**Question 2**: What does REST stand for? When I say something is RESTful, what does that mean?

**Question 3**: What does CRUD stand for? For each letter in CRUD, give the associated HTTP method.

**Question 4**: What do HTTP `1XX` Status Codes mean? HTTP `2xx`? HTTP `3xx`? HTTP `4xx`? HTTP `5xx`?

**Question 5**: What is an XSS attack? Provide one way a site can be vulneratble to an XSS attack.

**Question 6**: What does CORS stand for? What situation in web application development will you need to implement CORS protection?
  
  * Hint: What does the *CO* part of CORS mean?

------

**Optional**: Deploy your Flask application to Heroku.

  * How does your `Procfile` change when compared to a Django application?

