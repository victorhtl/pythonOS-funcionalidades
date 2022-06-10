import os
import shutil

old_directory_path = 'C:\Ti_fora_doGIT\python-aprendizado\Módulos (libs)\Os\pasta2'
new_directory_path = 'C:\Ti_fora_doGIT\python-aprendizado\Módulos (libs)\Os\pasta'

try:
    os.mkdir(new_directory_path)
except FileExistsError:
    print('Arquivo já existe')

for root, dirs, files in os.walk(old_directory_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_directory_path, file)

        # Transferir files da pasta antiga para a pasta criada
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} transferido com sucesso')
