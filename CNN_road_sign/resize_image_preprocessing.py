import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, target_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for class_folder in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_folder)
        output_class_path = os.path.join(output_folder, class_folder)

        if not os.path.exists(output_class_path):
            os.makedirs(output_class_path)

        for image_name in os.listdir(class_path):
            image_path = os.path.join(class_path, image_name)
            output_path = os.path.join(output_class_path, "resized_" + image_name)

            img = Image.open(image_path)
            img_resized = img.resize(target_size, Image.ANTIALIAS) # type: ignore
            img_resized.save(output_path)

input_folder = os.getcwd() + '/NSCCAI/CNN_road_sign/road_signs_img'
output_folder = os.getcwd() + '/NSCCAI/CNN_road_sign/resized_images'
# Resize Images to a Consistent Size: 224 x 224
target_size = (224, 224)

resize_images_in_folder(input_folder, output_folder, target_size)
