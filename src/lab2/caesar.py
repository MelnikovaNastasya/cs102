def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():

            shift_amount = shift % 26
            """
            Проверяем, является ли символ буквой и гарантируем, что сдвиг находится в пределах алфавита
            """
            if char.isupper():  # для заглавных букв
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            else:  # для строчных букв
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
        else:
            shifted_char = char  # не изменяем не-буквенные символы
        ciphertext += shifted_char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            """
            Проверяем, является ли символ буквой и гарантируем, что сдвиг находится в пределах алфавита
            """
            if char.isupper():  # для заглавных букв
                shifted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            else:  # для строчных букв
                shifted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
        else:
            shifted_char = char
            """
            Если символы не являются буквами - не изменяем их
            """
        plaintext += shifted_char
    return plaintext