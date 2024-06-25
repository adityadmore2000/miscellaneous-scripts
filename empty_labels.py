import os
import shutil
def find_empty_txt_and_corresponding_image(directory):
    dest_dir = os.path.join(directory_path, '..', f"moved_{os.path.basename(directory)}")
    if not os.path.exists(dest_dir):
        print(f"Directory {dest_dir} created successfully...")
        os.makedirs(dest_dir)
    else:
        print(f"directory: {dest_dir} already exists!!!")
    # Traverse through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a text file and empty
        if filename.endswith(".txt") and os.path.getsize(os.path.join(directory, filename)) == 0 and filename!='classes.txt':
            # Find the corresponding image file
            base_name = os.path.splitext(filename)[0]
            possible_image_filenames = [f for f in os.listdir(directory) if f.startswith(base_name) and f != filename]

            # Check if any corresponding image files exist
            for image_filename in possible_image_filenames:
                shutil.move(os.path.join(directory,filename),dest_dir)
                shutil.move(os.path.join(directory,image_filename),dest_dir)

# Replace 'your_directory_path' with the path of the directory you want to search
directory_path = input("Enter source directory path: ")

find_empty_txt_and_corresponding_image(directory_path)
