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


def main(port):
    app = make_app()
    server = tornado.httpserver.HTTPServer(app, xheaders=True)
    server.bind(port)
    server.start(1)
    print "Server started at PORT: %s" % port
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run_port = 8888
    main(run_port)
