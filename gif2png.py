from PIL import Image
import os


def convert_image_type(src_dir,dest_dir,type1,type2):
    length = len(type1)
    for filename in os.listdir(src_dir):
        if filename.endswith(type1):
            path = os.path.join(src_dir,filename)
            img = Image.open(path)
            img.save(os.path.join(dest_dir,filename[:-length]+type2))



#convert_image_type("images","temp",".gif",".png")