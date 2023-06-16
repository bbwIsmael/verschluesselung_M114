from db import insert_counter


# Je nach dem was de key isch, ver-/entschlüsslet die Funtkion de text
def xor(text, key):
    """
        Verschlüssle oder Entschlüssle en Text mit XOR und eme key

        Je nach dem was de key isch, ver-/entschlüsslet die Funtkion de text
    """

    result = []
    # Iteriere über jedes Zeiche vom text drüber und bechum au grad de index (mit enumerate()) devo
    for index, char in enumerate(text):
        # Mach e XOR rechnig zwüsched de Unicode Zahle vom text und enere gwüsse Stell vom key
        xored_char = ord(char) ^ ord(key[index % len(key)])
        # Füeg d'"xored" Zahl zu de Liste
        result.append(chr(xored_char))

    insert_counter("XOR")
    # Wandle die Liste no in en String um und gib sie zrugg
    return ''.join(result)