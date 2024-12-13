def hitung_bmi(berat, tinggi):
    return berat / (tinggi ** 2)

berat = float(input("Masukkan berat (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))

bmi = hitung_bmi(berat, tinggi)

if bmi < 18.5:
    print("Kurus")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Gemuk")
else:
    print("Sangat gemuk")
