Title: Lab 4 - Django
Date: 2019-01-07 9:10
Modified: 2021-10-12 10:00
Tags: homework, lab
Authors: Alexander Wong, Xin Yang, Jihoon Og
Status: published

----

Big lab! Build a simple [Django](https://www.djangoproject.com/) website. Understand the fundamentals of Django's MVC architecture using the built in models and views. 

Answers to the questions should be submitted to *Lab 4* on eClass. You may also follow along with the [official documentation](https://docs.djangoproject.com/en/3.1/#first-steps). We will be going through Parts 1 to 4 of the first steps tutorial in lab. You should commit your project to git after each question.

### Creating a Django Project

* Official Docs [Overview](https://docs.djangoproject.com/en/3.1/intro/overview/), [Installation](https://docs.djangoproject.com/en/3.1/intro/install/)

Create a virtual environment and install Django.

Make sure to use a **virtual environment** for this lab!

If you're doing this on **Windows** please make sure to follow the Windows
instructions for Lab 1 before starting this lab!

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip install Django==3.1.6 # latest official version
```

Initialize a new Django project called **mysite**.

```bash
django-admin startproject mysite
cd mysite
python manage.py runserver
```

Add your files and push the contents to GitHub. The *manage.py* file should be at the root of your github repository.

**Question 1**: What is the link to your github repository for this lab?

**Question 2**: After starting a brand new Django application and running the runserver command, what does the browser show you?

----

### Creating a Django App

 * Official Docs [Part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

Create a new application within **mysite** called **polls**.

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
  path('', views.index, name='index'),
]
```

Within *mysite/urls.py* include the following code.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

Run the Django project with the runserver command.

```bash
python manage.py runserver
```

**Question 3**: After creating the first view within polls, what does the browser show you when navigating to `/` and to `/polls` respectively?

----

### Working with Models

* Official Docs [Part 2](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)

Time to create our first models. Open up *mysite/settings.py* and ensure that the default database is set to `sqlite3`.

```python
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Within *polls/models.py* include the following code.

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

To activate our poll application in our project, add it to the installed apps within *mysite/settings.py*.

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Make the database migrations.

```bash
python manage.py makemigrations polls
```

Run the migration command to create the tables in your database.

```bash
python manage.py migrate
```

**Question 4**: What is a Django migration and why do we need them?

----

### Using Django Admin

Create a user that can log into the admin site.

```bash
python manage.py createsuperuser
```

Make the polls app modifiable in the admin by editing the *polls/admin.py* file to be the following:

```python
from django.contrib import admin

from .models import Choice, Question

admin.site.register(Choice)
admin.site.register(Question)
```

Start the development server again and go to `/admin` on local application.

```bash
python manage.py runserver
```

**Question 5**: What do you see after you log into the Django adminstration site? From a high levle, how do you get custom models to appear in the Django admin page?

----

### Working with Views

* Official Docs [Part 3](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)

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
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

**Question 6**: What do you see when you go to `/polls/38/` in your browser? What about `/polls/38/results` and `/polls/38/vote`? What happens when you don’t put a number, and instead use a string? How would you modify the *urls.py* file to allow arbitrary alphabetic characters?

----

### Making views render model data

Update the *polls/views.py* `index` method so the questions are returned.

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
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
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
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
    return render(request, 'polls/detail.html', {'question': question})
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

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

Change your *polls/index.html* template to point at the namespaced detail view.

```html
<!-- old -->
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

<!-- new -->
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

**Question 7**: Why is it a bad idea to hardcode urls into the templates?

----

### Writing a simple form

* Official Docs [Part 4](https://docs.djangoproject.com/en/3.1/intro/tutorial04/)

Update the *polls/templates/polls/detail.html* file to match the following:

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```

Create a url *polls/urls.py* that handles the form submitted data.

```python
path('<int:question_id>/vote/', views.vote, name='vote'),
```

Update the `vote` view in *polls/views.py* to handle the new template.

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

After voting, the application should redirect to a view displaying the results. Update the `results` view in *polls/views.py*

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
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

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
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
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

**Question 8**: What are the benefits of using Django's generic views over writing views 'the hard way'? When should you use a generic view and when shouldn't you use a generic view?

----

### Serializing and Deserializing Queries (Optional, but highly recommended to do)

Based from the DRF (Django Rest Framework) tutorial [here](https://www.django-rest-framework.org/tutorial/1-serialization/)

To convert your queries to or from a JSON object you can use Django's serializers to serialize or deserialize Django QuerySets to or from JSON objects.  

First install the Django Rest Framework library using `pip`

```bash
pip install djangorestframework
```

Then add the `rest_framework` app to `INSTALLED_APPS` in our `mysite/settings.py` file

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
@api_view(['POST'])
def update_question(request, pk):
    """
    Get the list of questions on our website
    """
    questions = Question.objects.get(id=pk)
    serializer = QuestionSerializer(questions, data=request.data, partial=True)
    if serializer.is_valid():
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

* [Part 5: Testing](https://docs.djangoproject.com/en/3.1/intro/tutorial05/)
* [Part 6: Static Files](https://docs.djangoproject.com/en/3.1/intro/tutorial06/)
* [Part 7: Customizing the Admin Site](https://docs.djangoproject.com/en/3.1/intro/tutorial07/)
