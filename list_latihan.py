from latihan_data import *
print(f"Daftar Nama Buah: \n{data_buah}")
# menambahkan element
data_buah.append("durian")
data_buah.insert(1,"manggis")
print(f"Daftar Nama Buah: \n{data_buah}")
# menghapus element di posisi paling belakang
data_buah.pop()
print(data_buah)
# menghapus element
data_buah.remove("manggis")
print(data_buah)

# print data dictionary
print(data_mobil)
# menambah data dictionary
data_mobil['fuel'] = "gasoline"
data_mobil['color'] = "black"
print(data_mobil)
#Mengubah item pada dictionary
data_mobil["tipe"] = 'Fortuner TRD Sportivo'
print(data_mobil)