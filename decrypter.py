import os
import pyaes

file_name = "teste.txt.ransomware"
file = open(file_name, "rb")
file_data = file.read()
file.close()


key = b"maistestedioransom"
aes = pyaes.AESModeOfOperationsCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = "teste.txt"
new_file = open(f'{new_file}','wb')
new_filme.write(decrypt_data)
new_file.close()
