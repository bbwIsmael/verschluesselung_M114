import random
from db import insert_counter


def generate_prime_number():
    # Bechum e zuefälligi Zahl
    num = random.randint(100, 1000)

    while True:
        # Falls die Zahl e Primzahl isch, gib sie zrugg
        if is_prime(num):
            return num
        # Suscht addiere 1 und probiers wiiter (ab x addiert er 1 bis er die nöchst grösseri Primzahl usegfunde het)
        num += 1


def is_prime(num):
    # E Primzahl mues 2 oder grösser sii
    if num < 2:
        return False
    # Überprüef obs e Primzahl isch indem er über di quadrirti Zahl vo 0.5 + 1 iteriert (Mathe Formle)
    for i in range(2, int(num ** 0.5) + 1):
        # Wenn d'Zahl durch so e Zahl dividerbar isch, isches kei Primzahl
        if num % i == 0:
            return False
    return True


def hash_text(text):
    """ Hash en Text """

    hash_value = 0
    prime = generate_prime_number()

    # Iterier über jedes Zeiche im Text
    for char in text:
        # Multipliziere de Hash Wert mit de generierte Primzahl und addiere d'Unicode Zahl
        # Denn mach Modulo zum d'maximal Grössi festlegge
        hash_value = (hash_value * prime + ord(char)) % (2**32)

    insert_counter("Hash")
    # Schniide die erste 2 Zeiche weg damit das "0x" weg isch (wills e Hexadezimalzahl isch)
    return hex(hash_value)[2:]
