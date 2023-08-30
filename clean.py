import os
import re

def clean_filename(filename):
    # Remove unwanted characters using regular expressions
    cleaned_filename = filename
    cleaned_filename = cleaned_filename.replace(',', '_')
    cleaned_filename = re.sub(r'ward\s+(\d)', r'ward\1', cleaned_filename)
    cleaned_filename = cleaned_filename.replace(' ', '_')
    return cleaned_filename.lower()

# Specify the root directory to start from
root_directory = './'

for dirpath, dirnames, filenames in os.walk(root_directory):
    for dirname in dirnames:
        new_dir_name = dirname[0] + '_' + dirname[1:] if dirname[0].isdigit() else dirname

        if dirname != new_dir_name:
            old_dir_path = os.path.join(dirpath, dirname)
            new_dir_path = os.path.join(dirpath, new_dir_name)
            os.rename(old_dir_path, new_dir_path)
            print(f'Renamed: {old_dir_path} -> {new_dir_path}')

# for dirpath, dirnames, filenames in os.walk(root_directory):
#     for dirname in dirnames:
#         old_dir_path = os.path.join(dirpath, dirname)
#         new_dir_name = dirname.replace(' ', '')  # Remove space
#         new_dir_path = os.path.join(dirpath, new_dir_name)

#         if dirname != new_dir_name:
#             os.rename(old_dir_path, new_dir_path)
#             print(f'Renamed: {old_dir_path} -> {new_dir_path}')

# # Walk through all directories and subdirectories
# for dirpath, dirnames, filenames in os.walk(root_directory):
#     for filename in filenames:
#         old_path = os.path.join(dirpath, filename)
#         cleaned_filename = clean_filename(filename)
#         new_path = os.path.join(dirpath, cleaned_filename)

#         if old_path != new_path:
#             os.rename(old_path, new_path)
#             print(f'Renamed: {old_path} -> {new_path}')
