import json
import os
import shutil

# separate out an image and json file into another folder only when there is instance of given class 
root_path = input("Enter path: ")

dest_dir = os.path.join(os.path.dirname(root_path),f'staircase_{os.path.basename(root_path)}')

os.makedirs(dest_dir,exist_ok=True)



for split in os.listdir(root_path):
    files_to_move = set()

    split_dir = os.path.join(root_path, split)

    for file in os.listdir(split_dir):

        if file.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')):
            image_file = os.path.join(split_dir, file)
            label_file = os.path.join(split_dir, f"{file.split('.')[0]}.json")

            with open(label_file) as f:
                data = json.load(f)

            for i, shape in enumerate(data['shapes']):
                if shape['label'] == 'staircase':
                    files_to_move.add(label_file)
                    files_to_move.add(image_file)

    dest_split = os.path.join(dest_dir, split)
    os.makedirs(dest_split, exist_ok=True)

    for file in files_to_move:
        shutil.copy(file, dest_split)


for split in os.listdir(dest_dir):
    dest_split = os.path.join(dest_dir,split)

    for file in os.listdir(dest_split):

        if file.endswith(('.jpg','.jpeg','.png','.JPG','.JPEG','.PNG')):
            image_file = os.path.join(dest_split, file)
            label_file = os.path.join(dest_split,f"{file.split('.')[0]}.json")

            with open(label_file) as f:
                data = json.load(f)
            for i,shape in enumerate(data['shapes']):
                if shape['label']!='staircase':
                    data['shapes'].pop(i)
            output_json = os.path.join(dest_split,f"{file.split('.')[0]}_staircase.json")
            with open(output_json,'w') as f:
                json.dump(data,f)

            os.remove(label_file)
            os.rename(output_json,label_file)