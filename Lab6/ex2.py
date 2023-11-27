#Ex 2
import os

def rename_files(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' doesn't exist.")

        files = os.listdir(directory_path)
        files.sort()

        count = 1

        for file_name in files:
            new_file_name = f"file{count}.txt"

            old_path = os.path.join(directory_path, file_name)
            new_path = os.path.join(directory_path, new_file_name)

            try:
                os.rename(old_path, new_path)
                print(f"Fisier redenumit cu succes: {file_name} -> {new_file_name}")
            except OSError as rename_error:
                print(f"Eroare la redenumirea fisierului {file_name}: {rename_error}")

            count += 1

    except FileNotFoundError as e:
        print(f"Eroare: {e}")
    except Exception as e:
        print(f"Eroare necunoscuta: {e}")
    finally:
        print(f"Redenumirea fisierelor a fost realizata cu succes.")

if __name__ == "__main__":
    directory_path = input("Introduceti calea directorului: ")
    rename_files(directory_path)

