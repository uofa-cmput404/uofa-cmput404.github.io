Title: Lab - TCP Proxy
Date: 2019-01-07 8:30
Modified: 2023-09-18 19:14
Category: Lab
Tags: tcp, proxy, socket
Authors: Alexander Wong

----

Create a tcp client, proxy server, echo server in Python. Understand how sockets work in relation to web requests. Use [multiprocessing](https://docs.python.org/3.4/library/multiprocessing.html?highlight=process) for forking new processes.

Answers to the questions should be submitted to *Lab: TCP Proxy* on eClass.

* [Python socket documentation](https://docs.python.org/3/library/socket.html)
* [w3 HTTP 1.0 Specification](https://www.w3.org/Protocols/HTTP/1.0/spec.html)
    * Also good: [Intro to HTTP 1.0](https://tecfa.unige.ch/moo/book2/node93.html)

### Sockets

Create a github repository for this lab and initialize a clean Python3 virtual environment.

1. Make a file called *client.py* which uses the [socket](https://docs.python.org/3/library/socket.html) library to connect to `www.google.com` and requests a page.

2. Make your program output whatever was sent to it onto the terminal.

    * **Question 1**: How do you specify a TCP socket in Python?

3. Make a file called *echo_server.py* that listens for incoming connections and echos any received data.

    * Test echoing example: `$ echo "Foobar" | nc localhost 8001 -q 1` should return Foobar, provided the port used is `8001`

    * **Question 2**: What is the difference between a client socket and a server socket in Python?

4. Print out information about what is connected to the server socket to the terminal.

    * **Question 3**: How do we instruct the OS to let us reuse the same bind port?

    * **Question 4**: What information do we get about incoming connections?

5. Print out whatever is sent to your server program.

    * **Question 5**: What is returned by `recv()` from the server after it is done sending the HTTP request?

6. Create a file called *proxy_server.py* and connect to Google. Create a file called *proxy_client.py* and connect to your proxy server.

7. Forward whatever is received on the server socket to `www.google.com`. Take the response from `www.google.com` and send it to the original connection.

8. Make your proxy server and echo server forking so multiple programs can use it simultaneously.

9. Push your code to GitHub.

    * **Question 6**: Provide a link to your code on GitHub.
