from bottle import route, run


@route("/hello/<name>")
def index(name):
    return f"<b>Hello {name}</b>!"

run(host="localhost", port=8080) 