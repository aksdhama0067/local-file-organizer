# Local File Organizer

A minimal, zero-dependency Python script designed to clean up cluttered folders (like your Desktop or Downloads directory) by automatically sorting files into dedicated subfolders based on their extensions.

## 🚀 Features
* **Automated Sorting:** Detects file types (`.pdf`, `.jpg`, `.zip`, etc.) and routes them to correct folders.
* **Smart Folder Creation:** Dynamically creates destination folders (e.g., Documents, Images) only if they are needed.
* **Safe Operations:** Skips directories entirely to prevent accidental nesting.

## 🛠️ How to Use
1. Clone or download `file_organizer.py`.
2. Update the `messy_folder` path at the bottom of the script to your target directory:
   ```python
   messy_folder = r"C:\Your\Messy\Folder\Path"