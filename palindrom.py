def cek_palindrom(teks):
    teks = teks.replace(" ", "").lower()
    return teks == teks[::-1]

kata = input("Masukkan kata atau kalimat: ")
if cek_palindrom(kata):
    print(f"'{kata}' adalah palindrom.")
else:
    print(f"'{kata}' bukan palindrom.")