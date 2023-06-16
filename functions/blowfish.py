from Crypto.Cipher import Blowfish


def blowfish_encrypt(text, key):
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    encrypted_data = cipher.encrypt(text.encode())
    return encrypted_data


def blowfish_decrypt(encrypted_data, key):
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()
