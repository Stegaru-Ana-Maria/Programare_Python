# EX 1
import sys
import os

def read_and_print_files(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directorul {directory_path} nu exista.")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"{directory_path} nu este un director.")

        if not file_extension.startswith("."):
            raise ValueError(f"Extensie de fișier invalidă. Ar trebui să înceapă cu un punct.")

        files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]

        if not files:
            raise FileNotFoundError(f"Nu s-au gasit fisiere cu extensia {file_extension} in directorul {directory_path}.")

        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                    print(f"Continutul fisierului '{file_name}':\n{file_contents}")
            except Exception as file_error:
                print(f"Eroare la citirea fisierului '{file_name}': {file_error}.")
    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Eroare: {e}")
    except Exception as e:
        print(f"Eroare necunoscuta: {e}")
    finally:
        print("Citirea fisierelor a fost realizata cu succes.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Mod de utilizare: python ex1.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)

