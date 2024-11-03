karakter = input("Masukkan sebuah karakter = ")

if karakter.isdigit():
    print("Karakter tersebut adalah angka.")
elif karakter.isalpha():
    print("Karakter tersebut adalah huruf.")
else:
    print("Karakter tersebut bukan huruf atau angka.")