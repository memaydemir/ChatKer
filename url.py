#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import tornado.web

URL = [
        (r"/", "app.base.MainHandler"), 
        (r"/websocket", "app.base.ChatSocketHandler"), 
    ]
