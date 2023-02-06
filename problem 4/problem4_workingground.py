"""
Author: Cray-sh
Date: 2023.02.06

This is problem 4, the final problem, for the course. 
Again, I will use several blocks to organize all of the pieces of this project before
putting them together in a more organized problem4_final.py

Problem Description:

"""
#shebang to be used in linux environments will be below here
#!/usr/bin/env python3

#%% Block 1 - this would be used to create createImage.py, and is becoming a scratch space

#modules/libraries to import

import os
import sys
import shutil
import psutil
from PIL import Image

path_for_linux = '//home//student-04-3ced89d2dcbd//supplier-data//images//'

#%% Block 1b - This is createImage.py
"""
Pretty much the same design as problem1, but tweaked a little,
they wanted 600x400 and to make sure to convert to RGB first
This is exactly createImage.py
"""
#!/usr/bin/env python3


from PIL import Image
import os
import sys

basepath = "//home//student-04-3ced89d2dcbd//supplier-data//images//"
new_path = basepath
new_ext = ".jpeg"

for entry in os.listdir(basepath):
 if os.path.isfile(os.path.join(basepath,entry)):
  fi,ext = os.path.splitext(entry)
  output_file = fi
  try:
   with Image.open(basepath + entry) as start_image:
    start_image_part1 = start_image.convert('RGB')
    start_image_complete = start_image_part1.resize((600,400)).save(new_path+output_file+new_ext,'JPEG')
  except OSError:
   print("Could not convert {}".format(output_file))


#%% Block 2 - This will be used to upload the converted pictures, below is the example they used
#which will need to be adjusted to use them

#!/usr/bin/env python3

import requests
#This example shows how a file can be uploaded using the python requests module
url = "http://localhost/upload"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

#%% Block 2b - Modified to use in our scenario, on linux vm

#This is the exact supplier_image_upload.py that was used in the lab

#!/usr/bin/env python3

import requests

url = "http://localhost/upload/"
#don't forget that slash at the end of upload!
path_of_pics = ""

for photo in os.listdir(path_of_pics):
    if photo.endswith('.jpeg'):
        with open(path_of_pics + photo, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(r.status_code)
    
    else:
        print("{} was not a jpeg and therefore not uploaded".format(photo))



#%% Block 3 - A script to convert text files to JSON files to be uploaded to fruits
# This will eventually become run.py
"""Example Json Object to upload

{"name": "Watermelon",
 "weight": 500,
 "description": "Watermelon is good for relieving heat,
 eliminating annoyance and quenching thirst. It contains a lot of water,
 which is good for relieving the symptoms of acute fever immediately.
 The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation.
 Watermelon also contains substances that can lower blood pressure.",
 "image_name": "010.jpeg"}

"""
#!/usr/bin/env python3

import requests
import os
import json
"""
Line 1 will be name, Line 2 will be weight, Line 3 will be description
Four fields necessary:
name (L1)
weight (L2)
description (L3)
image_name - will be image that you want with this data
"""
text_file_location = "~/supplier-data/descriptions/"
url = "http://34.171.126.190/fruits/"


















#%% Block 2 - 




























