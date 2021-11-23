import os
import sys
import io
import datetime

os.system('git add .')
os.system('git commit -a -m update')
os.system('git push')

tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
print(tarihsaat)
print("git pushing completed")