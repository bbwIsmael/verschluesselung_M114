from flask import Flask, render_template, request
import sys
sys.path.append('./functions')

from functions.blowfish import blowfish_encrypt, blowfish_decrypt
from functions.caesar import caesar
from functions.hash import hash_text
from functions.xor import xor

app = Flask(__name__)


from functions.db import setup_db
setup_db()


@app.route('/', methods=["GET"])
def titel():  # put application's code here
    return render_template("index.html", titel=titel)


# Blowfish schnittstellene
@app.route('/blowfish/encrypt', methods=["GET"])
def blowfish_enc():
    text = request.args.get("text")
    key = request.args.get("key")

    if not text or not key:
        return "Ey gib mal en text oder en key mit!"

    return blowfish_encrypt(text, key)


@app.route('/blowfish/decrypt', methods=["GET"])
def blowfish_dec():
    text = request.args.get("text")
    key = request.args.get("key")

    if not text or not key:
        return "Ey gib mal en text oder en key mit!"

    return blowfish_decrypt(text, key)


# Caesar schnittstellene
@app.route('/caesar/encrypt', methods=["GET"])
def caesar_encrypt():
    text = request.args.get("text")
    shift = int(request.args.get("shift"))

    if not text or not shift:
        return "Ey gib mal en text oder en shift mit!"

    return caesar(text, shift)


@app.route('/caesar/decrypt', methods=["GET"])
def caesar_decrypt():
    text = request.args.get("text")
    shift = int(request.args.get("shift"))

    if not text or not shift:
        return "Ey gib mal en text oder en shift mit!"

    # Verwandle de shift in negativ damit er entschlüsslet (anstatt verschlüsslet)
    return caesar(text, -shift)


# Hash
@app.route('/hash', methods=["GET"])
def hash_it():
    text = request.args.get("text")

    if not text:
        return "Ey gib mal en text mit!"

    return hash_text(text)


# XOR schnittstellene
@app.route('/xor', methods=["GET"])
def xor_it():
    text = request.args.get("text")
    key = request.args.get("key")

    if not text or not key:
        return "Ey gib mal en text oder en key mit!"

    return xor(text, key)


if __name__ == '__main__':
    app.run()
