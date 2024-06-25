import os

path = input("Enter path to root dir: ")


def get_filenames(folder):
    return set([file for file in os.listdir(folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))])


train_files = get_filenames(os.path.join(path, 'train'))
test_files = get_filenames(os.path.join(path, 'test'))
val_files = get_filenames(os.path.join(path, 'val'))

train_test_common = train_files.intersection(test_files)
test_val_common = test_files.intersection(val_files)
train_val_common = train_files.intersection(val_files)

if train_test_common:
    print("train-test-common", train_test_common)
if test_val_common:
    print("test_val_common", test_val_common)
if train_val_common:
    print("train_val_common", train_val_common)
