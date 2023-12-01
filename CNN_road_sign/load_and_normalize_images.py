# https://stackoverflow.com/questions/53754662/mnist-dataset-structure
# I take the above link as a reference to create the following code.
# It is used to load and normalize images in the same way as the MNIST dataset.

import os
import pickle
import numpy as np
from PIL import Image

def preprocess_and_save_dataset(input_folder, output_file):
    dataset = []

    for class_folder in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_folder)

        for image_name in os.listdir(class_path):
            image_path = os.path.join(class_path, image_name)

            # Load and resize image
            img = Image.open(image_path)

            # Convert image to NumPy array and normalize pixel values to [0, 1]
            img_array = np.array(img, dtype=np.float32) / 255.0

            # Extract label from folder name
            label_str = class_folder.split()[0]
            label = int(label_str)

            # Combine image and label into a dictionary
            data = {"image": img_array, "label": label}

            # Append to the dataset
            dataset.append(data)

    # Save the dataset to a file using pickle
    with open(output_file, 'wb') as file:
        pickle.dump(dataset, file)

input_folder = os.getcwd() + '/NSCCAI/CNN_road_sign/resized_images'
output_file = os.getcwd() + '/NSCCAI/CNN_road_sign/road_signs_dataset.pkl'

preprocess_and_save_dataset(input_folder, output_file)
