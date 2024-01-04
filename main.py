import os
import requests
from natsort import natsorted

def get_images_from_folder(folder_path):
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in natsorted(files):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_files.append(os.path.join(root, file))
    return image_files

images = get_images_from_folder("images")
for image in images:
    print(image)