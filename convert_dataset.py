import os
import xml.etree.ElementTree as ET
import shutil
from sklearn.model_selection import train_test_split

# ORIGINAL DATASET
IMG_SRC = "datasets/Car_Plates/images"
ANN_SRC = "datasets/Car_Plates/annotations"

# YOLO DATASET
IMG_TRAIN = "datasets/images/train"
IMG_VAL = "datasets/images/val"
LBL_TRAIN = "datasets/labels/train"
LBL_VAL = "datasets/labels/val"

os.makedirs(IMG_TRAIN, exist_ok=True)
os.makedirs(IMG_VAL, exist_ok=True)
os.makedirs(LBL_TRAIN, exist_ok=True)
os.makedirs(LBL_VAL, exist_ok=True)

xml_files = [f for f in os.listdir(ANN_SRC) if f.endswith(".xml")]
train_xml, val_xml = train_test_split(xml_files, test_size=0.2)

def convert(xml_file, img_dst, lbl_dst):
    tree = ET.parse(os.path.join(ANN_SRC, xml_file))
    root = tree.getroot()

    img_name = root.find("filename").text
    w = int(root.find("size/width").text)
    h = int(root.find("size/height").text)

    label_file = os.path.join(lbl_dst, img_name.replace(".jpg", ".txt"))

    with open(label_file, "w") as f:
        for obj in root.findall("object"):
            b = obj.find("bndbox")
            xmin, ymin, xmax, ymax = map(int, [
                b.find("xmin").text,
                b.find("ymin").text,
                b.find("xmax").text,
                b.find("ymax").text
            ])

            xc = ((xmin + xmax) / 2) / w
            yc = ((ymin + ymax) / 2) / h
            bw = (xmax - xmin) / w
            bh = (ymax - ymin) / h

            f.write(f"0 {xc} {yc} {bw} {bh}\n")

    shutil.copy(os.path.join(IMG_SRC, img_name), img_dst)

for x in train_xml:
    convert(x, IMG_TRAIN, LBL_TRAIN)

for x in val_xml:
    convert(x, IMG_VAL, LBL_VAL)

print(" Dataset converted successfully ")
