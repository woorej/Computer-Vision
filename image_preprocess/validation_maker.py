import os
import math
import random
import shutil

src_dir = './sample_data'
dst_dir = './sample_valid'
os.makedirs(dst_dir, exist_ok=True)
valid_ratio = 0.2

files = [file for file in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, file))]

num_files_to_move = math.ceil(len(files)*valid_ratio)
files_to_move = random.sample(files, num_files_to_move)

for file in files_to_move :
    shutil.move(os.path.join(src_dir, file), dst_dir)
