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

import flask
from flask import Flask, request
import json
import difflib
import os
import os.path
from Crypto.Cipher import AES
from Crypto import Random
import urllib
#import urlparse
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import binascii
import hashlib

app = Flask(__name__)
app.debug = True


def flask_post_json():
    '''Ah the joys of frameworks! They do so much work for you
       that they get in the way of sane operation!'''
    if (request.json != None):
        return request.json
    elif (request.data != None and request.data != ''):
        return json.loads(request.data)
    else:
        return json.loads(request.form.keys()[0])


ourwords = []

def load_words():
    global ourwords
    words = open("server.py").read().split()
    x = dict()
    for word in words:
        x[word] = 1
    ourwords = list(x.keys())
    ourwords.sort()

def get_closest_words(entity, n):
    global ourwords
    print(ourwords)
    return difflib.get_close_matches(entity, ourwords, n, 0.1)

@app.route("/")
def hello():
    return flask.redirect("/static/index.html")

@app.route("/happybirthday")
def happy_birthday():
    name = request.args.get('name')
    return flask.render_template('happybirthday.html', name=name)

@app.route("/happybirthday2")
def happy_birthday2():
    name = request.args.get('name')
    if name is None:
        name = "World"
    str = open('templates/happybirthday2.html').read().replace("{{ name }}",name)
    return (str, 200, {"Content-type": "text/html"})

@app.route("/traverse")
def traverse():
    entity = request.args.get('entity')
    str = open(entity).read()
    return (str, 200, {"Content-type": "text/plain"})

@app.route("/traverse_sane")
def traverse_sane():
    entity = request.args.get('entity')
    path = os.path.abspath(entity)
    mycwd = os.getcwd()
    common = os.path.commonprefix([mycwd,path])
    if (len(common) >= len(mycwd)):
        str = open(entity).read()
        return (str, 200, {"Content-type": "text/plain"})
    else:
        flask.abort(403)

adcount = 0
@app.route("/ads")
def malicious_ad():
    global adcount
    adcount += 1
    if (adcount > 0 and (adcount % 3 == 0)):
        return flask.render_template('malice.html')
    else:
        return flask.render_template('worms.html')


key = b'ABCDEFGHIJKLKMNO'
def encrypt(msg):
    global key
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(bytes(msg,encoding='utf8'))
    print(type(msg),msg)
    return msg

def decrypt(msg):
    global key
    iv = msg[0:16]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(msg[16:])


@app.route("/auth")
def auth():
    defv = {"user":"username","admin":"0"}
    v =  None
    decrypted = ""
    if request.args.get('token'): 
        decrypted = decrypt(binascii.unhexlify(request.args.get('token'))).decode('unicode-escape')
        print(type(decrypted),decrypted)
        v = parse_qs( decrypted )
        for key in v:
            v[key] = v[key][0]
    else:
        v = defv
    print("Decrypted: [%s]" % decrypted)
    print(v)

    v["user"] = v.get("user",defv["user"])
    if request.args.get('user'):
        v["user"] = request.args.get('user')
    v["admin"] = v.get("admin",0)
    tosend = urlencode([("user",v["user"]),("admin",v["admin"])])
    token = encrypt( tosend )
    hextoken = binascii.hexlify(token).decode('unicode-escape')
    print(type(hextoken),hextoken)
    safe_decrypted = decrypted#.decode('unicode-escape')
    print(u"sd: %s " % safe_decrypted)
    safe_admin = str(v["admin"])#.decode('unicode-escape')
    safe_tosend = tosend#.decode('unicode-escape')
    safe_user = v["user"]#.encode('unicode-escape')
    return flask.render_template('auth.html', 
                                 admin=safe_admin,
                                 adminzero= v["admin"] == '0',
                                 adminone = v["admin"] == '1',
                                 decrypted = safe_decrypted,
                                 tosend = safe_tosend,
                                 hextoken = hextoken,
                                 user=safe_user)

# this is a safer example where we cannot modify it without breaking the hash
@app.route("/safe_auth")
def safe_auth():
    secret = "I really enjoy your company"
    defv = {"user":"username","admin":"0"}
    v =  None
    decrypted = ""
    def hashit(v,salt = None):
        if salt is None:
            iv =  Random.new().read(4)
            salt = binascii.hexlify(iv)
            salt = salt.decode('unicode-escape')
            print(type(salt),salt)
            print(type(secret),secret)
            print(type(v["user"]),v["user"])
            print(type(v["admin"]),v["admin"])
        hss = salt + secret + v["user"] + v["admin"]
        return (hashlib.sha224(hss.encode('utf-8')).hexdigest(), salt)
        
    if request.args.get('token'): 
        # decrypted = decrypt(binascii.unhexlify(request.args.get('token')))
        decrypted = decrypt(binascii.unhexlify(request.args.get('token'))).decode('unicode-escape')
        v = parse_qs( decrypted )
        for key in v:
            v[key] = v[key][0]
        # verify the token
        (h,salt) = hashit(v,v.get("salt",None))
        if not (h == v["h"]):
            print("Invalid hash! expected %s but got %s " % (h,v["h"]))
            flask.abort(403)
    else:
        v = defv
    print("Decrypted: [%s]" % decrypted)
    print(v)

    v["user"] = v.get("user",defv["user"])
    if request.args.get('user'):
        v["user"] = request.args.get('user')
    v["admin"] = v.get("admin",0)
    (h,salt) = hashit(v)
    tosend = urlencode([("h",h),("salt",salt),("user",v["user"]),("admin",v["admin"])])
    token = encrypt( tosend )
    #hextoken = binascii.hexlify(token)
    hextoken = binascii.hexlify(token).decode('unicode-escape')
    #safe_decrypted = str(decrypted).encode('unicode-escape')
    #safe_decrypted = decrypted.decode('unicode-escape')
    safe_decrypted = decrypted#decrypted.decode('unicode-escape')
    print("sd: %s " % safe_decrypted)
    #safe_admin = str(v["admin"]).encode('unicode-escape')
    #safe_tosend = tosend.encode('unicode-escape')
    #safe_user = str(v["user"]).encode('unicode-escape')
    safe_admin = str(v["admin"])#.decode('unicode-escape')
    safe_tosend = tosend#.decode('unicode-escape')
    safe_user = v["user"]#.encode('unicode-escape')
    return flask.render_template('auth.html', 
                                 admin=safe_admin,
                                 adminzero= v["admin"] == '0',
                                 adminone = v["admin"] == '1',
                                 decrypted = safe_decrypted,
                                 tosend = safe_tosend,
                                 hextoken = hextoken,
                                 user=safe_user)

    


if __name__ == "__main__":
    load_words()
    app.run()
