import random

angka_rahasia = random.randint(1, 100)
tebakan = 0

while tebakan < 6:
    jawaban = int(input("Tebak angka antara 1-100: "))
    if jawaban < angka_rahasia:
        print("Terlalu rendah!")
    elif jawaban > angka_rahasia:
        print("Terlalu tinggi!")
    else:
        print("Benar!")
        break
    tebakan += 1
else:
    print(f"Angka rahasia: {angka_rahasia}")



