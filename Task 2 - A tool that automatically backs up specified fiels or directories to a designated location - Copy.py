import shutil
import os

def backup_files(source_paths, destination):
    try:
        for source_path in source_paths:
            if os.path.exists(source_path):
                if os.path.isfile(source_path):
                    shutil.copy(source_path, destination)
                    print(f"File '{source_path}' backed up successfully to '{destination}'.")
                elif os.path.isdir(source_path):
                    shutil.copytree(source_path, os.path.join(destination, os.path.basename(source_path)))
                    print(f"Directory '{source_path}' backed up successfully to '{destination}'.")
            else:
                print(f"'{source_path}' does not exist.")
    except Exception as e:
        print(f"Error occurred during backup: {e}")

def get_user_input():
    source_paths = input("Enter the path(s) of the file(s) or directory(ies) to back up : ").split(",")
    destination = input("Enter the destination path to store the backup files: ")
    return source_paths, destination

def main():
    print("Welcome to the Backup Tool!")
    print("This tool allows you to back up specified files or directories to a designated location.\n")
    
    source_paths, destination = get_user_input()
    backup_files(source_paths, destination)

if __name__ == "__main__":
    main()
