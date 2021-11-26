import os
import sys
import io
import datetime

tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
tarih = datetime.datetime.now().strftime("%d-%m-%Y");

os.system('git add .')
os.system('git commit -a -m "update '+str(tarihsaat)+'"')
os.system('git push')


print(tarih)
print("git pushing completed " +tarihsaat)