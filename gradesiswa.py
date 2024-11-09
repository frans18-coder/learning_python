nama_siswa = input("Masukkan nama siswa: ")
nilai = float(input("Masukkan nilai siswa (0-100): "))
if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B'
elif nilai >= 70:
    grade = 'C'
elif nilai >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f"Siswa: {nama_siswa}")
print(f"Nilai: {nilai}")
print(f"Grade: {grade}")

