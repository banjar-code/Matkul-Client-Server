from data import *
import random
print(f"Daftar Nilai Mahasiswa: \n{data_mhs}")
print(f" Elemen List Pertama: \n{data_mhs [0]}")
print(f" Elemen List Terakhir: \n{data_mhs [5]}")
# mencari panjang list
jumlah_element = len(data_mhs)
print(f"Jumlah element list: {jumlah_element}")
# menambahkan element
data_mhs.append(66)
data_mhs.insert(2,77)
# menghapus element di posisi paling belakang
data_mhs.pop()
print(data_mhs)
# menghapus element
data_mhs.remove(77)
print(data_mhs)
# print data dictionary
print(data_kry)
#print nama karyawan
print(f"Nama Karyawan: {data_kry['nama']}")
# menambah data dictionary
data_kry['no_hp'] = "082126546564"
print(data_kry)
#Mengubah item pada dictionary
data_kry["golongan"] = 'IIIb'
print(data_kry)
#menghapus item
data_kry.pop('no_hp')
#menghapus item paling akhir
data_kry.popitem()
print(data_kry)
#contoh mendapatkan nilai acak
print(random.randint(0,101))
#mengambil nilai acak dari data list
nilai = random.choice(data_mhs)
print(f"Nilai acak: {nilai}")
x = "Kota Tasikmalaya Provinsi Jawa Barat"
print(random.choice(x))