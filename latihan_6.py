jenis = input("Pilih jenis kaos P = Pria, W = Wanita : ").lower()
kaos = input("Pilih ukuran kaos S, M, L, XL, XXL : ").lower()
warna = input("Pilih warna kaos P = putih, H = hitam, A = Abu-abu : ").lower()
jumlah = int(input("Berapa jumlah kaos yang dibeli: "))
if jenis == "p":
 gender = "Pria"
if kaos == "s":
    harga = 50000
elif kaos == "m":
      harga = 60000
elif kaos == "l":
      harga =70000
elif kaos == "xl":
      harga = 80000
elif kaos == "xxl":
      harga = 90000
if warna == "p":
    kode = "putih"
    biaya = 0
elif warna == "h":
    kode = "hitam"
    biaya = 5000
elif warna == "a":
    kode = "abu-abu"
    biaya = 5000
if jenis == "w":
 gender = "wanita"
if kaos == "s":
    harga = 55000
elif kaos == "m":
      harga = 70000
elif kaos == "l":
      harga =85000
elif kaos == "xl":
      harga = 100000
elif kaos == "xxl":
      harga = 115000
if warna == "p":
    kode = "putih"
    biaya = 0
elif warna == "h":
    kode = "hitam"
    biaya = 5000
elif warna == "a":
    kode = "abu-abu"
    biaya = 5000
else:
    kode = "pilihan tidak tersedia"
total = (harga + biaya) * jumlah
print (f"Anda membeli kaos {gender}")
print (f"Ukuran {kaos}")
print (f"Warna {kode} +{biaya}")  
print (f"Harga Rp.{harga}") 
print (f"Jumlah {jumlah}")
print (f"total bayar RP.{total}")