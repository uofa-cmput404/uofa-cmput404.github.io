Title: HTTP Lab
date: 2024-07-17
tags: curl, http, socket, socketserver <!-- @LT-IGNORE:MORFOLOGIK_RULE_EN_CA(http)@ -->
authors: Hazel Victoria Campbell, Samuel Iwuchukwu, Sadia Zahin Prodhan
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking

----

<style>
    html body main {
        background-image: url("/theme/draft.png");
        background-repeat: repeat;
        background-size: 100%;
    }
</style>

[TOC]

---

# Description

Your task is to build an HTTP/1.1 compliant webserver and a basic HTTP client. This lab is designed to give you a hands-on, ground-up understanding of the basics of HTTP by implementing both the client and server sides.

The webserver will serve static content from the `www` directory in the same directory where you start the webserver. The client will be used to make HTTP requests to the server or any HTTP/1.1 server.

# Getting Started

1. Clone the GitHub classroom repository from eClass.
2. Follow the instructions below to implement the client and server.

# Collaboration

* You may consult with others (exchange high-level ideas) but the submission should be your own source code.
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/labs.md#lab-marking)
* **Yes, the instructors and TAs are all aware that ChatGPT can solve this assignment.**
    * There are also plenty of solutions all over the internet... that's the reason ChatGPT can solve it.
    * You are not being graded on your ability to use an LLM or google for a solution. Instead, you are being graded on your ability to understand how HTTP and network communications work.
    * If you cannot explain your solution to the TA and instructor, you will get a mark of zero.
    * If you use code from a LLM "AI" or from somewhere else, you must cite it, or you will be written up for plagiarism. See the outline for how to cite it.
    * Here are the only code you don't have to cite:
        * Code from this course's slides
        * The starter code from GitHub Classroom
        * Code written by an instructor or TA and hosted on this website: `uofa-cmput404.github.io`

# User Stories

* As a user, I want to view files in `./www` via a web browser and curl to see and test my website.
* As a webserver admin, I want to serve HTML and CSS files from `./www` and deeper to avoid dealing with other file types and to enhance security.
* As a user, I want the client to send an HTTP request to the server, so I can receive the appropriate response based on the request method
* As a developer, I want my custom client to interact with a standard server and my custom server to interact with a standard client. My custom client should also be able to interact with my custom server.

# Task 1: Implement the HTTP Client

## Client Requirements

* A single python program called `httpclient.py`
* Run it by using a command like:
    * `httpclient.py GET http://servername:port/path`
    * or `httpclient.py GET http://127.0.0.1:port/path` (or another ipv4 address)
    * or `httpclient.py GET http://[::1]:port/path` (or another ipv6 address)
    * or `httpclient.py POST http://servername:port/path` (or an ipv4/ipv6 address)
* Connect to a server at an address and port specified on the command line.
* Send request with appropriate headers.
* Receive and process responses from the server.
* Implement basic HTTP GET
* Implement basic HTTP POST
* HTTP POST can post vars
* HTTP POST handles at least Content-Type: application/x-www-form-urlencoded
* Handle 404 requests and 200 requests
* Handle a wider range of status codes (e.g., 301 for redirects, 500 for server errors) and act accordingly
* Support virtual hosting by correctly setting the Host header in GET and POST requests
* Pass the free-tests
 
To make your client communicate with the server, follow these steps:
  - Import the libraries needed (socket)
  - Create a Context Manager
  - Connect to server and send request
  - Receive and Process Responses

## Import the python socket module


```python
import socket
```

## Create a context manager

Create a context manager to ensure you close the socket once the block of code is executed.
Utilize the context manager on the socket module to create a new socket object. This object has an overloaded constructor. The two arguments to the constructor are the address family and the socket type. (i.e. socket.AF_INET and socket.SOCK_STREAM)

1. socket.AF_INET : represents the address type (for IPv4, IPv6, and DNS names)
2. socket.SOCK_STREAM : represents the socket type (TCP socket)

## Correctly parse URL

1. Make sure it starts with `http://` or stop with an error.
    * We do not support HTTPS in this lab.
2. Separate the IP address, port, and path.
    * If the port is not specified, use the default port 80.
    * If the IP address is a IPv6 address, remove the square brackets around it.
3. Make sure the path is percent decoded.
    * You do not need to percent decode anything but the path.
4. You do not need to handle query or fragment parts.

## Connect to a remote socket at specified address

Connect to a remote socket at specified address. This uses the socket.connect(address) method to connect with the host address. The address is a tuple that holds the host or IP address and the port number of the server

```python
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
   sock.connect((HOST,PORT))
   print(f"connected to server at host {HOST} and port {PORT}")
```

## Prepare your request

This would be correctly formatted to include the HTTP method, protocol, Host address, Content-Type and Content length and finally the data.

* Hint: don't forget the headers end with a blank line!

##  Pass your request byte as a parameter to socket.sendall function


Call the sendall function that accepts raw bytes to send the request to the server. Remember data is transmitted as bytes over the internet  and not strings. To convert the request string message to a byte, you encode the request using the utf-8 encoding.

```python
sock.sendall(request.encode("utf-8"))

```

## Process and receive response
<!-- TODO: replace this with the socket.makefile code  (DONE) -->

The "read_response" function reads the entire HTTP response from a server after a request has been made through a socket connection. It converts the socket into a file-like object (sock_file) using the makefile('rb') method, which allows the response to be read as raw bytes. The makefile() method simplifies the process of reading from and writing to the socket by providing file-like methods (read, write, etc.), making it easier to handle network communication. The function reads all the data from the server in one go and stores it in a byte string called response. Finally, it returns this byte string, containing the full response, including headers and any accompanying data, such as HTML content or binary files. 

```python
# Receive the response
   def read_response(self):
        response = b""
        with self.socket.makefile('rb') as sock_file:  
            response = sock_file.read()
        return response
    

```

# Task 2: Implement the HTTP Server

## Server Requirements

* Serve files from `./www`.
* Serve HTML and CSS files correctly with appropriate `Content-Type` headers.
* Serve `index.html` when directories (paths ending in `/`) are accessed.
* Serve 404 errors for non-existent paths.
* Serve a `405 Method Not Allowed` response for unsupported HTTP methods (like POST, PUT, DELETE).
* Use a `301 Moved Permanently` redirect for directory paths not ending in `/`.
* Serve files properly with Firefox and Chromium-based browsers.
* Serve CSS correctly so that the front page has an orange `h1` header.
* Tests must execute within 60 seconds.
* The server must be started by calling the `main` function.
* The server must handle requests from both custom and standard clients.
* Pass the free-tests

Getting your server to talk to a client involves the following steps

- Import the libraries needed (socketserver and pathlib)
- Create a custom server class to inherit from the TCPServer class
- Create the custom HttpHandler class
- Implement the handle method
    - Receive and decode request
    - Extract the method and path from the request line
    - Extract the headers and store in a dictionary
    - Decide the action to take based on the Http method type

- Start the server 


## Import the libraries needed (socketserver and pathlib)

The socketserver provides simplicity for creating network servers in python. The pathlib module is useful for managing filesystem path

```python
import socketserver
import pathlib
```

## Create a custom server class to inherit from the TCPServer class

Create a custom server class and make it inherit from the socketserver.TCPServer class. This is the first step in setting up a server, There are four basic servers available within the socketserver module namely TCPServer, UDPServer,UnixStreamServer and UnixDatagramServer

```python
class LabHttpTcpServer(socketserver.TCPServer):
   allow_reuse_address = True
```
## Create the custom HttpHandler class

Create the custom HttpHandler class by inheriting the socketserver.StreamRequestHandler to handle incoming requests. We utilized the socketserver.StreamRequestHandler class, a subclass of socketserver.BaseRequestHandler  because it provides implementation for rfile and wfile.

```python
class LabHttpTCPHandler(socketserver.StreamRequestHandler)
```

## Implement the handle method

This would involve some substeps

### Receive and decode request

The rfile would be utilized to receive and decode the request sent from the client. Simply call the readline() method which calls the recv() method multiple times until a new character line is reached

```python
# Receive and decode the request
       request_line = self.rfile.readline().strip().decode('utf-8')
```

### Extract the method and path from the request line

The split method is used to divide the request into three different parts because the 2 ensure split is done only twice. The first line in a request_line always contains the HTTP METHOD  PATH and HTTP_Version.
For example GET  /index.html  HTTP/1.1 would be split into
    
    GET
    /index.html
    HTTP/1.1
    
The underscore is a convention used for values that would be ignored in our case the HTTP version

```python
# Extract the method and path from the request
       method, path, _ = request_line.split(' ', 2)
```

### Extract the headers and store in a dictionary

We created a custom method to handle this. We split the line using the colon delimiter to ensure the split is done on the content type

```python
def parse_headers(self):
       headers = {}
       while True:
           line = self.rfile.readline().strip().decode('utf-8')
           if not line:
               break
           key, value = line.split(":", 1)
           headers[key.strip()] = value.strip()
       return headers
```

### Decide the action to take based on the Http method type

All other method other than GET and POST are met with a 405 error

##  Serve Multiple IP Addresses from a Single Domain
Implementation for serving multiple IP addresses from a single domain. Get the host header to determine the domain and apply this to the path

```python
# Get the Host header to determine the domain
       host = headers.get('Host', '')


       # Base directory to serve files from
       base_dir = pathlib.Path(f"www/{host}").resolve()
       # Parse and sanitize the path
       sanitized_path = base_dir / pathlib.Path(path.lstrip('/')).resolve()

```
## Start the server

Start the server by calling the serve_forever method and pass the HOST, PORT

```python
def main():
   with LabHttpTcpServer((HOST,PORT),LabHttpTCPHandler) as server:
       print("server is starting")
       print("running")
       server.serve_forever() 
```
# Task 3: Testing

## Scenario 1 : Ensure that your custom client can send requests to your custom server and receive the expected response

You have implemented both a custom HTTP client and server. The server serves files from a directory and handles different types of HTTP requests (e.g., GET, POST).
Use your custom client to send a GET request to your custom server to retrieve a specific file (e.g., index.html).
Your client should receive the correct HTML content from the server, indicating that the file was successfully served. The response should include the correct status code (200 OK) and appropriate headers.

## Scenario 2: Verify that your custom client can interact with standard servers, correctly sending requests and processing responses.

Your custom client needs to be tested against a well-known, standard server like Google's web server. Use your custom client to send a GET request to google.com. Most servers (such as google) will only return a redirect to force your client to use encryption (HTTPS). If you test against a standard server like google, the client should receive a response containing the redirect.

Here are some standard HTTP test servers that support unencrypted HTTP/1.1. Make sure the servers correctly understand the GET and POST requests your client is making. Note these are all IPv4 only, because IST. These servers should return 200 OK. They also respond with a description of the way the server interpreted the request, so you can check that the server is interpreting it correctly.

* Dr. Campbell's
    * <http://buttercup.cs.ualberta.ca:9000/> (get and post, IPv4 only)
    * <http://129.128.184.44:9000/>
* Dr. Hindle's
    * <http://webdocs.cs.ualberta.ca/~hindle1/1.py>
    * <http://webdocs.cs.ualberta.ca/~hindle1/2.cgi>
    * <http://129.128.243.190/~hindle1/1.py>
    * <http://129.128.243.190/~hindle1/2.cgi>
* <http://httpbin.org/get> (get only)
* <http://httpbin.org/post> (post only)

## Scenario 3: Ensure that standard clients (web browsers, Postman, curl) can communicate with your custom server and receive the correct responses.

You want to verify that your custom server can handle requests from standard clients, such as [Postman](https://www.postman.com/downloads/).
Use Postman to send a GET request to your custom server to retrieve 'index.html'. Then, use a web browser and curl to perform the same test. 
Postman should receive the correct content, with appropriate status codes and headers.



# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* Must run on Ubuntu (Use the undergrad lab machines, for example the ones in CSC 2-29 or install an Ubuntu VM to check this)
* Must work with Firefox
* The only allowed imports are `socketserver`, `re`, `socket`, and `pathlib`: You will receive a zero mark for using any other imports/libraries.
    * `re` library is optional, only use it if you know regular expressions.
    * Use of `urllib`, `http`, `requests`, and similar libraries is extra double forbidden and will result in a mark of `-0.0`. Please do not ask to use these libraries, they defeat the purpose of the assignment.
* Use of `recv` or `sendall` will result in 
* Your code must not modify the code out of its scope (must not do dependency injection), must not run anything at the top level (outside of functions/classes/defining constants), and must not try to work around or modify the test suite.

# Submission Instructions

Make sure you push to GitHub classroom **BEFORE 4PM on the day of your lab section!** You will not be able to push after that!

Submit a link to your repo in the form `https://github.com/uofa-cmput404/w24-h0x-labsignment-http-yourgithubname` on eClass. **Do not** submit a link to a branch, a file, or the clone URL. If you do not do this we will not know which GitHub submission is yours.

# Tips

## Ubuntu on Windows

Install Ubuntu on Windows using WSL2. 

Installing Ubuntu on Windows

Step 1-  Search for Windows PowerShell in your Windows search bar, then select Run as administrator.

At the command prompt type:
wsl --install
And wait for the process to complete.
For WSL to be properly activated, you will now need to restart your computer.

Step 2- WSL supports a variety of Linux distributions, including the latest Ubuntu release, Ubuntu 20.04 LTS and Ubuntu 18.04 LTS. You can find them by opening the Microsoft store app and searching for Ubuntu.

Choose the distribution you prefer and then click on Get.

Ubuntu will then install on your machine.

The one line install!

There is a single command that will install both WSL and Ubuntu at the same time.

When opening PowerShell for the first time, simply modify the initial instruction to:

wsl --install -d ubuntu

This will install both WSL and Ubuntu! Don’t forget to restart your machine before continuing.

Once installed, you can either launch the application directly from the store or search for Ubuntu in your Windows search bar.

 Step-3 Configure Ubuntu
 
Congratulations, you now have an Ubuntu terminal running on your Windows machine!

If Ubuntu returns an error during this initial installation, then the most common issue is that virtualisation is disabled in your device’s BIOS menu. You will need to turn this on during your device’s boot sequence. The location of this option varies by manufacturer, so you will need to refer to their documentation to find it.
Once Ubuntu has finished its initial setup you will need to create a username and password (this does not need to match your Windows user credentials).

Finally, it’s always good practice to install the latest updates with the following commands, entering your password when prompted.

sudo apt update

Then

sudo apt upgrade

Press Y when prompted.

Step - 4 Install your first package

Installing packages on Ubuntu is as easy as using a single command. Below, you will see how to install bpython, a simple python interpreter for trying out ideas, featuring some nice usability features like expected parameters and autocompletion.
To check that you have the latest package lists, type:

sudo apt update

Then install bpython:

sudo apt install bpython

To run the application type:

bpython

And you’re ready to go!

Step- 5 Customizing your terminal with Windows Terminal Preview

Since you’re likely to be using your Ubuntu terminal a fair bit, it’s always nice to do some customisation. We recommend installing Windows Terminal Preview to get the most user-friendly setup. You can find it in the Microsoft Store. 

Windows Terminal allows you to open multiple Terminal instances as tabs, so you can have PowerShell running alongside Ubuntu. It also includes a number of customisation options. In the below screenshot, we’ve changed the tab name and color, and configured the terminal appearance to use the Tango Dark theme and the Ubuntu font!


These customisations can be applied universally using the Appearance menu in Settings or to individual profiles which each have their own Appearance menu. Try it yourself to find something you feel comfortable with!

## Ubuntu on macOS ARM:

1. Install UTM for macOS: https://mac.getutm.app/
2. Download Ubuntu image for ARM: https://ubuntu.com/download/server/arm
3. Open the UTM app and Select "Create a New Virtual Machine"
4. Select "Virtualize" followed by "Linux"
5. Browse for the Ubuntu iso file you downloaded
6. Select your desired VM memory and CPU configs
7. Give your VM a name and select "Save"
8. Run the VM
9. Follow the onscreen prompts, default options are sufficient
10. Once the configuration is complete, shutdown the VM and dismount the iso file
11. Start and log into your VM
12. Run: `sudo apt install ubuntu-desktop` and `reboot`
You should now have access to Ubuntu desktop.

For more details, you can read [this](https://jun1okamura.medium.com/install-ubuntu-on-mac-m1-powered-by-utm-499aba3ba7e9).

## For macOS with homebrew:

1. `brew install git`
2. `brew install python@3`
3. `sudo pip3 install virtualenv`
4. In your repository directory, `virtualenv venv --python=python3`
5. Activate the virtual environment: `source venv/bin/activate`
6. Install requests: `pip3 install requests`


## For Windows 10 with pip:

Installing Python for Windows

Step 1- Downloading the Python Installer

Go to the official Python download page for Windows.
Find a stable Python 3 release. This tutorial was tested with Python version 3.10.10.
Click the appropriate link for your system to download the executable file: Windows installer (64-bit) or Windows installer (32-bit).

Step 2- Running the Executable Installer

1. After the installer is downloaded, double-click the .exe file, for example python-3.10.10-amd64.exe, to run the Python installer.
   
2. Select the Install launcher for all users checkbox, which enables all users of the computer to access the Python launcher application.
   
3. Select the Add python.exe to PATH checkbox, which enables users to launch Python from the command line.


4. If you’re just getting started with Python and you want to install it with default features as described in the dialog, then click Install Now and go to Step 4 - Verify the Python Installation. To install other optional and advanced features, click Customize installation and continue.

5. The Optional Features include common tools and resources for Python and you can install all of them, even if you don’t plan to use them.

Select some or all of the following options:

Documentation: recommended

pip: recommended if you want to install other Python packages, such as NumPy or pandas

tcl/tk and IDLE: recommended if you plan to use IDLE or follow tutorials that use it

Python test suite: recommended for testing and learning

py launcher and for all users: recommended to enable users to launch Python from the command line

6. Click Next.
   
7. The Advanced Options dialog displays.

Select the options that suit your requirements:

Install for all users: recommended if you’re not the only user on this computer

Associate files with Python: recommended, because this option associates all the Python file types with the launcher or editor

Create shortcuts for installed applications: recommended to enable shortcuts for Python applications

Add Python to environment variables: recommended to enable launching Python

Precompile standard library: not required, it might down the installation

Download debugging symbols and Download debug binaries: recommended only if you plan to create C or C++ extensions

Make note of the Python installation directory in case you need to reference it later.

8. Click Install to start the installation.
   
9. After the installation is complete, a Setup was successful message displays.

Step 3- Adding Python to the environment variables.

Skip this step if you selected Add Python to environment variables during installation.
If you want to access Python through the command line but you didn’t add Python to your environment variables during installation, then you can still do it manually.
Before you start, locate the Python installation directory on your system. The following directories are examples of the default directory paths:

C:\Program Files\Python310: if you selected Install for all users during installation, then the directory will be system wide

C:\Users\Sammy\AppData\Local\Programs\Python\Python310: if you didn’t select Install for all users during installation, then the directory will be in the Windows user path

Note that the folder name will be different if you installed a different version, but will still start with Python.

Go to Start and enter advanced system settings in the search bar.

Click View advanced system settings.

In the System Properties dialog, click the Advanced tab and then click Environment Variables.
Depending on your installation:

If you selected Install for all users during installation, select Path from the list of System Variables and click Edit.
If you didn’t select Install for all users during installation, select Path from the list of User Variables and click Edit.
Click New and enter the Python directory path, then click OK until all the dialogs are closed.

Step-4 Verify Python Installation

You can verify whether the Python installation is successful either through the command line or through the Integrated Development Environment (IDLE) application, if you chose to install it.
Go to Start and enter cmd in the search bar. Click Command Prompt

Enter the following command in the command prompt:

python --version

You can also check the version of Python by opening the IDLE application. Go to Start and enter python in the search bar and then click the IDLE app, for example IDLE (Python 3.10 64-bit).

You’ve successfully installed Python on your Windows system.

In cmd (not powershell):

1. pip install requests
2. pip install virtualenv
3. In your repository directory, `virtualenv venv --python=python3`
    * if you get the error "virtualenv not found" try forcing a reinstall with pip install virtualenv --force-reinstall
4 To activate: venv\Scripts\activate

As of 2018 all Windows 10 machines come pre-installed with curl, so you should have it already.  

## Ubuntu Lab Computers

Connect to one of the lab machines at the University if needed. 

They are named like `ug01.cs.ualberta.ca`, `ug02.cs.ualberta.ca`, all the way up to `ug34.cs.ualberta.ca`:

`ssh yourccid@ugXX.cs.ualberta.ca`

For example:

`ssh hazelcam@ug15.cs.ualberta.ca`

To quit the ssh connection to the lab machine, use the exit command or press control-D on a blank prompt. If that does not work you can force close the connection by pressing enter, then ~, then .

**Want to view stuff in terminal but it scrolled off the top of the page?**

Try using the more command to scroll page by page. For example, you can pipe the output of curl to more to scroll through the output of curl page by page:

```.sh
curl -s url | more
```

(The `-s` option to curl prevents curl from displaying download progress. You can combine it with other curl options like `-i` and `-L`.)
