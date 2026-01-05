Title: HTTP Lab
date: 2024-07-17
tags: curl, http, socket, socketserver, labs <!-- @LT-IGNORE:MORFOLOGIK_RULE_EN_CA(http)@ -->
authors: Hazel Victoria Campbell, Samuel Iwuchukwu, Sadia Zahin Prodhan
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking

----

[TOC]

<!-- <style>
    html body main {
        background-image: url("/theme/draft.png");
        background-repeat: repeat;
        background-size: 100%;
    }
</style>

**This is currently a draft. It will be finalized by Sept 15.**
 -->
 
# Description

Your task is to build an HTTP/1.1 compliant webserver and a basic HTTP client. This lab is designed to give you a hands-on, ground-up understanding of the basics of HTTP by implementing both the client and server sides.

The webserver will serve static content from the `www` directory in the same directory where you start the webserver. The client will be used to make HTTP requests to the server or any HTTP/1.1 server.

# Getting Started

1. Clone the GitHub classroom repository from Canvas.
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

# Task 0: Get an Environment with a Recent Python3 Version

[Make sure you have a working development environment with these instructions!]({filename}/general/environment.md)

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

* Client must have a `HTTPClient` class with a `command(self, method, url, args)` method.
    * `method` will be `'GET'` or `'POST'`
    * `url` will be a url including path, but not including query arguments or fragment
    * `args` will be a dict
        * This should become the query args for `GET`
        * This should become the posted body for `POST`
    * `command` method should return an `HTTPResponse`
* Client must have a `HTTPResponse` class .
    * It must have a `code` attribute which is an `int` response code like `200` for OK.
    * It must have a `body` attribute which is a `str` containing just the body. No headers.

## Import the python socket module

```python
import socket
```

## Connect to a remote socket at specified address

Use  the socket module to create a new socket object. This object has an overloaded constructor. The two arguments to the constructor are the address family and the socket type. (i.e. socket.AF_INET and socket.SOCK_STREAM)

1. socket.AF_INET : represents the address type (for IPv4, IPv6, and DNS names)
2. socket.SOCK_STREAM : represents the socket type (TCP socket)
Connect to a remote socket at specified address. This uses the socket.connect(address) method to connect with the host address. The address is a tuple that holds the host or IP address and the port number of the server

```python
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
   sock.connect((HOST,PORT))
   print(f"connected to server at host {HOST} and port {PORT}")
```

## Correctly parse URL

1. Make sure it starts with `http://` or stop with an error.
    * We do not support HTTPS in this lab.
2. Separate the IP address, port, and path.
    * If the port is not specified, use the default port 80.
    * If the IP address is a IPv6 address, remove the square brackets around it.
3. If it is a GET request, the params need to made into query parameters.
    * If it is a POST request the params should become the post body instead, and they should not be added to the query parameters.
4. The path and query params must be correctly percent encoded.



## Prepare your request

This would be correctly formatted to include the HTTP method, protocol, Host address, Content-Type and Content length and finally the data.

* Hint: don't forget the headers end with a blank line!

##  Pass your request byte as a parameter to socket.sendall function

Call the sendall function that accepts raw bytes to send the request to the server. Remember data is transmitted as bytes over the internet  and not strings. To convert the request string message to a byte, you encode the request using the utf-8 encoding.

```python
sock.sendall(request.encode("utf-8"))

```

## Process and receive response

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
* The server must correctly percent decode incoming paths.
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
class LabServer(socketserver.TCPServer):
   allow_reuse_address = True
```
## Create the custom HttpHandler class

Create the custom HttpHandler class by inheriting the socketserver.StreamRequestHandler to handle incoming requests. We utilized the socketserver.StreamRequestHandler class, a subclass of socketserver.BaseRequestHandler  because it provides implementation for rfile and wfile.

```python
class LabServerTCPHandler(socketserver.StreamRequestHandler)
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

All other method other than GET are met with a 405 error

## Start the server

Start the server by calling the serve_forever method and pass the HOST, PORT

```python
def main():
   with LabServer((HOST,PORT),LabServerTCPHandler) as server:
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

## Hints
* For IPV6, use socket.AF_INET6 as the address family when creating the socket.
* GET should not have a body, and since GET doesn't have a body it should not have a Content-Type header at all. Instead, when given arguments, GET should add them to the query part of the URL and send that along with the path when making the GET request.
* When given vars, POST should include a body that is urlencoded and Content-Type: application/x-www-form-urlencoded .
* The Wikipedia page on percent encoding actually has a great explanation of what characters are allowed. They are the unreserved characters. However, you need to also make sure you allow / (forward slash) in paths. https://en.wikipedia.org/wiki/Percent-encoding
* It's better to percent-encode all reserved characters except the "/". For example, if the path has a folder or file name with a "?" in it, you wouldn't want it to prematurely end the path and start the query. Same for "#".
* The port may not always be specified. In that case, the client must assume a default port value (which for HTTP is 80)
* Use "Connection: close" header on both sides
* Check the "Content-Type" header to see if the encoding is ISO-8859-1 or UTF-8 on the client
* You can turn unicode into a byte string with Python's built-in .encode() method of strings. For example. "❤️".encode() produces b'\xe2\x9d\xa4\xef\xb8\x8f' and coincidentally the correct percent-encoding is %E2%9D%A4%EF%B8%8F
* If a client sends a GET request to http://localhost:8000/index.html, the server should send them the contents of www/index.html in the HTTP response body.
* If a client sends a GET request to http://localhost:8000/base.css, the server should send them the contents of www/base.css in the HTTP response body.
* If a client sends a GET request to http://localhost:8000/deep/index.html, the server should send them the contents of www/deep/index.html in the HTTP response body.
* If a client sends a GET request to http://localhost:8000/deep/, the server should send them the contents of www/deep/index.html in the HTTP response body. (and deep is a directory therefore the specifications say to return the index.html file in the deep directory), you would also need to additionally send the correct redirect related headers and status code if the path does not end in a / but is a directory.
* The names of the directories/files aren't restricted to the files autogenerated. If I put a file in the www folder at www/test/test2/test3.css, then it should be accessible at http://localhost:8000/test/test2/test3.css
* To get an overview of HTTP requests and response you can visit-  https://developer.mozilla.org/en-US/docs/Web/HTTP 
* Check for both ISO-8859-1 and UTF-8 as some servers give a response in ISO-8859-1
* For this lab you do not need to construct an IPv6 header. You only need to construct an HTTP header.
* The client only needs to percent encode. The server needs to percent decode.

# Restrictions

Violation of the restrictions will result in a mark of zero.

* Must use Python3
* Must run on Ubuntu (Use the undergrad lab machines, for example the ones in CSC 2-29 or install an Ubuntu VM to check this)
* Must work with Firefox
* The only allowed imports are `socketserver`, `re`, `socket`, `pathlib`, and `argv`: You will receive a zero mark for using any other imports/libraries.
    * `re` library is optional, only use it if you know regular expressions.
    * Use of `urllib`, `http`, `requests`, and similar libraries is extra double forbidden and will result in a mark of `-0.0`. Please do not ask to use these libraries, they defeat the purpose of the assignment.
* Your code must not modify the code out of its scope (must not do dependency injection), must not run anything at the top level (outside of functions/classes/defining constants), and must not try to work around or modify the test suite.

# Submission Instructions

Make sure you push to GitHub classroom **BEFORE the deadline!** You will not be able to push after that!

Submit a link to your repo in the form `https://github.com/uofa-cmput404/f25-labsignment-http-yourgithubname/commit/bunch-of-numbers` on Canvas. **Do not** submit a link to a branch, a file, or the clone URL.

<p class="warning">If you do not submit a link to your COMMIT on Canvas on time using the correct format above, you will get a zero.</p>

You can submit and then resubmit as many times as you want before the deadline, so submit early and often.

# Collaboration

* You may consult with others (exchange high-level ideas) but the submission should be your own source code.
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code. This includes code from LLMs.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/labs.md#lab-marking)
* For more information see the collaboration section in the outline: [{filename}/general/outline.md#consultation-assignments-labs]

# Tips

