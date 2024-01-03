Title: Lab 5 - Pelican & Basic HTML/CSS
Date: 2019-01-07 12:40
Modified: 2019-02-11 17:50
Category: Lab
Tags: pelican, html css
Authors: Alexander Wong
Status: hidden

----

Create a static page using [Pelican](https://blog.getpelican.com/), or write plain html. Deploy using [GitHub pages](https://pages.github.com/). Learn to style the basic theme.

Answers to the questions should be submitted to *Lab 5* on eClass. Feel free to follow along with the [official documentation](https://docs.getpelican.com/en/stable/quickstart.html).

*aside*: These lab instructions are currently using Pelican and hosted on Github Pages!

### Initializing the Project

Create a repository on Github for your github hosted page.

* If using a **User or Organization site**, the repo must be named `${username}.github.io`
    * raw html must be served on the master branch directly
* If using a project site, the repo can be named anything,
    * raw html can also be on the master branch in a directory named `/docs`


Clone the repository, change directory into the repo. Create a branch named `src` and initialize a `python3` virtual environment.

```bash
git clone {git-repo-url}
cd {git-clone-url}
git checkout -b src
virtualenv venv --python=python3
source venv/bin/activate
```

Install Pelican and Markdown.

```bash
pip install pelican markdown
```

Run the pelican quickstart.

```bash
pelican-quickstart

Welcome to pelican-quickstart v4.0.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

    
> Where do you want to create your new web site? [.] 
> What will be the title of this web site? My Cool Site
> Who will be the author of this web site? Danger Doggo
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Paris] America/Edmonton
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
Done. Your new project is available at /path/to/your/project
```

### Create your first Article

Create a file inside *content* with some content. For example, you can use *content/my-first-article.md* with the following:

```markdown
Title: My First Article
Date: 2019-01-07 8:00
Category: Blog

I like free static web hosting.
```

Generate and preview your site using `make devserver`. Your site should now be available at [http://localhost:8000](http://localhost:8000).

### Deploy your page to Github

Update *publishconf.py* and set `SITEURL` to your github given url.

* If using **User or Organization site**, deploy using `make github`.
    * If you get ghp-import error. Install ghp-import using pip. (`pip install ghp-import`)
* If using **Project site**, set *Makefile* `OUTPUTDIR=$(BASEDIR)/docs`.
    * Run `make publish`
    * Commit the *docs/* directory to the master branch on Github.

### Theme your static site

Make a directory called *templates*. Within this directory, create a new theme directory containing a templates folder and a static folder.

```bash
mkdir -p templates/mytheme/{static,templates}
```

Within the *templates/mytheme/templates" directory, create a new file *base.html*. Within the *templates/mytheme/static* directory, create a new file *style.css*.

```bash
touch templates/mytheme/templates/base.html
touch templates/mytheme/static/style.css
```

Add the following content to the file *templates/mytheme/templates/base.html*.

```html
{% extends "!simple/base.html" %}

{% block head %}
{{ super() }}
  <link rel="stylesheet" type="text/css" href="{{ SITEURL }}/theme/style.css" />
{% endblock %}
```

Modify the content of the *templates/mytheme/static/style.css* file to your preference. A quick sample stylesheet can be found below.

```css
html, body {
  margin: 0;
  border: 0;
  font-size: 100%;
  background-color: #000000;
  color: #ffffff;
}
```

Add your theme to your *pelicanconf.py* file.

```python
THEME = 'templates/mytheme'
```

In publishconf.py, Comment out `CATEGORY_FEED_ATOM`.
* See [pelican/issues/2489](https://github.com/getpelican/pelican/issues/2489)


Create at least 3 articles/pages on your static site and deploy to GitHub. Ensure that you are not using a theme created by someone else.

**Question 1**: What are some of the benefits of using a static site generator? What are some disadvantages?

**Question 2**: What is the link to your GitHub pages hosted static site?

If you are not finished [Lab 4]({filename}lab-4.md), please work on it. We will be deploying the Django application to Heroku in the next lab.
