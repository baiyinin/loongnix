import xml.etree.ElementTree as ET 
import os
import glob,shutil
import os,glob
rootdata = r"E:\train_data9\safe_hat_diedao\falldata"
allxml  =  glob.glob(os.path.join(rootdata,"Annotations","*.xml"))
alljpg = glob.glob(os.path.join(rootdata,"JPEGImages","*.jpg"))
allxmlName  = []
for xml in allxml:
    name = xml.split(os.sep)[-1].split(".")[0]
    allxmlName.append(name)

allxmlJpeg = []
for jpg in alljpg:
    name = jpg.split(os.sep)[-1].split(".")[0]
    allxmlJpeg.append(name)

for x in allxmlName:
    if x not in allxmlJpeg:
        print("======",x)
        os.remove(os.path.join(rootdata,"Annotations",f"{x}.xml"))

for x in allxmlJpeg:
    if x not in allxmlName:
        print(x)
        # delpath = os.path.join(rootdata,"traindata",f"{x}.jpeg")
        # if not os.path.exists(delpath):
        #     delpath = os.path.join(rootdata, "traindata", f"{x}.jpg")
        # if not os.path.exists(delpath):
        #     delpath = os.path.join(rootdata, "traindata", f"{x}.png")
        # os.remove(delpath)
