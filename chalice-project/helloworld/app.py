from chalice import Chalice

from chalicelib.utils import boom as boom_util

app = Chalice(app_name="helloworld")


@app.route("/boom")
def boom():
    request = app.current_request
    trigger = int(
        request.query_params["trigger"]
        if request.query_params and "trigger" in request.query_params
        else 0
    )

    return {"hello": boom_util(trigger)}


@app.route("/zero")
def zero():
    bla = 1 / 0
    return {"hello": "zero"}


@app.route("/")
def index():
    return {"hello": "world"}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#