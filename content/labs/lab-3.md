Title: Lab 3 - Common Gateway Interface
Date: 2019-01-07 8:40
Modified: 2019-01-07 8:45
Category: Lab
Tags: cgi, common gateway interface
Authors: Alexander Wong

----

Explore the Common Gateway Interface.

Create a text file `lab3-${ccid}.txt` containing answers to the questions and submit to *Lab 3* on eClass.

## Common Gateway Interface

1. Fork and clone the lab repository. [https://github.com/uofa-cmput404/cgi-lab](https://github.com/uofa-cmput404/cgi-lab)

    * (Reccomended) Activate a python3 virtual environment

2. Start the `cgi_server.py` in a background terminal window.
3. Initialize an empty file (this will be your CGI script).

    `touch hello.py`

4. Make your CGI script executable.

    `chmod +x hello.py`

5. Make the very first line of your CGI script the shebang:

    `#!/usr/bin/env python`

6. Examine the environment variables given to the CGI script.

    **Question 1**: How do you inspect all environment variables in Python?

7. Make your CGI script serve the environment back as JSON.
8. What changes if we add query parameters?
9. Modify your CGI script to report the values of the query parameters in the HTML.

    **Question 2**: What environment variable contains the query parameter data?

10. Modify your CGI script to report the user’s browser in the HTML.

    **Question 3**: What environment variable contains information about the user’s browser?

11. Modify your CGI script to contain a login form that POSTs to itself. You may use `login_page()` in templates.py.
12. Modify your CGI script to report the values of the POSTed data in the HTML.

    **Question 4**: How does the POSTed data come to the CGI script?

13. Edit the username and password in secret.pyand delete the raiseline; then import it in your login CGI script.
14. Modify your CGI script to set a cookie if the login is correct.

    **Question 5**: What is the HTTP header syntax to set a cookie from the server?

15. Modify your CGI script so it displays a secret message if the cookie says the user is logged in. You may use `secret_page()` from templates.py.
16. Steal the cookie using proxy.py.

    **Question 6**: What is the HTTP header syntax the browser uses to send the cookie back?

17. Clear the cookie in the browser or use a private/incognito browser window
18. Use the cookie to appear to be logged in to the CGI script without logging in.
    * Within the JavaScript console, enter: `document.cookie = "key=value"`
