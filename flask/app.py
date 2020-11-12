from flask import Flask
from modules.Connection import Connection


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)