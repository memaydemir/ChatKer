#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import tornado.ioloop
import os
import tornado.options
import tornado.web

from tornado.options import define, options
from url import URL
from etc import config

define("port", default=8080, help="run on the given port", type=int)

SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    )

SETTINGS.update(config.tornado_settings)
application = tornado.web.Application(URL, **SETTINGS)


def main():
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
