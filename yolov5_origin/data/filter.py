import os
import sys
import glob
import xml.etree.ElementTree as ET
import numpy as np
from data.data_config import get_train_data
from PIL import  Image
output_folder = "txtlabel"
import shutil
all_file = glob.glob(get_train_data() + "Annotations_origin" +"/*.xml") #F://xxxx/Annotations\xxx.xml

def convert_annotation(ffile,image_id):
    in_file = open(get_train_data() + "Annotations_origin" + '/%s.xml' % (image_id),encoding="utf-8")
    tree = ET.parse(in_file)
    root = tree.getroot()
    contins = False
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls == "hat":
            contins = True
    exists = os.path.exists(os.path.join(r"E:\train_data9\safe_hat_diedao\traindata",f"{image_id}.jpg"))
    if contins and exists:
        shutil.copy(os.path.join(r"E:\train_data9\safe_hat_diedao\traindata",f"{image_id}.jpg"),
                    os.path.join(r"E:\train_data9\safe_hat_diedao\JPEGImages",f"{image_id}.jpg"))

        shutil.copy(os.path.join(r"E:\train_data9\safe_hat_diedao\Annotations_origin",f"{image_id}.xml"),
                    os.path.join(r"E:\train_data9\safe_hat_diedao\Annotations",f"{image_id}.xml"))

if __name__ == "__main__":
    for file in all_file:
        image_id = file.split("\\")[-1].split(".")[0]
        convert_annotation(file,image_id)