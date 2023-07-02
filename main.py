#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dependencies
from os import system as cmd
cmd("pip install -r requirements.txt")

# start
from web_app import start_web_server

start_web_server()