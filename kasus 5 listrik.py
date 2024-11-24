golongan = int(input("masukan golongan listrik [ 1 atau 2 ] = "))
pemakaian_KWH = int(input("masukan jumlah pemakaian listrik dalam KWH [ minimal 100 KWH ] = "))

if golongan == 1 :
    tarif_KWH = 1000
elif golongan == 2 :
    tarif_KWH = 2000
else : 
    print("golongan tidak valid")
    
if pemakaian_KWH < 100 : 
    biaya = 100 * tarif_KWH
elif pemakaian_KWH >= 1000:
    biaya = pemakaian_KWH * tarif_KWH * 1.10
else:
    biaya = pemakaian_KWH * tarif_KWH
    

print(f"Biaya listrik yang harus dibayar: Rp {biaya:,.2f}")
