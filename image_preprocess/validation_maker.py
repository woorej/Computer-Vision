import os
import math
import random
import shutil
'''
train과 label폴더가 분리되어 있다고 가정한다.
train의 데이터 갯수중 valid_ratio만큼을 validation으로 사용한다.
이때 라벨도 같이 이동한다.

'''
src_img_dir = './sample_train_image'
src_label_dir = './sample_train_label'

dst_img_dir = './sample_valid_image'
dst_label_dir = './sample_valid_label'

os.makedirs(dst_img_dir, exist_ok=True)
os.makedirs(dst_label_dir, exist_ok=True)

valid_ratio = 0.2

image_files = [file for file in os.listdir(src_img_dir) if os.path.isfile(os.path.join(src_img_dir, file))]

num_files_to_move = math.ceil(len(image_files)*valid_ratio)
image_files_to_move = random.sample(image_files, num_files_to_move)

for file in image_files_to_move :
    label_files_to_move = file.replace('.jpg','.txt')

    shutil.move(os.path.join(src_img_dir, file), dst_img_dir) # move images
    shutil.move(os.path.join(src_label_dir, label_files_to_move), dst_label_dir) # move label
    print(f"{os.path.join(src_img_dir, file)} ---> {dst_img_dir}")
    print(f"{os.path.join(src_label_dir, label_files_to_move)} ---> {dst_label_dir}")