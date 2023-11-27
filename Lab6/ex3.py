import sys
import os

def calculate_total_size(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directorul '{directory_path}' nu exista.")

        total_size = 0

        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except Exception as file_error:
                    print(f"Nu s-a putut obține dimensiunea pentru fișierul '{file_path}': {file_error}")

        print(f"Dimensiunea totală a tuturor fișierelor din directorul '{directory_path}' este: {total_size} bytes.")

    except FileNotFoundError as e:
        print(f"Eroare: {e}")
    except PermissionError as e:
        print(f"Eroare de permisiune: {e}")
    except Exception as e:
        print(f"Eroare necunoscuta: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Mod de utilizare: python ex3.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    calculate_total_size(directory_path)
