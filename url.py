#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
URL = [
        (r"/", "app.single.MainHandler"),
        (r"/websocket", "app.single.ChatSocketHandler"),
        (r"/chatRoom", "app.room.ChatSocketHandler"),
      ]
