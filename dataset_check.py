import os 

train_img_count = len(os.listdir(path = "datasets/train/images"))
test_img_count = len(os.listdir(path = "datasets/test/images"))
val_img_count = len(os.listdir(path = "datasets/valid/images"))

names = {'Chassis', 'back_cover', 'calculator', 'front_panel', 'motor', 'motor_cover', 'number_pad', 'objects', 'screw', 'screw_driver', 'vehicle_body', 'wheel'}

from pathlib import Path
from collections import Counter

train_counts = Counter(
    int(line.split()[0]) for p in Path("datasets/train/labels").glob("*.txt") for line in p.read_text().splitlines() if line.strip()
)

train_parts_label_counts = {"Chassis" : train_counts[0], "back_cover" : train_counts[1], "calculator" : train_counts[2], "front_panel" : train_counts[3],
                      "motor" : train_counts[4], "motor_cover" : train_counts[5], "number_pad" : train_counts[6], "objects" : train_counts[7],
                      "screw" : train_counts[8], "screw_driver" : train_counts[9], "vehicle_body" : train_counts[10], "wheel" : train_counts[11]}



test_counts = Counter(
    int(line.split()[0]) for p in Path("datasets/test/labels").glob("*.txt") for line in p.read_text().splitlines() if line.strip()
)

test_parts_label_counts = {"Chassis" : test_counts[0], "back_cover" : test_counts[1], "calculator" : test_counts[2], "front_panel" : test_counts[3],
                      "motor" : test_counts[4], "motor_cover" : test_counts[5], "number_pad" : test_counts[6], "objects" : test_counts[7],
                      "screw" : test_counts[8], "screw_driver" : test_counts[9], "vehicle_body" : test_counts[10], "wheel" : test_counts[11]}


val_counts = Counter(
    int(line.split()[0]) for p in Path("datasets/valid/labels").glob("*.txt") for line in p.read_text().splitlines() if line.strip()
)


val_parts_label_counts = {"Chassis" : val_counts[0], "back_cover" : val_counts[1], "calculator" : val_counts[2], "front_panel" : val_counts[3],
                      "motor" : val_counts[4], "motor_cover" : val_counts[5], "number_pad" : val_counts[6], "objects" : val_counts[7],
                      "screw" : val_counts[8], "screw_driver" : val_counts[9], "vehicle_body" : val_counts[10], "wheel" : val_counts[11]}

print("Image Counts".center(100,"*"))
print(f"\nTraining Image Counts: {train_img_count}")
print(f"Tetsing Image Counts: {test_img_count}")
print(f"Validation Image Counts: {val_img_count}")
print("\n\n")
print("Labels Counts".center(100,"*"))
print(f"\nTraining Label Counts: {train_parts_label_counts}")
print(f"Testing Label Counts: {test_parts_label_counts}")
print(f"Validation Label Counts: {val_parts_label_counts}")

