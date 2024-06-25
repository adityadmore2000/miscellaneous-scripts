import os
# import numpy as np

"""

"""
def change_first_char_in_same_file(root_dir,labels):
    # args = np.array(args).flatten()
    for file in os.listdir(root_dir):
        if file != 'classes.txt' and file.split('.')[1] == 'txt':
            file_path = os.path.join(root_dir,file)

            with open(file_path, 'r+') as file:
                lines = file.readlines()
                file.seek(0)  # Reset the file pointer to the beginning

                for line in lines:
                    if line.strip():  # Check if the line is not empty
                        for i in range(0,len(labels),2):
                            class_index = int(line.split()[0])
                            if class_index==labels[i]:
                                modified_line = str(labels[i+1])
                                modified_line += line[len(modified_line):]
                                print(f"modified line from {line} to : {modified_line}")
                        # elif int(line[0])==1:
                        #     modified_line = str(14) + line[1:]
                        #     print(f"modified line from {line} to : {modified_line}")
                                file.write(modified_line)
                    else:
                        print(f"didn't modified line: {line}")
                        file.write(line)  # Preserve empty lines

                file.truncate()

# change_first_char_in_same_file(os.path.normpath(input("Enter folder where you want to change label value... ")),0,11,1,14)
# root_dir = r"D:\Datasets\data_for_pump_stand\train"
# for file in os.listdir(root_dir):
#     if file!='classes.txt' and file.split('.')[1]=='txt':
#         change_first_char_in_same_file(os.path.join(root_dir,file))