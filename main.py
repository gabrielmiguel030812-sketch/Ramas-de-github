import random

numero = int(input("Adivina un número del 1 al 10: "))
numero2 = random.randint(1,10)

puntaje = 0

if numero == numero2:
    print("Has adivinado el numero")
    puntaje += 1
    print(f"Has adivinado el numero, tienes {puntaje} puntos")
else:
    print(f"No has adivinado el numero, el numero era {numero2}")                    