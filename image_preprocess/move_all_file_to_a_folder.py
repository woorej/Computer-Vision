import os
import glob
import shutil

# 여러 경로에 있는 폴더내의 파일들을 하나의 파일로 이동
# 화재 데이터가 모여있는 경로를 입력해준다. (이동할 대상 경로 1)
fire_data_dir = "/home/rtx4090/workspace/vms/yolov5/datasets/fire_dataset/fire_data/Training/fire_label/*.json"
# 자동차 번호판 데이터가 모여있는 경로를 입력해준다. (이동할 대상 경로 2)
# car_data_dir = "/home/jj/workspace/vms/Test2/*"

# 최종적으로 옮겨질 디렉토리를 입력해준다. (옮겨질 파일 경로)
parsed_dir = "/home/rtx4090/workspace/vms/yolov5/datasets/fire_dataset/fire_data/Training/fire_image/"

# 전체 화재데이터의 파일들의 리스트를 만든다.
fire_files = glob.glob(fire_data_dir)

for i, fire_file in enumerate(fire_files) :
    # 화재 데이터의 경로가 설정된 문자열 중에서 파일의 이름만 가져온다
    file_name = fire_file.split("/")[-1]
    # 해당 파일의 이름과 parsed 디렉토리를 합쳐서 총 이동할 경로의 문자열을 만든다.
    parsed_file = parsed_dir+file_name

    print(f"({i}/{len(fire_files)}) {fire_file} >> {parsed_file}")
    # 화재 데이터를 parsed_file의 디렉토리로 이동시킨다.
    shutil.move(fire_file, parsed_file)
