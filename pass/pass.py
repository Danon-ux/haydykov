import random
def generate_password(length, use_digits=False, use_symbols=False, use_uppercase=False):
    # Создаём список допустимых символов
    allowed_chars = []
    if use_digits:
        allowed_chars += list("0123456789")
    if use_symbols:
        allowed_chars += list(string.punctuation)
    if use_uppercase:
        allowed_chars += list(string.ascii_uppercase)
    else:
        allowed_chars += list(string.ascii_lowercase)

    # Генерируем случайную последовательность
    password = ""
    for i in range(length):
        password += random.choice(allowed_chars)

    return password
  for i in range(5):
    print(generate_password(10))
  print(generate_password(8, use_digits=True, use_symbols=True))
