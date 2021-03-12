def application(env, startResponse):
        startResponse("200 OK", [("Content-type", "text/plain")])
        return [b"See you at TeroKarvinen.com\n"]from DatabaseApp.py import app as application
