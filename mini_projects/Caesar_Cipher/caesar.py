def encrypt(text, k, language):
    out = ""
    if language == "en":
        for c in text:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                out += chr((ord(c) - ord("A") + int(k)) % 26 + ord("A"))
            elif c in "abcdefghijklmnopqrstuvwxyz":
                out += chr((ord(c) - ord("a") + int(k)) % 26 + ord("a"))
            else:
                out += c
    else:
        for c in text:
            if c in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
                out += chr((ord(c) - ord("А") + int(k)) % 32 + ord("А"))
            elif c in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
                out += chr((ord(c) - ord("а") + int(k)) % 32 + ord("а"))
            else:
                out += c
    return out


def decrypt(text, k, language):
    out = ""
    if language == "en":
        for c in text:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                out += chr((ord(c) - ord("A") - int(k)) % 26 + ord("A"))
            elif c in "abcdefghijklmnopqrstuvwxyz":
                out += chr((ord(c) - ord("a") - int(k)) % 26 + ord("a"))
            else:
                out += c
    else:
        for c in text:
            if c in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
                out += chr((ord(c) - ord("А") - int(k)) % 32 + ord("А"))
            elif c in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
                out += chr((ord(c) - ord("а") - int(k)) % 32 + ord("а"))
            else:
                out += c
    return out

language = input("Введите язык текста (en/ru): ")
enc_or_dec = input("Введите 'e' для шифрования или 'd' для дешифрования: ")
k = input("Введите шаг сдвига: ")
text = input("Введите текст: ")


if enc_or_dec == "e":
    print(encrypt(text, k, language))
elif enc_or_dec == "d":
    print(decrypt(text, k, language))




