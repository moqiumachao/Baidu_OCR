from accurate import BaiduImg
from ContextProcess import ContextProcess
import os

#遍历文件夹获取所有文件
def get_files_name(images_dir = "images",files_dir = "result"):
    images_path = []
    files_path = []
    for filename in os.listdir(images_dir):
        if filename.endswith(('.png','.jpg','.bmp','.jpeg')):
            images_path.append(os.path.join(images_dir, filename))
            if filename.endswith("jpeg"):
                files_path.append(os.path.join(files_dir, filename[:-4] + "txt"))
            else:
                files_path.append(os.path.join(files_dir, filename[:-3] + "txt"))




    return images_path,files_path



images_path,files_path = get_files_name()

for i,item in enumerate(images_path):
    image_path = images_path[i]
    file_path = files_path[i]
    baidu = BaiduImg(image_path)
    res = baidu.img_ocr()
    process = ContextProcess(res)
    process.basic_save_txt(file_path)