from flask import Flask, render_template

app = Flask(__name__)




@app.route('/', methods=["GET"])
def titel():  # put application's code here
    return render_template("index.html", titel=titel)


if __name__ == '__main__':
    app.run()
