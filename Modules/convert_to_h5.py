import glob
from random import shuffle
import h5py
import numpy as np
import cv2
import math
import time


def normalize_and_write_data_into_h5_file(dest_filepath, filepaths_list, n_px, n_channels=3):
    data_shape = (len(filepaths_list), n_px * n_px * n_channels)
    dataset_name = "input_data"
    with h5py.File(dest_filepath, 'a') as f:
        f.create_dataset(dataset_name, data_shape, np.float32)
        for i in range(len(filepaths_list)):
            filepath = filepaths_list[i]
            img = cv2.imread(filepath)
            img = cv2.resize(img, (n_px, n_px), interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = img / 255
            img = img.ravel()
            f[dataset_name][i, ...] = img[None]


def write_labels_into_h5_file(dest_filepath, labels):
    dataset_name = "input_labels"
    with h5py.File(dest_filepath, 'a') as f:
        f.create_dataset(dataset_name, (len(labels), 160), np.int8)
        f[dataset_name][...] = labels


def convert_images_to_data_in_h5_file(src_img_filepath_pattern, dest_h5_file_path, n_px,
                                      n_channels=3, batch_size=1024):
    src_filepaths = glob.glob(src_img_filepath_pattern)
    labels_path = 'Dataset\png\*'
    labels_folders = glob.glob((labels_path))
    labels_list = [i.split("\\")[-1] for i in labels_folders]
    labels_numbers = [labels_list.index(i.split('\\')[-2]) for i in src_filepaths]
    labels = []
    for i in labels_numbers:
        arr = [0] * 160
        arr[i] = 1
        labels.append(arr)
    t = list(zip(src_filepaths, labels))
    shuffle(t)
    src_filepaths, labels = zip(*t)
    m = len(src_filepaths)
    n_complete_batches = math.ceil(m / batch_size)
    for i in range(n_complete_batches):
        print('Creating file', (i + 1))
        dest_file_path = dest_h5_file_path + str(i + 1) + ".h5"
        start_pos = i * batch_size
        end_pos = min(start_pos + batch_size, m)
        src_filepaths_batch = src_filepaths[start_pos: end_pos]
        labels_batch = labels[start_pos: end_pos]
        normalize_and_write_data_into_h5_file(dest_file_path, src_filepaths_batch, n_px)
        write_labels_into_h5_file(dest_file_path, labels_batch)


src_filepath_pattern = 'Dataset\png\*\*.PNG'
dest_filepath = 'Dataset/H5Files/batch'
n_px = 224
n_channels = 3
tic = time.process_time()
convert_images_to_data_in_h5_file(src_filepath_pattern, dest_filepath, n_px, n_channels)
toc = time.process_time()
print('Time taken for creating the h5 file is', (toc-tic)*1000, 'ms')


"""src_filepath_pattern = 'Dataset\png\*\*.PNG'
src_filepaths = glob.glob(src_filepath_pattern)
labels_path = 'Dataset\png\*'
labels_folders = glob.glob((labels_path))
labels_list = [i.split("\\")[-1] for i in labels_folders]
labels_numbers = [labels_list.index(i.split('\\')[-2]) for i in src_filepaths]
labels = []
for i in labels_numbers:
    arr = [0] * 160
    arr[i] = 1
    labels.append(arr)"""