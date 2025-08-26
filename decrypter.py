import os
import pyaes

# busca o diretório alvo
target_dir = "arquivos-sensíveis"

# define a chave para descriptografia
key = b"testeransomwares"

# percorre os diretórios recursivamente
for root, dirs, files in os.walk(target_dir):
    for file_name in files:
        if not file_name.endswith(".ransomwaretroll"):
            continue

        file_path = os.path.join(root, file_name)

        # abre o arquivo criptografado
        with open(file_path, "rb") as f:
            file_data = f.read()

        # remove o arquivo criptografado
        os.remove(file_path)

        # descriptografa
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # recria o arquivo original sem a extensão do ransomware
        new_file = file_path.replace(".ransomwaretroll", "")
        with open(new_file, "wb") as f:
            f.write(decrypt_data)

print("Arquivos descriptografados com sucesso!")
