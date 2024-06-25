import os
import shutil

root_path = input("Enter path: ")

dest_dir = os.path.join(os.path.dirname(root_path),f'toilet_bowl_{os.path.basename(root_path)}')

os.makedirs(dest_dir,exist_ok=True)



for split in os.listdir(root_path):
    files_to_move = set()

    split_dir = os.path.join(root_path, split)

    for file in os.listdir(split_dir):

        if file.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')):
            image_file = os.path.join(split_dir, file)
            label_file = os.path.join(split_dir, f"{file.split('.')[0]}.txt")

            with open(label_file) as f:
                for line in f:
                    # specify class id of the class to be included
                    if int(line.strip().split(' ')[0]) == 1:
                        files_to_move.add(label_file)
                        files_to_move.add(image_file)

    dest_split = os.path.join(dest_dir, split)
    os.makedirs(dest_split, exist_ok=True)

    for file in files_to_move:
        shutil.copy(file, dest_split)

