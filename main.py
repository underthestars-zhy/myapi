#! /usr/local/bin/python3
#   Copyright (c) 2021.
#   You can freely change the code part, but you must follow the MIT protocol
#   You cannot delete any information about UTS
#   You cannot use this program to disrupt social order.

import tornado.ioloop
import tornado.web
import json
import random


class RandomHandler(tornado.web.RequestHandler):
    def get(self, num_1, num_2):
        json_dict = {
            0: random.randint(int(num_1), int(num_2)),
            1: random.randint(int(num_1), int(num_2)),
            2: random.randint(int(num_1), int(num_2)),
        }
        self.write(json.dumps(json_dict))

def make_app():
    return tornado.web.Application(
        [
            (r"/random/(\d+),(\d+)", RandomHandler)
        ]
    )

if __name__ == '__main__':
    app = make_app()
    app.listen(7777)
    tornado.ioloop.IOLoop.current().start()
