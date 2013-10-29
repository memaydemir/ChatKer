#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import tornado.websocket
import logging
import tornado.escape
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.set_secure_cookie("user", str(uuid.uuid4()))
        self.render("index.html", messages=ChatSocketHandler.cache)


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    pool = {}
    cache = []
    cache_size = 200
    index = 0

    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True

    def open(self):
        print "new client opened"
        ChatSocketHandler.index = ChatSocketHandler.index + 1;
        self._index = ChatSocketHandler.index
        ChatSocketHandler.pool[self._index] = self

    def on_close(self):
        del ChatSocketHandler.pool[self._index]

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, sock_index, chat):
        logging.info("sending message to %d waiters", len(cls.pool))
        if sock_index % 2 == 0:
            target = sock_index - 1
        else:
            target = sock_index + 1

        if target in cls.pool:
            try:
                cls.pool[target].write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)
        else:
            logging.error("still not available chater ", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        ChatSocketHandler.send_updates(self._index, message)
