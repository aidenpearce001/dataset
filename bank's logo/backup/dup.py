import glob
from os.path import join
import os
a = glob.glob("*.jpg")
for i in a:
    file_name = i.split('.')
    if os.path.exists(i) == True and os.path.exists(file_name[0]+'.txt') == False:
        os.remove(i)