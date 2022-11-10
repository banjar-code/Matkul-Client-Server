nilai_angka = int(input("Masukan nilai (0-10) "))
if nilai_angka > 80:
    nilai_huruf = "A"
elif nilai_angka > 65:
    nilai_huruf = "B"
elif nilai_angka > 50:
    nilai_huruf = "C"
else:
     nilai_huruf = "D"
print(f"Nilai angka {nilai_angka} maka nilai huruf {nilai_huruf}")
