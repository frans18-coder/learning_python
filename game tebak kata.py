import random

kata = ["apel", "banana", "mangga"]
tebakan = 0
kata_rahasia = random.choice(kata)

while tebakan < 3:
    jawaban = input("Tebak kata buah: ")
    if jawaban == kata_rahasia:
        print("Benar!")
        break
    else:
        print("Salah!")
        tebakan += 1
else:
    print("Kata rahasia:", kata_rahasia)
