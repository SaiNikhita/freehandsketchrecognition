import os
import shutil
import random

DATASET_PATH = r'C:\Users\Vanitha\Desktop\project\Dataset\png'


def get_images_in_folder(folder_path):
    return [image for image in os.listdir(folder_path) if (image.endswith(".png"))]


def split_images(images, split_percent):
    split_index = int(len(images) * split_percent)
    train = images[:split_index]
    test = images[split_index:]
    return train, test


def create_folder(path, folder_name):
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        shutil.rmtree(folder_path)
        os.makedirs(folder_path)
    return folder_path


def split_dataset(split_percent):
    for roots, directories, files in os.walk(DATASET_PATH):
        images = get_images_in_folder(roots)
        random.shuffle(images)

        if images:
            train_set, test_set = split_images(images, split_percent)
            train_folder_path = create_folder(roots, "train")
            test_folder_path = create_folder(roots, "test")

            for sample in train_set:
                sample_path = os.path.join(roots, sample)
                shutil.copy(sample_path, train_folder_path)

            for sample in test_set:
                sample_path = os.path.join(roots, sample)
                shutil.copy(sample_path, test_folder_path)


split_dataset(0.8)