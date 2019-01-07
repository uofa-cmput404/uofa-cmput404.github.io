Title: Lab 2 - TCP Proxy
Date: 2019-01-07 8:30
Modified: 2019-01-07 11:50
Category: Lab
Tags: tcp, proxy, socket
Authors: Alexander Wong

----

Create a multi-client tcp proxy client in Python.

Answers to the questions should be submitted to *Lab 2* on eClass.

### Sockets

1. Make a socket client in Python that connects to google and requests a page.

2. Make your program output whatever was sent to it onto the terminal.

    * **Question 1**: How do you specify a TCP socket in Python?

3. Make a new program that listens for incoming connections.

    * **Question 2**: What is the difference between a client socket and a server socket in Python?

4. Print out information about what is connected to the server socket to the terminal.

    * **Question 3**: How do we instruct the OS to let us reuse the same bind port?

    * **Question 4**: What information do we get about incoming connections?

5. Print out whatever is sent to your server program.

6. Connect a client socket to Google.

7. Forward whatever is received on the server socket to the client socket.

8. Forward whatever is received on the client socket to the server socket.

    * **Question 5**: What is returned by recv() from the server after it is done sending the HTTP request?

9. Make your proxy server forking so multiple programs can use it.

10. Push your code to GitHub.

    * **Question 6**: Provide a link to your code on GitHub.
