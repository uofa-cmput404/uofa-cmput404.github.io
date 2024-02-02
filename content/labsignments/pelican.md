Title: Pelican Lab
date: 2024-02-01
tags: labs
authors: Sadia Zahin Prodhan
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking
----

[TOC]

# Description
The primary objective of this lab is for you to acquire the skills necessary to create a static page using [Pelican](https://blog.getpelican.com/), deploy it using [GitHub pages](https://pages.github.com/), and learn to customize the basic themes by experimenting with CSS styling.

# Getting Started


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
> Is this your personal page (username.github.io)? (y/N) N
Done. Your new project is available at /path/to/your/project
```
# Lab Instructions
## Phase One: Simple Pelican Site

### Create your first Article

Create a file inside *content* with some content. For example, you can use *content/my-first-article.md* with the following:

```markdown
Title: My First Article
Date: 2019-01-07 8:00
Category: Blog

I like free static web hosting.
```

###Generate and preview your site
For Mac And Ubuntu:

`make devserver`.  

For Windows:
```bash
pelican content
pelican --listen
```
 
 Your site should now be available at [http://localhost:8000](http://localhost:8000).


### Deploy your page to Github

Update *publishconf.py* and set `SITEURL` to your github given url.
```bash
SITEURL = 'https://uofa-cmput404.github.io/${repository-name}'

```
* For Mac and Ubuntu: 
    * Deploy using `make github`.
    * If you get ghp-import error. Install ghp-import using pip. (`pip install ghp-import`)
* For Windows:
```bash
pelican content -o output -s pelicanconf.py
ghp-import output  (you will need to install ghp-import with pip/conda)
git push origin src

```


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

## Phase TWO: Playing around with CSS

Create 3 more articles for your site from 3 project [Gutenberg](http://www.gutenberg.org/browse/scores/top)   HTML documents of your choosing, you can directly download the html file from the website. 

Write CSS to enable your site to have dark mode, light mode, print mode, and responsiveness in both desktop and mobile views.  

* Light Mode: You can take inspiration from modern websites such as amazon, facebook or google. BUT DO NOT COPY THEIR CODE. Try to make your light mode as fancy as possible.  

* Dark Mode: You can take inspiration from the [oatmeal comic](https://theoatmeal.com/comics/design_hell?fbclid=IwAR32De0TRFISnARpWunp3jvoCF1k1iXdotYZbvenRJOvqUCeaJwABk91JFw) or [space jam](https://www.spacejam.com/1996/). Try to make it like those 90s website.

* Print Mode: Try to make the page look good and clean for printing.

Finally publish to your GITHUB PAGES!!!

You should use media queries to achieve these

```
/* Light mode styles */
  @media (prefers-color-scheme: light) {
    html,body {
      background-color: #d7a1a1;
      /* Add more styling for light theme */
    }
    /* Add more styling for light theme */

  }
/* Dark mode styles */
  
  @media (prefers-color-scheme: dark) {
    html, body {
      background-color: #0f0f0f;
       /* Add more styling for dark theme */
    }
    /* Add more styling for dark theme */

  }

  /* Styles for printing */
  @media print {
    html,body {
      background-color: #fff;
      /* Add more styling for printing */
    }
  
    /* Additional styles for printed pages */
  }
  /* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {
  /* Add styling here */
}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {
   /* Add styling here */
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
   /* Add styling here */
}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
   /* Add styling here */
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
   /* Add styling here */
}
```

You can read more about CSS and Media Queries [here](https://www.w3schools.com/css/default.asp)

### Testing it on the Browser
You can use a browser to test out the different modes in the developer tools or developer console. Firefox is more preffered as the latest version has the light mode , dark mode and printing mode button in the tools. You can just click and toggle between different modes. 
<br>
1. Open your browser. <br>
2. Right click and select <strong> Inspect (Q) </strong><br>
* Keyboard shortcut for Windows: CTRL+ SHIFT + I <br>
* Keyboard shortcut for MAC: Command + Option + I. <br>
Once you have opened the Developer Tools, you can toggle between dark mode, light mode and print mode by clicking on those buttons.
<br><img id="toggle-mode" alt="toggle-mode" src="{attach}Firefox-mode-toggle.png" style="width: 50%;"> <br>
You can change to Desktop and mobile view by click on this button.

<br><img id="mobile-view" alt="mobile-view" src="{attach}Desktop-Mobile-view.png" style="width: 50%;"> 

In case your dark mode is not working in firefox, please check your firefox settings and see if the privacy.resistFingerprinting is set to false, otherwise it will always override with light mode. 

# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* Using of any frontend frameworks, css libraries or frameworks such bootstrap or tailwind is FORBIDDEN. You have to write plain CSS.
* If you borrow CSS, always cite the author and the source

# Recommendation
* Go look at CSS on the internet. Check the licenses.
* Look how things are achieved.
# Requirements
A functioning Pelican site featuring four articles with different stylings in dark mode, light mode, and print mode, and responsive in both mobile and desktop views, deployed on GitHub Pages.

# Submission Instructions

Make sure you push to github classroom **BEFORE 4PM on the day of your lab section!** You will not be able to push after that!

Submit a link to your repo in the form `https://github.com/uofa-cmput404/w24-h0x-labsignment-pelican-yourgithubname` and your Github Pages URL in the form `https://uofa-cmput404.github.io/your-repo-name/` on eClass. **Do not** submit a link to a branch, a file, or the clone url. If you do not do this we will not know which github submission is yours.

# Collaboration

* You may consult with others (exchange high-level ideas) but the submission should be your own source code.
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/labs.md#lab-marking)
