import zipfile

def backup_directory(directory_path):
    if not os.path.exists(directory_path):
        print("Error: Directory does not exist.")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    backup_filename = f"backup_{timestamp}.zip"
    
    try:
    with zipfile.ZipFile(backup_filename, "w") as zipf
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    zipf.write(file_path, os.path.relpath(file_path, directory_path))
                    
                    # Add the file to the ZIP archive with its relative path
                    zipf.write(file_path, os.path.relpath(file_path, directory_path))
        
        print(f"Backup created: {backup_filename}")
    
    except:
        print(f"Error creating backup: {str(e)}")

# Prompt the user to enter the directory path for backup
directory_path = input("Enter the directory path to back up: ")
backup_directory(directory_path)
