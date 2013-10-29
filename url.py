#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
URL = [
        (r"/", "app.base.MainHandler"),
        (r"/websocket", "app.single.ChatSocketHandler"),
        (r"/chatRoom", "app.room.ChatSocketHandler"),
      ]
