Title: Lab 3 - Common Gateway Interface
Date: 2019-01-07 8:40
Modified: 2019-01-07 11:50
Category: Lab
Tags: cgi, common gateway interface
Authors: Alexander Wong

----

Explore the Common Gateway Interface.

Answers to the questions should be submitted to *Lab 3* on eClass.

### Common Gateway Interface

Fork and clone the lab repository. [https://github.com/uofa-cmput404/cgi-lab](https://github.com/uofa-cmput404/cgi-lab)

Activate a python3 virtual environment.

Start the `cgi_server.py` in a background terminal window.

Initialize an empty file (this will be your CGI script).

```bash
touch hello.py
```

Make your CGI script executable.

```bash
chmod +x hello.py
```

Make the very first line of your CGI script the shebang:

```python
#!/usr/bin/env python
```

Examine the environment variables given to the CGI script.

**Question 1**: How do you inspect all environment variables in Python?

----

Make your CGI script serve the environment back as JSON. What changes if we add query parameters?

Modify your CGI script to report the values of the query parameters in the HTML.

**Question 2**: What environment variable contains the query parameter data?

----

Modify your CGI script to report the user’s browser in the HTML.

**Question 3**: What environment variable contains information about the user’s browser?

----

Modify your CGI script to contain a login form that POSTs to itself. You may use `login_page()` in *templates.py*.

Modify your CGI script to report the values of the POSTed data in the HTML.

**Question 4**: How does the POSTed data come to the CGI script?

----

Edit the username and password in `secret.py` and delete the `raise` line; then import it in your login CGI script.

Modify your CGI script to set a cookie if the login is correct.

**Question 5**: What is the HTTP header syntax to set a cookie from the server?

----

Modify your CGI script so it displays a secret message if the cookie says the user is logged in. You may use `secret_page()` from *templates.py*.

Capture the cookie using *proxy.py*.

**Question 6**: What is the HTTP header syntax the browser uses to send the cookie back?

----

Clear the cookie in the browser or use a private/incognito browser window

Use the cookie to appear to be logged in to the CGI script without logging in.
    * Within the JavaScript console, enter: `document.cookie = "key=value"`

**Question 7**: In your own words, what are cookies used for?
