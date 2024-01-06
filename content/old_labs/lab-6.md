Title: Lab 6 - Heroku
Date: 2019-01-07 12:41
Modified: 2019-02-11 17:58
Tags: homework, lab
Authors: Alexander Wong
Status: published

----

Deploy the Django application created in [Lab 4]({filename}lab-4.md) to [Heroku](https://www.heroku.com/). Understand the reasoning behind Platform as a Service (PaaS) businesses like Heroku. You may follow the [official documentation](https://devcenter.heroku.com/articles/django-app-configuration).

### Setting up the Heroku CLI

Sign up for a free Heroku account at [https://signup.heroku.com/](https://signup.heroku.com/).

Download and install the [Heroku CLI tools](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

* Use the default installation instructions if you are on a VM or your own device.
* If using a lab machine, download and extract the tarball and add the binary to your path.

```bash
wget https://cli-assets.heroku.com/heroku-linux-x64.tar.gz
tar -xvf heroku-linux-x64.tar.gz
export PATH="$PATH:$HOME/heroku/bin"
```

Ensure the heroku tool works, login to your account.

```bash
heroku --version
# heroku/7.19.4 linux-x64 node-v11.3.0
heroku login
```

### Deploying our Django Application

Ensure the Django application created in [Lab 4]({filename}lab-4.md) is working locally.

Activate the virtualenv for the Django application.

Ensure that the current working directory is similar to the following.

```text
$ tree 
.
├── db.sqlite3
├── manage.py
├── mysite
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
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-37.pyc
    │       └── __init__.cpython-37.pyc
    ├── models.py
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
web: gunicorn mysite.wsgi
```

Within *mysite/settings.py*, add the following statements:

```python
import django_on_heroku # top of the file

# ...

django_on_heroku.settings(locals()) # bottom of the file
```

Commit your files and deploy the application using a git integration.

What happens when you go to `/polls` on your Heroku deployed site?

Run your migrations, create a Superuser, and ensure your application functionality works.

```bash
$ heroku run --app APPNAME python manage.py migrate
$ heroku run --app APPNAME python manage.py createsuperuser
```

**Question 1**: What are some ways you can deploy your code to Heroku?

**Question 2**: What is a Procfile used for?

**Question 3**: What is the link to your deployed application (on herokuapps)?

Optional: Configure TravisCI or CircleCI for a deployment pipeline that utilizes tests.
