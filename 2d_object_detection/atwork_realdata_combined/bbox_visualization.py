
from asyncore import file_dispatcher
import os
import glob as glob
import matplotlib.pyplot as plt
import cv2
import requests  # to download some data from internet
import random
import numpy as np

SEED = 42
np.random.seed(SEED)

# AllenKey
# Axis2
# Bearing2
# Drill
# F20_20_B
# F20_20_G
# Housing
# M20
# M20_100
# M30
# Motor2
# S40_40_B
# S40_40_G
# Screwdriver
# Spacer
# Wrench

class_names = ['AllenKey', 'Axis2', 'Bearing2', 'Drill', 'F20_20_B', 'F20_20_G', 'Housing', 'M20', 'M20_100', 'M30', 'Motor2', 'S40_40_B', 'S40_40_G', 'Screwdriver', 'Spacer', 'Wrench']
colors = np.random.uniform(0, 255, size=(len(class_names), 3))
# class_names = ['Ambulance', 'Bus', 'Car', 'Motorcycle', 'Truck']
# colors = np.random.uniform(0, 255, size=(len(class_names), 3))

# Function to convert bounding boxes in YOLO format to xmin, ymin, xmax, ymax.
def yolo2bbox(bboxes):
    xmin, ymin = bboxes[0]-bboxes[2]/2, bboxes[1]-bboxes[3]/2
    xmax, ymax = bboxes[0]+bboxes[2]/2, bboxes[1]+bboxes[3]/2
    return xmin, ymin, xmax, ymax

def plot_box(image, bboxes, labels):
    # Need the image height and width to denormalize
    # the bounding box coordinates
    h, w, _ = image.shape
    for box_num, box in enumerate(bboxes):
        x1, y1, x2, y2 = yolo2bbox(box)
        # denormalize the coordinates
        xmin = int(x1*w)
        ymin = int(y1*h)
        xmax = int(x2*w)
        ymax = int(y2*h)
        width = xmax - xmin
        height = ymax - ymin

        class_name = class_names[int(labels[box_num])]

        cv2.rectangle(
            image,
            (xmin, ymin), (xmax, ymax),
            color=colors[class_names.index(class_name)],
            thickness=2
        )

        font_scale = min(1, max(3, int(w/500)))
        font_thickness = min(2, max(10, int(w/50)))

        p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
        # Text width and height
        tw, th = cv2.getTextSize(
            class_name,
            0, fontScale=font_scale, thickness=font_thickness
        )[0]
        p2 = p1[0] + tw, p1[1] + -th - 10
        cv2.rectangle(
            image,
            p1, p2,
            color=colors[class_names.index(class_name)],
            thickness=-1,
        )
        cv2.putText(
            image,
            class_name,
            (xmin+1, ymin-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            (255, 255, 255),
            font_thickness
        )
    return image

# Function to plot images with the bounding boxes.
def plot(image_paths, label_paths, num_samples):
    all_training_images = glob.glob(image_paths)
    all_training_labels = glob.glob(label_paths)
    all_training_images.sort()
    all_training_labels.sort()

    num_images = len(all_training_images)

    plt.figure(figsize=(15, 12))
    for i in range(num_samples):
        j = random.randint(0, num_images-1)
        # j = 0
        image = cv2.imread(all_training_images[j])
        with open(all_training_labels[j], 'r') as f:
            bboxes = []
            labels = []
            label_lines = f.readlines()
            for label_line in label_lines:
                label = label_line.split(' ')[0]
                bbox_string = label_line.split(' ')[1:]
                x_c, y_c, w, h = bbox_string
                x_c = float(x_c)
                y_c = float(y_c)
                w = float(w)
                h = float(h.split('\n')[0])
                bboxes.append([x_c, y_c, w, h])
                labels.append(label)
        result_image = plot_box(image, bboxes, labels)
        plt.subplot(2, 2, i+1)
        plt.imshow(result_image[:, :, ::-1])
        plt.axis('off')
    plt.subplots_adjust(wspace=0)
    plt.tight_layout()
    plt.show()


def extarct_bbox_from_label(label_path):

    all_label_files = glob.glob(label_path + '/*.txt')

    for label_file in all_label_files:
        with open(label_file, 'r') as f:
            bboxes = []
            labels = []
            label_lines = f.readlines()
            for label_line in label_lines:
                label_objects = label_line.split(' ')
                label = label_objects[0]
                bbox_string = label_objects[4:8]
                x_min = (bbox_string[0])
                y_min = (bbox_string[1])
                x_max = (bbox_string[2])
                y_max = (bbox_string[3])
                bboxes.append([x_min, y_min, x_max, y_max])
                labels.append(label)

            # extract file name from label_path
            file_name = label_file.split('/')[-1]
            file_path = label_file.replace(file_name, '')
            label_folder_name = file_path.split('/')[-2] + '_bbox'
            aa = file_path.split('/')
            aa[-2] = label_folder_name
            new_label_folder_path = '/'.join(aa)

def main():
    # Visualize a few training images.
    plot(
        image_paths='<path-to-the-image-dir>/*',
        label_paths='<path-to-the-labels-dir>/*',
        num_samples=4,
    )


if __name__ == "__main__":
    main()
