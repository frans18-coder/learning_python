import random

angka_rahasia = random.randint(1, 100)
tebakan = 0

while tebakan < 6:
    jawaban = int(input("Tebak angka antara 1-100: "))
    if jawaban < angka_rahasia:
        print("Terlalu rendah! Sisa tebakan:", 6-tebakan)
    elif jawaban > angka_rahasia:
        print("Terlalu tinggi! Sisa tebakan:", 6-tebakan)
    else:
        print("Benar!")
        break
    tebakan += 1
else:
    print("Angka rahasia:", angka_rahasia)
