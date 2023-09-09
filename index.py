# merubah satu tipe ke tipe yang lain
# tipe data = int, string, float, boolean

# integer 
print("===integer====")
data_int = 9;

data_float = float(data_int) # akan dibulatkan ke bawah
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data = " , data_float , ",tipe = ", type(data_float))
print("data = " , data_str , ",tipe = ", type(data_str))
print("data = " , data_bool , ",tipe = ", type(data_bool))

print("===float===")
# float 
data_float = 2.5;

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai int = 0
print("data = " , data_int , ",tipe = ", type(data_int))
print("data = " , data_str , ",tipe = ", type(data_str))
print("data = " , data_bool , ",tipe = ", type(data_bool))

print("===boolean===")
# boolean 
data_bool = False       

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai int = 0
print("data = " , data_int , ",tipe = ", type(data_int))
print("data = " , data_str , ",tipe = ", type(data_str))
print("data = " , data_float , ",tipe = ", type(data_float))

print("===string===")
# string 
data_string = "10"       
# string tidak bisa diubah mnjadi integer
# string kosong akan menjadi boolean false 
data_int = int(data_string)
data_bool = bool(data_string)
data_float = float(data_string) # akan false jika nilai int = 0
print("data = " , data_int , ",tipe = ", type(data_int))
print("data = " , data_bool , ",tipe = ", type(data_bool))
print("data = " , data_float , ",tipe = ", type(data_float))


