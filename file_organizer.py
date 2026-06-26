import os
import shutil

def organize_folder(target_folder):

    #types of files it can work with

    file_rules = {
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.jpg': 'Images',
        '.png': 'Images',
        '.mp3': 'Audio',
        '.zip': 'Archives'
    }

   #1. list of every thing in folder
    all_files = os.listdir(target_folder)

    # 2. loop to check
    for file_name in all_files:
        file_path = os.path.join(target_folder, file_name)

        if os.path.isdir(file_path):
            continue



        name, extension = os.path.splitext(file_name)
        extension = extension.lower()

        
        if extension in file_rules:
            folder_name = file_rules[extension]
            destination_folder = os.path.join(target_folder, folder_name)


            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)


            shutil.move(file_path, os.path.join(destination_folder, file_name))
            print(f"Moved: {file_name} -> {folder_name}/")

# ~~~ HOW TO RUN IT ~~~
# Example: "C:/Users/YourName/Desktop/bankai_test"
#change the location to your file
messy_folder = r"C:\Users\HP\OneDrive\Desktop\bankai_test"
organize_folder(messy_folder)
