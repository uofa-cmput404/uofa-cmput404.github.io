Title: Heroku Lab
date: 2024-01-25
tags: labs
authors: Xin Yang
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking

----

[TOC]

# Description

Big lab! This lab contains two phases. In Phase One, you will build a simple Django website. Understand the fundamentals of Django's MVC architecture using the built in models and views.
In Phase Two, you will deploy the Django application to [Heroku](https://www.heroku.com/). Understand the reasoning behind Platform as a Service (PaaS) businesses like Heroku. You may follow the official documentation.

## Warning!

The University's firewall (UWS) blocks new domains for 24 hours to prevent scam domains.

This *might* affect your Heroku domain.The University's firewall is also inconsistent so it doesn't *always* seem to do this.
We have complained about this every semester since forever, but IST simply does not care.

Double check that your Heroku is not blocked before you demo. We will **not** give you an extension if you Heroku is blocked.

You have several options to make sure this doesn't happen:

* Connect to your Heroku with your web browser on UWS at least 2 days before your demo.
    * It doesn't have to be fully working, the firewall just needs to see that the domain does in fact exist.
* Bypass the Unversity's DNS server by adding the hostname and IP address of your heroku site to your hosts file.
    * Follow the steps of the "Checking your heroku app" below.
    * Then add it your hosts file:
        * It uses the format `ip-address host-name host-name` on each line.
            * Example (has CNAME): `46.137.15.86 ie02.ingress.herokuapp.com example-app-1234567890ab.herokuapp.com`
            * Example (no CNAME): `34.201.81.34 lab3test-fbb81150e720.herokuapp.com`
        * Linux: edit /etc/hosts as superuser. and add it in the format .
        * MacOS: <https://kinsta.com/knowledgebase/edit-mac-hosts-file/>
        * Windows 10/11: <https://allthings.how/how-to-edit-hosts-file-in-windows-11/>
    * If it stops working check again with nslookup and update it.
* Use a VPN service or proxy.
* Demo over Zoom using Shaw or Telus internet, or another internet not provided by the University.

# Getting Started

## Prepare your Repo

1. Get the github classroom link from eClass, create your assignment, and clone it.
2. Create an appropriate `.gitignore` file, to prevent unwanted files being commited to your repository.

Place this gitignore within the root of your project. You can combine [this one](https://github.com/github/gitignore/blob/main/Python.gitignore) and [this one](https://github.com/github/gitignore/blob/main/Node.gitignore) and [this one](https://github.com/django/django/blob/main/.gitignore) for your django+node project. Double check you're not staging any unwanted files before you commit. The `git status` command can help with that.

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

# Lab Instructions

## Phase One: Django Polls App

### Creating a Django Project

* Official Docs [Overview](https://docs.djangoproject.com/en/5.0/intro/overview/), [Installation](https://docs.djangoproject.com/en/5.0/intro/install/)


Make sure to use a **virtual environment** for this lab!

If you're doing this on **Windows** please make sure to follow the Windows
instructions for Lab 1 before starting this lab!

Follow Labsignments 2 to create a virtual environment and install Django. You can tell Django is installed and which version by running the following command in a shell prompt:

```bash
python -m django --version
```


Initialize a new Django project called **lab3**.

```bash
django-admin startproject lab3
cd lab3
python manage.py runserver
```

Now that the server’s running, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!

----

### Creating a Django App

 * Official Docs [Part 1](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

Create a new application within **lab3** called **polls**.

```bash
python manage.py startapp polls
```

Modify the *polls/views.py* file to look like the following.

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Create a file at *polls/urls.py* with the following code.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Within *lab3/urls.py* include the following code.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

Run the Django project with the runserver command.

```bash
python manage.py runserver
```

Go to [http://localhost:8000/polls/](http://localhost:8000/polls/) in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which you defined in the index view.

If you get an error page here, check that you’re going to [http://localhost:8000/polls/](http://localhost:8000/polls/) and not [http://localhost:8000/](http://localhost:8000/).


----

### Working with Models

* Official Docs [Part 2](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)

Time to create our first models. Open up *lab3/settings.py* and ensure that the default database is set to `sqlite3`.

```python
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Within *polls/models.py* include the following code.

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

To activate our poll application in our project, add it to the installed apps within *lab3/settings.py*.

```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

Make the database migrations.

```bash
python manage.py makemigrations polls
```

You should see something similar to the following:

```bash
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

Run the migration command to create the tables in your database.

```bash
python manage.py migrate
```
----

### Using Django Admin

Create a user that can log into the admin site.

```bash
python manage.py createsuperuser
```

You will be asked to enter your username, email, and password (twice for confirmation).


Make the polls app modifiable in the admin by editing the *polls/admin.py* file to be the following:

```python
from django.contrib import admin

from .models import Choice, Question

admin.site.register(Choice)
admin.site.register(Question)
```

Start the development server again and go to `/admin` on your local domain – e.g., [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). You should see the admin’s login screen and can login with your admin account.

```bash
python manage.py runserver
```

### Working with Views

* Official Docs [Part 3](https://docs.djangoproject.com/en/5.0/intro/tutorial03/)

Add some additional views to the *polls/views.py* file. Include the following methods:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

With the above views added, add them to *polls/urls.py*.

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Take a look in your browser, at `/polls/34/`. It’ll run the detail() function and display whatever ID you provide in the URL. Try `/polls/34/results/` and `/polls/34/vote/` too – these will display the placeholder results and voting pages.

----

### Making views render model data

Update the *polls/views.py* `index` method so the questions are returned.

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```

Create an empty directory named *templates* within *polls*. Then create another directory named *polls* within the *templates* directory. Lastly create a file called *index.html* within the second *polls* directory.

```bash
mkdir -p polls/templates/polls
touch polls/templates/polls/index.html
```

Within the newly created empty *polls/templates/polls/index.html* file, write the following.

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Update the `index` view in *polls/views.py* to use the new template.

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

Add a new template file for the poll details view.

```bash
touch polls/templates/polls/detail.html
```

For the newly created template in *polls/templates/polls/detail.html*, update the content with the template tag for our question:

```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

Update the `detail` view in *polls/views.py* to use the new template.

```python
from django.shortcuts import get_object_or_404, render

from .models import Question

# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

Remove the hardcoded urls that we specified in the *polls/templates/polls/index.html* file and replace it with at emplate tag referencing our url.

```html
<!-- old -->
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>

<!-- new -->
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

----

### Namespacing URL names

Add an `app_name` in the *polls/urls.py* file to set the application namespace.

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Change your *polls/index.html* template to point at the namespaced detail view.

```html
<!-- old -->
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

<!-- new -->
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

----

### Writing a simple form

* Official Docs [Part 4](https://docs.djangoproject.com/en/5.0/intro/tutorial04/)

Update the *polls/templates/polls/detail.html* file to match the following:

```html
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

Remember, in Part 3, we created a url for the polls application in *polls/urls.py* that includes this line:

```python
path('<int:question_id>/vote/', views.vote, name='vote'),
```

We also created a dummy implementation of the `vote()` function in *polls/views.py*. Let’s update the `vote` view in *polls/views.py* to handle the new template.

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

After voting, the application should redirect to a view displaying the results. Update the `results` view in *polls/views.py*

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

Create a template for the results in *polls/templates/polls/results.html*

```html
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

Run your application. Use the admin interface to create aquestion, then create multiple choices for your question. Navigate back to `polls/` and attempt to use your application.

----

### Refactoring: Generic Views

To convert the `poll` application to use generic views, we will:

1. Convert the old url conf.
2. Delete some of the old, unnecessary views.
3. Introduce new views based on Django's generic views.

Amend the *polls/urls.py* url configuration. Note that the name of the matched pattern in the path strings of the second and third patterns has changed from `<question_id>` to `<pk>`.

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Amend the *polls/views.py* file.

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    ...  # same as above, no changes needed.
```

----

### Serializing and Deserializing Queries (Optional, but highly recommended to do)

Based from the DRF (Django Rest Framework) tutorial [here](https://www.django-rest-framework.org/tutorial/1-serialization/)

To convert your queries to or from a JSON object you can use Django's serializers to serialize or deserialize Django QuerySets to or from JSON objects.  

First install the Django Rest Framework library using `pip`

```bash
pip install djangorestframework
```

Then add the `rest_framework` app to `INSTALLED_APPS` in our `lab3/settings.py` file

```python
INSTALLED_APPS = [
    ...
    'rest_framework'
]
```

### Creating a Serializer Class

Create a file in the `polls` directory named `serializers.py` and add the following

```python
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data
        """
        return Question.object.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data
        """
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance
```

### Update our views using our Serializer

Once you have the serializers you now need to write some API views using the new Serializer class

Edit the `polls/views.py` file, and add the following

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer

...


@api_view(['GET'])
def get_questions(request):
    """
    Get the list of questions on our website
    """
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)
```

The `@api_view` decorator will wrap the view so that only HTTP methods that are listed in the decorator will get executed.

### Updating the our URLs for the new views

Because we want our API responses to have JSON objects we will have to add another set of urls with a `api/` prefix to our `polls/urls.py` file.

```python
from django.urls import path
from . import views

urlpatterns = [
    ...
    path('api/questions/', views.get_questions, name='get_questions'),
]
```

Now run the project again with the `runserver` command and go to `polls/api/questions/`

```bash
python manage.py runserver
```

You should see a list of question in a json format.

### Updating a Question Using our Serializer

We can use the serializer to update the `question_text` field of our question entries.

```python
@api_view(['GET','POST'])
def update_question(request, pk):
    """
    Get the list of questions on our website
    """
    questions = Question.objects.get(id=pk)
    serializer = QuestionSerializer(questions, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)
```

and update the `polls/urls.py` file.

```python
from django.urls import path
from . import views

urlpatterns = [
    ...
    path('api/question/<int:pk>', views.update_question, name='update_question'),
]
```

Run the project using `runserver` and go to this link `polls/api/question/1` and POST the following information below.  

```json
{
    "question_text": "Updated question text"
}
```

After clicking the POST button you should see the updated value in the json structure above. The new value should also be reflected in the model admin page as well.

### Other cool things to know

- If your serializer is replicating a lot of information that's also contained in the model being (de)serialized then you can use the `ModelSerializer` class to automatically generate the fields and produce a simple default implementations for the `create()` and `update()` methods
- If you want to support alternative serialization and deserialization styles then you can inherit the `BaseSerializer` class and override these four functions depending on what functionality you want the serializer class to support:
  - `.to_representation()` - Override this to support serialization, for read operations
  - `.to_internal_value()` - Override this to support deserialization, for write operations
  - `.create()` and `.update()` - Override either or both of these to support saving instances.

### More information about DRF

Her is the [API Guide for Serializers](https://www.django-rest-framework.org/api-guide/serializers/)

Here is the [Tutorial guide](https://www.django-rest-framework.org/tutorial/1-serialization/)

### Optional/Outside of Lab

It is in your best interest to Work through the rest of Django's First Steps Tutorials:

* [Part 5: Testing](https://docs.djangoproject.com/en/5.0/intro/tutorial05/)
* [Part 6: Static Files](https://docs.djangoproject.com/en/5.0/intro/tutorial06/)
* [Part 7: Customizing the Admin Site](https://docs.djangoproject.com/en/5.0/intro/tutorial07/)


## Phase Two: Heroku

### Setting up the Heroku CLI

Sign up for a Heroku account at [https://signup.heroku.com/](https://signup.heroku.com/).
You can apply for free Heroku credits for 12 months at [https://www.heroku.com/github-students](https://www.heroku.com/github-students) with an eligible GitHub student account [https://education.github.com/pack](https://education.github.com/pack). 

Note: Remember to clean up all Heroku resources after this course to avoid unexpected charges after exceeding the credit limit or the offer expires.

Download and install the [Heroku CLI tools](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

* Use the default installation instructions if you are on a VM or your own device.
* If using a lab machine, download and extract the tarball and add the binary to your path.

```bash
wget https://cli-assets.heroku.com/channels/stable/heroku-linux-x64.tar.gz
tar -xvf heroku-linux-x64.tar.gz
export PATH="$PATH:$HOME/heroku/bin"
```

Ensure the heroku tool works, login to your account.

```bash
heroku --version
# heroku/8.7.1 linux-x64 node-v16.19.0
heroku login
```

### Preparing our Django Application for Heroku

Ensure the Django application created in Phase One is working locally.

Activate the virtualenv for the Django application.

Ensure that the current working directory is similar to the following.

```text
$ tree 
.
├── db.sqlite3
├── manage.py
├── lab3
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   └── polls
    │       ├── detail.html
    │       ├── index.html
    │       └── results.html
    ├── tests.py
    ├── urls.py
    └── views.py

```

Pip install [gunicorn](https://gunicorn.org/) and [django-on-heroku](https://github.com/pkrefta/django-on-heroku).

```bash
pip install gunicorn django-on-heroku
```

Save the new python requirements into the *requirements.txt* file.

```bash
pip freeze > requirements.txt
```

Create a new file named *Procfile* for Heroku applications. The file shall have following contents:

```text
web: gunicorn lab3.wsgi
```

Within *lab3/settings.py*, add the following statements:

```python
import django_on_heroku # top of the file

# ...

django_on_heroku.settings(locals()) # bottom of the file
```

### Deploying our Django Application to Heroku

Commit your files and deploy the application using a the heroku command line tool. See [their article on how to do this](https://devcenter.heroku.com/articles/git). Follow the instructions for an existing app, not a new app: `use heroku git:remote`, **not** `heroku create`.
If you used `heroku create`, please see [this stackoverflow question](https://stackoverflow.com/questions/50421071/git-i-made-a-repository-inside-a-repository-and-now-i-just-want-the-one-big-rep) about how to return to a single repository.

Run your migrations, create a Superuser, and ensure your application functionality works.

```bash
$ heroku run --app APPNAME python manage.py migrate
$ heroku run --app APPNAME python manage.py createsuperuser
```

Go to `/polls` on your Heroku deployed site, you should be able to use the Polls app from Heroku. 

Note: Please make sure that the Heroku app uses Postgres as the backend database. If you created the Heroku app through Git integration, this should be a default setting.

You can verify the backend in use by login into the dashboard of the Heroku app: [https://dashboard.heroku.com/apps/APP_NAME](https://dashboard.heroku.com/apps/APP_NAME), then click the `Resources` tab, you should see `Heroku Postgres` under the `Add-ons` Section.

If a different Heroku backend is used (e.g., SQLite), or if you try to create the Heroku app through the Heroku webpage, you can follow the below instructions to enable Postgres.
[https://www.geeksforgeeks.org/deploying-django-app-on-heroku-with-postgres-as-backend/](https://www.geeksforgeeks.org/deploying-django-app-on-heroku-with-postgres-as-backend/)

### Checking your heroku app

You can use the `heroku open` command to open your heroku app in a web browser. 

* Add your apps hostname, cname, and ip address to the README.md file in your git repo. You **must** do this to help us mark your work. 
    * First get your heroku apps hostname, it will look something like `example-app-1234567890ab.herokuapp.com`.
    * Then get an IP address for it using the `nslookup` command and a public dns server not controlled by the University.
        * This will look something like `nslookup example-app-1234567890ab.herokuapp.com 1.1.1.1`.
            * The second argument is the DNS server's IP address. You could also use:
                * `nslookup example-app-1234567890ab.herokuapp.com 8.8.8.8`
                * `nslookup example-app-1234567890ab.herokuapp.com 9.9.9.9`
                    * Or any other [public DNS server](https://duckduckgo.com/?t=ffab&q=public+dns+servers&ia=answer&iax=answer). `1.1.1.1` `8.8.8.8` and `9.9.9.9` are just easy to remember!
    * Read the output of nslookup, it will say something like:
        * `example-app-1234567890ab.herokuapp.com  canonical name = ie02.ingress.herokuapp.com.`
        * `ie02.ingress.herokuapp.com`
        * `Address: 46.137.15.86`
    * Sometimes it doesn't have CNAME, this is fine:
        * `Name:   lab3test-fbb81150e720.herokuapp.com`
        * `Address: 34.201.81.34`
        * In this case, write "none" for the cname.
    * Write your app's hostname, cname, and ip address to the README.md in your git repo.
* Make sure you can use the admin panel on heroku from your web browser.
    * Hint: shut down your localhost server if its running to make sure you're not connecting to the one on your computer by accident!
    * Use the admin panel to add a poll.
* Make sure you can use the polls app on heroku from your web browser.
* Make sure your heroku app remembers the results of your polls and your superuser login!
    * If your heroku is not configured properly to use postgres it will forget them randomly! (somewhere between 0 and 24 hours.)

# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* Must run on Ubuntu (Use the undergrad lab machines, for example the ones in CSC 2-29 or install an Ubuntu VM to check this)
* Must run on your machine (whatever machine you use to demo)
* Must be running on heroku, with some polls that you created for the TA to look at when they mark it.

# Requirements

* A working Django 5 application
    * using the latest Django version from pypi
        * downloaded with pip into a virtualenv
    * that is deployed on Heroku 
* A git repository that does not contain built (compiled, transpiled, bundled) or downloaded artifacts, including but not limited to:
    * virtualenv
    * node_modules
    * main.min.js
    * README.md
        * Has heroku app's hostname, cname, and IP address.
            * cname can be "none" if nslookup doesn't give a cname.

# Submission Instructions

Make sure you push to github classroom **BEFORE 4PM on the day of your lab section!** You will not be able to push after that!

Submit a link to your repo in the form `https://github.com/uofa-cmput404/w24-h0x-labsignment-heroku-yourgithubname` on eClass. **Do not** submit a link to a branch, a file, or the clone url. If you do not do this we will not know which github submission is yours.

# Collaboration

* You may consult with others (exchange high-level ideas) but the submission should be your own source code.
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/labs.md#lab-marking)

# Tips

Django is a complex framework and maybe overwhelming at times. You should consult the documentation should you run into any issues with the framework. 

If you're unable to load a static file or resource, it maybe because you're not referencing it correctly. It may be in a different directory or you have a typo when you are referencing that particular resource using its path. 

Another common problem is not being able to render the templates even though you're directory structure is correct. Make sure your app is registered in `settings.py` otherwise it may not render.

