import random

print("Generando 5 números aleatorios:")

for i in range(5):
    numero = random.randint(1, 100)
    print("Número", i + 1, ":", numero)
