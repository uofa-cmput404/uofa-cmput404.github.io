Title: Lab 4 - Django
Date: 2019-01-07 9:10
Modified: 2019-01-29 10:00
Category: Lab
Tags: django
Authors: Alexander Wong

----

Big lab! Build a simple [Django](https://www.djangoproject.com/) website. Understand the fundamentals of Django's MVC architecture using the built in models and views. 

Answers to the questions should be submitted to *Lab 4* on eClass. You may also follow along with the [official documentation](https://docs.djangoproject.com/en/2.1/#first-steps). We will be going through Parts 1 to 4 of the first steps tutorial in lab. You should commit your project to git after each question.

### Creating a Django Project

* Official Docs [Overview](https://docs.djangoproject.com/en/2.1/intro/overview/), [Installation](https://docs.djangoproject.com/en/2.1/intro/install/)

Create a virtual environment and install Django.

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip install Django==2.1.5 # latest official version
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

 * Official Docs [Part 1](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)

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
  path('', views.index, name='index')
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

* Official Docs [Part 2](https://docs.djangoproject.com/en/2.1/intro/tutorial02/)

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

* Official Docs [Part 3](https://docs.djangoproject.com/en/2.1/intro/tutorial03/)

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

**Question 7**: Why is it a bad idea to hardcode urls into the templates?

----

### Writing a simple form

* Official Docs [Part 4](https://docs.djangoproject.com/en/2.1/intro/tutorial04/)

Update the *polls/templates/polls/detail.html* file to match the following:

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'vote' question.id %}" method="post"> <!-- 'polls:vote'-->
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
        return HttpResponseRedirect(reverse('results', args=(question.id,))) # 'polls:results'
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

<a href="{% url 'detail' question.id %}">Vote again?</a> <!-- polls:detail -->
```

Run your application. Use the admin interface to create aquestion, then create multiple choices for your question. Navigate back to `polls/` and attempt to use your application.

----

### Refactoring: Generic Views

To convert the `poll` application to use generic views, we will:

1. Convert the old url conf.
2. Delete some of the old, unnecessary views.
3. Introduce new views based on Django's generic views.

Amend the *polls/urls.py* url configuration.

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

### Optional/Outside of Lab

It is in your best interest to Work through the rest of Django's First Steps Tutorials:

* [Part 5: Testing](https://docs.djangoproject.com/en/2.1/intro/tutorial05/)
* [Part 6: Static Files](https://docs.djangoproject.com/en/2.1/intro/tutorial06/)
* [Part 7: Customizing the Admin Site](https://docs.djangoproject.com/en/2.1/intro/tutorial07/)
