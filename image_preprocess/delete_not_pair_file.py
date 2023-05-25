import glob
import os

'''
 Json과 Image가 Pair가 이루어 지지 않는 친구들은 삭제한다.
 Json파일이 이미지 파일 보다 더 많은 경우에 해당한다.
 Json을 전부 읽어들이고 해당 파일의 확장자를 .jpg로 replace한다.
 해당 이미지가 디렉토리에 없으면 json파일을 삭제한다.
'''

# 작업할 디렉토리를 설정한다.
directory = '/home/rtx4090/workspace/vms/yolov5/datasets/fire_dataset/fire_data/Training/fire_image/'

# 파일의 갯수가 더 많은 파일을 선택해야 한다. json이 더 많음으로 확장자를 json으로 한다.
json_files = glob.glob(directory+'*.jpg')

counter = 0

for i, json_file in enumerate(json_files) :
    #json파일을 기준으로 이미지 파일로 확장자만 변경한다.
    image_file = json_file.replace(".jpg", ".txt")

    # 만약 json파일과 상응하는 이미지 파일이 있다면
    if os.path.isfile(image_file) :
        # 있다고 출력하고
        print(f"({i+1}/{len(json_files)}) {image_file} Exist")
    # 그렇지 않다면
    else :
        print(f"({i+1}/{len(json_files)}) {image_file} Removed")
        # json파일에 상응하는 이미지 파일이 없다는 것으로 판단하고 해당 json파일을 삭제한다.
        os.remove(json_file)
        counter += 1