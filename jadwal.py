print("Jadwal Matakuliah Kelas B TI Pagi 2021")
print("Senin, Selasa , Rabu, Kamis, Jumat, Sabtu, Minggu")
pilih = input("Pilih Jadwan Pada Hari: ").lower()
if pilih == "senin":
    matakuliah_satu = "PEMROGRAMAN WEB 10.30 - 13.00"
    matakuliah_dua = "PRAKTIKUM BASIS DATA 08.00 - 09.40"
    matakuliah_tiga = " "
    notif = "Hari Yang Cukup Berat...!!! "
elif pilih == "selasa":
    matakuliah_satu = "STRUKTUR DATA 10.30 - 13.00"
    matakuliah_dua = " "
    matakuliah_tiga = " "
    notif = "Jaga Fokus Bro...!!! "
elif pilih == "rabu":
    matakuliah_satu = "STATISTIKA 13.00 - 15.30"
    matakuliah_dua = " "
    matakuliah_tiga = " "
    notif = "Perhatiin Dosen-nya Bro...!!! "
elif pilih == "kamis":
    matakuliah_satu = "PEMROGRAMAN CLIENT SERVER 08.00 - 09.40"
    matakuliah_dua = "MULTIMEDIA INTERAKTIF 10.30 - 12.10 "
    matakuliah_tiga = "BASIS DATA 13.00 - 15.30"
    notif = "Hari Yang Sangat Berat...!!!"
elif pilih =="jumat":
    matakuliah_satu = "METODOLOGI PENELITIAN 13.00 - 14.40"
    matakuliah_dua = " "
    matakuliah_tiga = " "
    notif = "Masuk Gak Masuk Yang Penting Hadir...!!! "
else:
    notif = "Hari ini Libur Bro...!!!"
    matakuliah_satu = " "
    matakuliah_dua = " "
    matakuliah_tiga = " "
print(f"{matakuliah_satu}")
print(f"{matakuliah_dua}")
print(f"{matakuliah_tiga}")
print(f"{notif}")