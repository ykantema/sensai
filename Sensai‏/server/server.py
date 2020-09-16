from flask import Flask, request
from server import calc

app = Flask(__name__)


@app.route('/add/')
def add():
    return str(calc.add(int(request.args.get('x')), int(request.args.get('y'))))


@app.route('/double/')
def double():
    return calc.double(request.args.get('x'), request.args.get('y'))


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(debug=True)