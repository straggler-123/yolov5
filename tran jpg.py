import os
import cv2 as cv

image_path = 'C:/Users/19815/Desktop/project/yolov5/dataset/score/train/images/test'  # 设置图片读取路径
save_path = 'C:/Users/19815/Desktop/JPEGImages/test'  # 设置图片保存路径

if not os.path.exists(save_path):  # 判断路径是否正确，并打开
    os.makedirs(save_path)

image_file = os.listdir(image_path)

for image in image_file:
    if image.split('.')[-1] in ['bmp', 'jpg', 'jpeg', 'png', 'JPG', 'PNG']:
        str = image.rsplit(".", 1)  # 从右侧判断是否有符号“.”，并对image的名称做一次分割。如112345.jpeg分割后的str为["112345","jpeg"]
        output_img_name = str[0] + ".jpg"  # 取列表中的第一个字符串与“.jpg”放在一起。
        src = cv.imread(os.path.join(image_path, image))
        newimg = cv.imwrite(save_path + '/' + output_img_name, src)
print('FINISHED')