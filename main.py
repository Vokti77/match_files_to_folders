import os
import shutil

def match_files(source_folder, target_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of files in the source folder
    source_files = os.listdir(source_folder)

    # Iterate over the source files
    for file_name in source_files:
        source_file_path = os.path.join(source_folder, file_name)
        target_file_path = os.path.join(target_folder, file_name)

        # Check if the file exists in the target folder
        if os.path.isfile(target_file_path):
            # Copy the file to the output folder
            output_file_path = os.path.join(output_folder, file_name)
            shutil.copy2(source_file_path, output_file_path)
            print(f"Match found: {file_name}")

# Specify the source folder, target folder, and output folder
source_folder = "folder_name"
target_folder = "folder_name"
output_folder = "folder_name"

# Call the match_files function
match_files(source_folder, target_folder, output_folder)
