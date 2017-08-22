from bottle import get, install, run
from bottleopenapi import OpenApi


@get("/", summary="test", produces={'random': int})
def example():  # auth argument is optional!
    return "ok"


install(OpenApi())
run(host="0.0.0.0", port="9988")
