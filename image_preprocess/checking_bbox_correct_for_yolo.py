import os
import cv2
import matplotlib.pyplot as plt
'''
yolo 포멧 형태의 라벨데이터(.txt)가 실제 이미지에서 bbox를 했을때 옳바른 좌표인지를 확인하기 위한 코드이다.
'''
img_rot = './sample_data' # 이미지 경로
label_rot = './generated_car_plate_text_label_data' # 이미지에 해당하는 라벨(yolo포멧의) txt파일 경로

file_cnt = 0

save_path = './bbox_valid_image' # subplot을 저장할 경로
os.makedirs(save_path, exist_ok=True)

for roots, dirs, files in os.walk(img_rot):
    for i in range(0, len(files), 9):  # 9개 이미지 단위로 처리합니다.
        fig, axs = plt.subplots(3, 3, figsize=(15, 15))  # 각 반복마다 새로운 fig 생성
        for j in range(i, min(i + 9, len(files))):  # 각 9개 이미지 또는 마지막에 남은 이미지들에 대해
            file = files[j]
            image_path = os.path.join(roots, file)
            label_path = image_path.replace(img_rot, label_rot)
            image = cv2.imread(image_path, 1)

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image_height, image_width = image.shape[:2]
            with open(label_path + '.txt') as f:
                readlines = f.readlines()
                for readline in readlines:
                    line = readline.strip()
                    line = line.split(' ')[1:]  # ['0.8692682926829268', '0.5865885416666667', '0.08780487804878048', '0.06901041666666667']
                    float_line = list(map(float, line))

                    x1 = int((float_line[0] - float_line[2] / 2) * image_width)
                    y1 = int((float_line[1] - float_line[3] / 2) * image_height)
                    x2 = int((float_line[0] + float_line[2] / 2) * image_width)
                    y2 = int((float_line[1] + float_line[3] / 2) * image_height)

                    cv2.rectangle(image_rgb, (x1, y1), (x2, y2), (255, 0, 0), 2)

            ax = axs[(j - i) // 3, (j - i) % 3]
            ax.imshow(image_rgb)
            ax.axis('off')

        plt.savefig(f'{save_path}/output_{file_cnt}.png')
        plt.close(fig)
        file_cnt += 1
               
