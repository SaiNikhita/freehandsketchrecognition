import os

DATASET_PATH = r'C:\Users\Anudeep\Desktop\Projects\Free Hand Sketch Recognition\Dataset\png'

for roots, directories, files in os.walk(DATASET_PATH):
    for file in files:
        print("Path ", roots)
        print("File ", file)
        print("Label ", roots.split('\\')[-1])
