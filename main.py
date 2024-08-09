import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    password_length = int(input("Introduce la longitud de la contraseña: "))
    generated_password = ""

    for i in range(password_length):
        generated_password += random.choice(characters)

    print("La contraseña generada es:", generated_password)
