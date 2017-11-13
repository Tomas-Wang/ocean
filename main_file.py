#!/user/bin/env python
# --*-- encoding: utf-8 --*--
import tornado.ioloop
import tornado.web
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Thomas!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])


def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app, xheaders=True)
    server.bind(18888)
    server.start(1)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
