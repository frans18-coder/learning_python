nilai = int(input("masukan nilai = "))

if nilai >= 90 and nilai <= 100:
    print("Predikat nya A")
elif nilai >= 80 and nilai < 90:
    print("Predikat nya B")
elif nilai >= 70 and nilai < 80:
    print("Predikat nya C")
elif nilai >= 60 and nilai < 70:
    print("Predikat nya D")
elif nilai >= 0 and nilai < 60:
    print("Predikat nya E ")
else:
    print("nilai tidak valid!")