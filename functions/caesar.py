from db import insert_counter

# Shift isch entweder positiv (denn verschlüsslet er) oder negativ (denn entschlüsslet er)
def caesar(text, shift):
    """
        Verschlüssle oder Entschlüssle en Text mit Caesar

        - Positive "Shift" => Verschlüssle
        - Negative "Shift" => Entschlüssle
    """

    end_text = ""
    # Über jedes Zeiche wird drüber iteriert
    for char in text:
       # Überprüef obs Zeiche alphabetisch isch (a-Z) suscht gib s'Zeiche direkt wiiter
        if char.isalpha():
            # Wenn s'Zeiche gross buechstabig isch, mues es andersch "verschobe" werde
            if char.isupper():
                # D'Unicode Zahl wird um 65 subtrahiert weil 65 im Unicode Alphabet de Buechstabe "A" isch
                # Nachher wird de "shift" hinzuegfüegt und denn mit Modulo 26 (wege 26 Buechstabe im Alphabet) usgrechnet.
                # Als nöchstes wird die 65 wieder zue addiert damit au en Buechstabe usechunt
                # Zum Schluss wird de Unicode mit dere Zahl (mit de chr() Funktion) zum Endtext hinzuegfüegt
                end_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                end_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            end_text += char

    insert_counter("Caesar")
    return end_text
