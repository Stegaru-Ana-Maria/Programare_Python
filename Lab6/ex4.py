#Ex 4
import os
import sys

def count_file_by_extension(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directorul {directory_path} nu exista.")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"{directory_path}' nu este un director.")

        if not os.access(directory_path, os.R_OK):
            raise PermissionError(f"Nu avem permisiuni de citire pentru directorul '{directory_path}'.")

        files = []
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                files.append(file_name)

        if not files:
            print(f"Directorul '{directory_path}' este gol.")
            return

        extension_counts = {}

        for file in files:
            _, extension = os.path.splitext(file)
            extension = extension.lower()
            extension_counts[extension] = extension_counts.get(extension, 0) + 1

        print("Numărul de fișiere pentru fiecare extensie:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} fișiere")

    except FileNotFoundError as e:
        print(f"Eroare: {e}")
    except NotADirectoryError as e:
        print(f"Eroare: {e}")
    except PermissionError as e:
        print(f"Eroare de permisiune la accesarea directorului '{directory_path}'. Verifică permisiunile.")
    except Exception as e:
        print(f"Eroare necunoscută: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Mod de utilizare: python ex4.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    count_file_by_extension(directory_path)
