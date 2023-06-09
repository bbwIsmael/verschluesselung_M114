from flask import Flask
import sys
sys.path.append('./functions')

app = Flask(__name__)


from functions.db import setup_db
setup_db()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
