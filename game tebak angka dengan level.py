import random

level = int(input("Pilih level (1-3): "))
angka_rahasia = random.randint(1, 100)

if level == 1:
    kesempatan = 5
elif level == 2:
    kesempatan = 3
elif level == 3:
    kesempatan = 1
else:
    print("Level tidak valid")

tebakan = 0
while tebakan < kesempatan:
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
    print("Angka rahasia:", angka_rahasia)
