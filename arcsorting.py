from PIL import Image
import os
import os.path
from shutil import copyfile
import sys

walk_dir = 'C:\\Users\\Admin\\Documents\\sisustusmööbel\\backup-10-2018\\htdocs\\images\\virtuemart\\product'
paysage_dir='C:\\Users\\Admin\\Pictures\\paysage' #Directory must exists
portrait_dir='C:\\Users\\Admin\\Pictures\\portrait' #Directory must exists
square_dir='C:\\Users\\Admin\\Pictures\\square' #Directory must exists


for root, subdirs, files in os.walk(walk_dir):
    for subdir in subdirs:
        for filename in files:
            print(filename)
            file_path = os.path.join(root, filename)
            if ".jpg" in str(file_path) or ".png" in str(file_path):
                with Image.open(file_path) as img:
                    width, height= img.size
                    arc = width/height
                    if arc>1:
                        print('paysage')
                        sort_path=paysage_dir+'\\'+filename 
                        if os.path.exists(sort_path)!=True:
                            copyfile(file_path,sort_path)
                            size=800, int(800/arc)
                    elif (arc<1):
                        print('portrait')
                        sort_path=portrait_dir+'\\'+filename
                        if os.path.exists(sort_path)!=True:
                            copyfile(file_path,sort_path)
                    else:
                        sort_path=square_dir+'\\'+filename 
                        if os.path.exists(sort_path)!=True:
                            copyfile(file_path,sort_path)
                                
        for root, subdirs, files in os.walk(walk_dir+'\\'+subdir):
            for filename in files:
                print(filename)
                file_path = os.path.join(root, filename)
                if ".jpg" in str(file_path) or ".png" in str(file_path):
                    try:
                        with Image.open(file_path) as img:
                            width, height= img.size
                            arc = width/height
                            if arc>1:
                                print('paysage')
                                sort_path=paysage_dir+'\\'+filename 
                                if os.path.exists(sort_path)!=True:
                                    copyfile(file_path,sort_path)
                                    size=800, int(800/arc)
                            elif (arc<1):
                                print('portrait')
                                sort_path=portrait_dir+'\\'+filename
                                if os.path.exists(sort_path)!=True:
                                    copyfile(file_path,sort_path)
                            else:
                                sort_path=square_dir+'\\'+filename 
                                if os.path.exists(sort_path)!=True:
                                    copyfile(file_path,sort_path)
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")




