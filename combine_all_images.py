import os
import shutil
import sys

def move_images(img_path,dest_img_path):
    for file in os.listdir(img_path):
        shutil.move(os.path.join(img_path,file),os.path.join(dest_img_path,file))

def move_labels(labels_path,dest_label_path):
    for file in os.listdir(labels_path):
        shutil.move(os.path.join(labels_path,file),os.path.join(dest_label_path,file))

img_path = sys.argv[1]
dest_img_path = sys.argv[2]
labels_path = sys.argv[3]
dest_label_path = sys.argv[4]