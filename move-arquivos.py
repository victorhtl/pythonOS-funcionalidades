import os
import shutil


def move_arquivo(old_directory_path, new_directory_path):
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


move_arquivo('caminho_antigo', 'caminho_novo')
