import os
import sys
from PIL import Image

path = sys.argv[1]
file_list = os.listdir(path)
file_list_png = sorted([file for file in file_list if file.endswith(".png")])


load_images = [Image.open(path + f) for f in file_list_png]
converted_images = [f.convert('RGB') for f in load_images]
image_list = converted_images[1:]
converted_images[0].save(path + '/hi.pdf', save_all=True, append_images=image_list)

# imagelist = [im2,im3,im4]

# im1.save(r'C:\Users\Ron\Desktop\Test\myImages.pdf',save_all=True, append_images=imagelist)