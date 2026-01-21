import os
import xml.etree.ElementTree as ET
import shutil
from sklearn.model_selection import train_test_split
# SOURCE DATA
IMG_SRC = "datasets/Car_Plates/images"
ANN_SRC = "datasets/Car_Plates/annotations"


# YOLO OUTPUT DATA
IMG_TRAIN = "datasets/images/train"
IMG_VAL   = "datasets/images/val"
LBL_TRAIN = "datasets/labels/train"
LBL_VAL   = "datasets/labels/val"

os.makedirs(IMG_TRAIN, exist_ok=True)
os.makedirs(IMG_VAL, exist_ok=True)
os.makedirs(LBL_TRAIN, exist_ok=True)
os.makedirs(LBL_VAL, exist_ok=True)

# Read all XML files
xml_files = [f for f in os.listdir(ANN_SRC) if f.endswith(".xml")]
# Split 
train_files, val_files = train_test_split(
    xml_files, test_size=0.2, random_state=42
)

def convert(xml_file, img_out_dir, lbl_out_dir):
    xml_path = os.path.join(ANN_SRC, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Image filename
    img_name = root.find("filename").text
    img_path = os.path.join(IMG_SRC, img_name)

    # Image size
    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    # Label file path
    label_path = os.path.join(
        lbl_out_dir, img_name.rsplit(".", 1)[0] + ".txt"
    )

    with open(label_path, "w") as f:
        for obj in root.findall("object"):
            bbox = obj.find("bndbox")

            xmin = int(bbox.find("xmin").text)
            ymin = int(bbox.find("ymin").text)
            xmax = int(bbox.find("xmax").text)
            ymax = int(bbox.find("ymax").text)

            # YOLO normalization
            x_center = ((xmin + xmax) / 2) / w
            y_center = ((ymin + ymax) / 2) / h
            bw = (xmax - xmin) / w
            bh = (ymax - ymin) / h

            # Class id = 0 (license_plate)
            f.write(f"0 {x_center} {y_center} {bw} {bh}\n")

    # Copy image to output folder
    shutil.copy(img_path, img_out_dir)

# Convert training set
for xml in train_files:
    convert(xml, IMG_TRAIN, LBL_TRAIN)

# Convert validation set
for xml in val_files:
    convert(xml, IMG_VAL, LBL_VAL)

print(" XML → YOLO conversion completed successfully ")
print(f"Train images: {len(train_files)}")
print(f"Val images: {len(val_files)}")
