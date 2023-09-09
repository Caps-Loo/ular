# data yang dimasukan pasti bernilai string
data = input("masukan data = ")

print("Data = ", data , ", tipe =", type(data))

# casting data menjadi angka
angka1 = int(input("Masukan data = "))
print("Data = ", angka1 , ", tipe =", type(angka1))
angka = float(input("Masukan data = "))
print("Data = ", angka , ", tipe =", type(angka))

# boolean
data_boolean = bool(int(input("Masukan Nilai Boolean = ")))
print("Data = ", data_boolean , ", tipe =", type(data_boolean))