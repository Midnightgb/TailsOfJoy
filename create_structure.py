import os


def create_project_structure():
    # Definir la estructura de carpetas
    folders = ['/app', '/app/static', '/app/templates', '/scripts', '/tests', '/app/api','/app/api/endpoints']

    # Crear las carpetas
    for folder in folders:
        print(f'Creando la carpeta {folder}...')
        folder_path = os.path.join(script_path, folder[1:])
        try:
            os.makedirs(folder_path)
            print(f'Creando la carpeta {folder_path}...\n')
        except FileExistsError:
            print(f'La carpeta {folder_path} ya existe.\n')

    # Crear archivos vacíos
    empty_files = [
        'app/main.py',
        'app/static/styles.css',
        'app/static/app.js',
        'app/templates/index.html'
    ]

    for file in empty_files:
        file_path = os.path.join(script_path, file)
        try:
            open(file_path, 'w').close()
            print(f'Creado el archivo {file_path}...')
        except FileNotFoundError:
            print(
                f'No se pudo crear el archivo {file_path}. Ruta no encontrada.')
        except PermissionError:
            print(
                f'No se pudo crear el archivo {file_path}. Permiso denegado.')

    print("Estructura creada exitosamente.")


if __name__ == "__main__":
    # Obtener la ruta del script
    script_path = os.path.dirname(os.path.realpath(__file__))
    create_project_structure()
