import os
import yaml 
from pathlib import Path
from collections import Counter

cls_names = ['Chassis', 'back_cover', 'calculator', 'front_panel', 'motor', 'motor_cover', 'number_pad', 'objects', 'screw', 'screw_driver', 'vehicle_body', 'wheel']


def img_count(image_path):
    return len(os.listdir(path = image_path))

#--------------------------------------------------------------------

with open(file= "datasets/data.yaml", mode="r") as file:
    config = yaml.safe_load(file)
names = config["names"]
def counts(label_path):
    counting = Counter(
        int(line.split()[0]) for p in Path(label_path).glob("*.txt") for line in p.read_text().splitlines() if line.strip()
    )

    label_counts = {
        name : counting[i]
        for i, name in enumerate(names)
    }

    return label_counts



print("Image Counts".center(100,"*"))
train_img_count = img_count("datasets/train/images")
print(f"\nTraining Image Counts: {train_img_count}")
test_img_count = img_count("datasets/test/images")
print(f"Tetsing Image Counts: {test_img_count}")
val_img_count = img_count("datasets/valid/images")
print(f"Validation Image Counts: {val_img_count}")
print("\n\n")
print("Labels Counts".center(100,"*"))
train_parts_label_counts = counts("datasets/train/labels")
print(f"\nTraining Label Counts: {train_parts_label_counts}")
test_parts_label_counts = counts("datasets/test/labels")
print(f"Testing Label Counts: {test_parts_label_counts}")
val_parts_label_counts = counts("datasets/valid/labels")
print(f"Validation Label Counts: {val_parts_label_counts}")

print("\n")
print("-".center(100,"-"))

#----------------------------------------------------------------------------------------

def image_label_checks(path_img, path_label):

    images = Path(path_img)
    labels = Path(path_label)

    images_name = set(p.stem for p in images.glob("*.jpg"))
    labels_name = set(p.stem for p in labels.glob("*.txt"))

    return images_name.difference(labels_name)

missing_train = image_label_checks("datasets/train/images", "datasets/train/labels")
print("Training misses:",missing_train)
missing_test = image_label_checks("datasets/test/images", "datasets/test/labels")
print("Testing misses:",missing_test)
missing_val= image_label_checks("datasets/valid/images", "datasets/valid/labels")
print("Validation misses:",missing_val)