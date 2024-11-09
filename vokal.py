huruf = input("Masukkan huruf: ").upper()
if huruf in 'AEIOU':
    print(f"{huruf} adalah huruf vokal.")
elif huruf.isalpha():
    print(f"{huruf} adalah huruf konsonan.")
else:
    print("Input bukan huruf.")