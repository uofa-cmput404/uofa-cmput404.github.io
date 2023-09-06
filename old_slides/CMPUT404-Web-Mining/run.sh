#!/bin/bash
python -m SimpleHTTPServer 8181 &
chromium-browser http://localhost:8181/
