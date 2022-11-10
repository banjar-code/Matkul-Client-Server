tiket = input("Pilih Jenis tiket V = velvet G = Gold D = 4DX atau R = reguler? ").lower()
jumlah = int(input("Berapa jumlah tiket yang dibeli? "))
if tiket == "v":
    harga = 150000
    jenis = "Velvet"
elif tiket == "g":
    harga = 100000
    jenis = "Gold"
elif tiket == "d":
    harga = 75000
    jenis = "4DX"
elif tiket == "r":
    harga = 50000
    jenis = "Reguler"
else:
    harga = 0
    jenis = "Yang tidak tersedia"
total = harga * jumlah
print (f"Anda membeli tiket {jenis} dengan harga Rp.{harga} jumlah tiket = {jumlah}, total bayar RP.{total}")