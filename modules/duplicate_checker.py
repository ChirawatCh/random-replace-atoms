import os
import hashlib
import shutil
import sys

def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_files(folder):
    file_hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            
            if file_hash in file_hashes:
                duplicates.append((file_path, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = file_path
    
    return duplicates

def remove_duplicate_files(duplicate_pairs):
    for pair in duplicate_pairs:
        print(f"Removing duplicate file: {pair[0]}")
        os.remove(pair[0])

if __name__ == "__main__":
    folder_to_check = sys.argv[1]
    # folder_to_check = "Ag5Au20"  # Replace with the folder containing your files
    duplicate_pairs = find_duplicate_files(folder_to_check)
    
    if duplicate_pairs:
        print("Duplicate files found:")
        for pair in duplicate_pairs:
            print(f"{pair[0]} is a duplicate of {pair[1]}")
        
        remove_duplicate_files(duplicate_pairs)
    else:
        print("No duplicate files found.")
