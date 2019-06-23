import os

DATASET_PATH = r'C:\Users\Anudeep\Desktop\Projects\Free Hand Sketch Recognition\Dataset\png'

for roots, directories, files in os.walk(DATASET_PATH):
    for file in files:
        print("Path of directory ", roots)
        print("Filename ", file)
        print("Path of sample ", os.path.join(roots, file))
        print("Label ", roots.split('\\')[-1])
