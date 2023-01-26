import numpy as np
import cv2
import os

def update_left(input_img_path,outut_img_path):

    image=cv2.imread(input_img_path)
    print(image.shape)
    cropped = image[0:1200,0:950] # 擷取座標為[y0:y1,x0:x1]
    cv2.imwrite(outut_img_path,cropped)

dataset_dir = 'cut'
output_dir = 'out_left'

#獲得需要轉化的圖片路徑並生成目標路徑(左半頁面)

image_filenames = [(os.path.join(dataset_dir,x),os.path.join(output_dir,x))
    for x in os.listdir(dataset_dir)]
for path in image_filenames:
    update_left(path[0],path[1])


def update_right(input_img_path,outut_img_path):

    image=cv2.imread(input_img_path)
    print(image.shape)
    cropped = image[0:1200,950:1900] # 擷取座標為[y0:y1,x0:x1]
    cv2.imwrite(outut_img_path,cropped)

dataset_dir = 'cut'
output_dir = 'out_right'

#獲得需要轉化的圖片路徑並生成目標路徑(左半頁面)

image_filenames = [(os.path.join(dataset_dir,x),os.path.join(output_dir,x))
    for x in os.listdir(dataset_dir)]
for path in image_filenames:
    update_right(path[0],path[1])