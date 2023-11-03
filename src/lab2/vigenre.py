def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()  # приводим ключевое слово к верхнему регистру
    keyword_length = len(keyword)  # вычисляем длину ключевого слова
    for i, char in enumerate(plaintext):  # перебираем символы в исходном тексте
        if char.isalpha():  # проверяем, является ли символ буквой
            shift = ord(keyword[i % keyword_length]) - ord('A')  # вычисляем сдвиг на основе символа ключа
            if char.isupper():  # если символ в исходном тексте в верхнем регистре
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))  # шифруем символ
            else:  # если символ в исходном тексте в нижнем регистре
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))  # шифруем символ
            ciphertext += encrypted_char  # добавляем зашифрованный символ к выходному тексту
        else:  # если символ не является буквой (например, пробел или знак пунктуации)
            ciphertext += char  # просто добавляем его к выходному тексту
    return ciphertext



def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()  # приводим ключевое слово к верхнему регистру
    keyword_length = len(keyword)  # вычисляем длину ключевого слова
    for i, char in enumerate(ciphertext):  # перебираем символы в зашифрованном тексте
        if char.isalpha():  # проверяем, является ли символ буквой
            shift = ord(keyword[i % keyword_length]) - ord('A')  # вычисляем сдвиг на основе символа ключа
            if char.isupper():  # если символ в зашифрованном тексте в верхнем регистре
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))  # дешифруем символ
            else:  # если символ в зашифрованном тексте в нижнем регистре
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))  # дешифруем символ
            plaintext += decrypted_char  # добавляем дешифрованный символ к исходному тексту
        else:  # если символ не является буквой (например, пробел или знак пунктуации)
            plaintext += char  # просто добавляем его к исходному тексту
    return plaintext