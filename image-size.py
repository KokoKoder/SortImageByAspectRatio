from PIL import Image
import os
import os.path
from shutil import copyfile
import sys

walk_dir = 'D:\\'


for root, subdirs, files in os.walk(walk_dir):
    
    for subdir in subdirs:
        for filename in files:
            file_path = os.path.join(root, filename)
            if ".jpg" in str(file_path) or ".png" in str(file_path):
                with Image.open(file_path) as img:
                    width, height= img.size
                    print(filename,' width: ',width,' height: ',height)
                    

                   

