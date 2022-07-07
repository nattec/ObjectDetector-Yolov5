# RESIZE import the modules
import os
from os import listdir
import cv2

# get the path/directory
folder_dir = "/content/yolov5/test_orig"
save_dir = "/content/yolov5/test_2"
dim=(403,302)
i=1

for image in os.listdir(folder_dir):
  if image.endswith(".jpg"):
    
    print(image)
    img = cv2.imread(os.path.join(folder_dir,image))
    img_small = cv2.resize(img, dim)
    new_fname = "{}.{}".format(str(image.split('.')[0]), "jpg")
    small_fname = os.path.join(save_dir, new_fname)
    cv2.imwrite(small_fname, img_small)
    i=i-1