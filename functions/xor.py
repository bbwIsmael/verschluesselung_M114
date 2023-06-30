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
        # Mues überprüefe ob er en string isch und denn andersch handle wege de ord() funktion
        if isinstance(char, str):
            # De Unicode vom aktuelle Zeiche
            char_code = ord(char)
        else:
            char_code = char

        # Mues überprüefe ob er en string isch und denn andersch handle wege de ord() funktion
        if isinstance(key[index % len(key)], str):
            key_code = ord(key[index % len(key)])
        else:
            key_code = key[index % len(key)]

        # Mach e XOR rechnig zwüsched de Unicode Zahle vom text und enere gwüsse Stell vom key
        xored_char = char_code ^ key_code
        # Füeg d'"xored" Zahl zu de Liste
        result.append(chr(xored_char))

    insert_counter("XOR")
    # Wandle die Liste no in en String um und gib sie zrugg
    return ''.join(result)