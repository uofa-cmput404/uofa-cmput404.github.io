#!/usr/bin/env python
# Copyright 2013 Abram Hindle
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# You can start this by executing it in python:
# python server.py
#
# remember to:
#     pip install flask

# Shared Chat 
#   for each message in
#      for each client
#         send message

import flask
from flask import Flask, request
from flask_sockets import Sockets
import gevent
from gevent import queue
import time
import json
import os
import string
import random
import sys
import hashlib

def rndstr(n=50):
    return "".join([random.choice( string.ascii_letters ) for x in range(1,50)])

def read_time():
    '''A greenlet function that reads from time'''
    try:
        print("Try ")
        while True:
            print("1")
            str = time.strftime("%c")
            print("Send %s" % str)
            send_all( f'<div class="time">{str}</div>' )
            gevent.sleep(3)            
    except Exception as e:
        print(e)

def gstdin_readline():
    '''gevent doesn't play nice with all file handles'''
    gevent.select.select([sys.stdin], [], [])
    return sys.stdin.readline()

def read_stdin():
    '''A greenlet function that reads from a file handle'''
    try:
        while True:
            line = gstdin_readline()
            print("Send %s" % line)
            # send_all_json( {"msg":line} )
            send_all( f'<div class="stdin">{line}</div>')
    except Exception as e:
        print(e)

def gen_sha1():
    '''A greenlet function slowly searches for 2 zeros in a row!'''
    m = hashlib.sha1()
    hashes = 0
    try:
        while True:
            try:
                str_ = rndstr()
                hash = hashlib.sha1(str_.encode("UTF-8")).hexdigest()
                hashes += 1
                zeros = "0000"
                if (hash.index(zeros)>=0):
                    line = "%s [%s]=>[%s] [%s]" % (zeros, str_, hash, hashes)
                    print("Send %s" % line)
                    send_all(f'<div class="hash">{line}</div>')
                    gevent.sleep(1)
            except ValueError:
                gevent.sleep(0)
    except Exception as e:
        print(e)



gevents = list()

def setup():
    global gevents
    gevents += [gevent.spawn( read_time )]
    gevents += [gevent.spawn( read_stdin )]
    gevents += [gevent.spawn( gen_sha1 )]

def create_app():
    app = Flask(__name__)
    setup()
    return app

app = create_app()
sockets = Sockets(app)
app.debug = True

clients = list()



def send_all(msg):
    for client in clients:
        client.put( msg )

def send_all_json(obj):
    send_all( json.dumps(obj) )

class Client:
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, v):
        self.queue.put_nowait(v)

    def get(self):
        return self.queue.get()


@app.route('/')
def hello():
    return flask.redirect("/static/exercise.html")



def read_ws(ws,client):
    '''A greenlet function that reads from the websocket'''
    try:
        while True:
            msg = ws.receive()
            print("WS RECV: %s" % msg)
            if (msg is not None):
                '''Do nothing'''
                #packet = json.loads(msg)
                #send_all_json( packet )
            else:
                break
    except:
        '''Done'''

@sockets.route('/tweets')
def subscribe_socket(ws):
    client = Client()
    clients.append(client)
    g = gevent.spawn( read_ws, ws, client )    
    print("Subscribing")
    try:
        while True:
            # block here
            msg = client.get()
            print("Got a message!")
            ws.send(msg)
    except Exception as e:# WebSocketError as e:
        print("WS Error %s" % e)
    finally:
        clients.remove(client)
        gevent.kill(g)




if __name__ == "__main__":
    # cheap hack
    os.system("bash run-exercise.sh");

