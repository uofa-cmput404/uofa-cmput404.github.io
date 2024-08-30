title: HTTP Lab2
date: 2024-07-17
tags: socket, http, socketserver
authors: Samuel Iwuchukwu, Hazel Victoria Campbell
status: published

----

[TOC]

# Task1

Your task is to implement a basic HTTP 1.1 client

# Getting Started

Building a basic client involves a series of steps as listed below

- Import the python socket module
- Create a context manager
- Connect to a remote socket at specified address
- Prepare your post request
- Pass your request byte as a parameter to socket.sendall function
- Process and receive response


## Import the python socket module

Here is a simple code snippet in Python:

```python
import socket
```

## Create a context manager

Create a context manager to ensure you close the socket once the block of code is executed
Utilize the context manager on the socket module to create a new socket object, This object has an overloaded constructor but we would utilize the two arguments constructor and pass the address family and the socket type. (i.e socket.AF_INET and socket.SOCK_STREAM)

1. socket.AF_INET : represents the address type (for IPv4)
2. socket.SOCK_STREAM : represents the socket type (TCP socket)

## Connect to a remote socket at specified address

Connect to a remote socket at specified address. This uses the socket.connect(address) method to connect with the host address. The address is a tuple that holds the host or ip address and the port number of the server

```python
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
   sock.connect((HOST,PORT))
   print(f"connected to server at host {HOST} and port {PORT}")
```

## Prepare your post request

This would be formatted to include the HTTP method,  protocol, Host address, Content-Type and Content length and finally the data

```python
# Prepare the HTTP POST request
   request = (
           "POST / HTTP/1.1\r\n"
           f"Host: {HOST}:{PORT}\r\n"
           "Content-Type: text/plain\r\n"
           f"Content-Length: {len(data)}\r\n"
           "\r\n"
           f"{data}"
       )
```

##  Pass your request byte as a parameter to socket.sendall function

Call the sendall function that accepts raw bytes to send the request to the server. Remember data is transmitted as bytes over the internet  and not strings. To convert the request string message to a byte, you encode the request using the utf-8 encoding.

```python
sock.sendall(request.encode("utf-8"))

```

## Process and receive response

We would utilize the recv method in socket class to receive response from the server. We need to create a bytes variable to accept responses. The recv() method takes the buffer size as an argument to capture the maximum amount of bytes to be received by the client. We set it 1024 for our case

```python
# Receive the response
   response = b""
   while True:
       part = sock.recv(1024)
       if not part:
           break
       response += part

```

# Task 2

Your task is to implement the server to talk to a normal client

# Getting Started

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

```python
if method == 'GET':
           self.serve_static_files(path)
       elif method == 'POST':
           content_length = int(headers.get('Content-Length', 0))
           post_data = self.rfile.read(content_length).decode('utf-8')


           self.serve_post_response(post_data)
       else:
           self.send_error(405, "Method Not Allowed")
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

# Task 3 

Your task is to serve multiple IP address from a single domain

# Getting Started

Implementation for serving multiple IP addresses from a single domain. Get the host header to determine the domain and apply this to the path

```python
# Get the Host header to determine the domain
       host = headers.get('Host', '')


       # Base directory to serve files from
       base_dir = pathlib.Path(f"www/{host}").resolve()
       # Parse and sanitize the path
       sanitized_path = base_dir / pathlib.Path(path.lstrip('/')).resolve()

```

# HTTP Client/Server Communication Diagram

![HTTP Client Server Communication](/Users/samueliwuchukwu/Documents/cmput404/code/uofa-cmput404.github.io/content/labsignments/images/http_diagram.png)

