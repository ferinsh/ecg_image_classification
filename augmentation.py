import cv2
import os
from concurrent.futures import ThreadPoolExecutor

image_path = 'data/ptb-xl_images_multiprocessed'

# def load_image(img_path):
#     img =  cv2.imread(img_path)
#     print('Loading image: ', img_path)
#     return img

# def load_image_from_folder_parellel(folder, max_workers = 6):
#     image_paths = [os.path.join(folder, filename) for filename in os.listdir(folder)]
#     images = []
#     with ThreadPoolExecutor(max_workers=max_workers) as executor:
#         results = executor.map(load_image, image_paths)
#         # images = [img for img in results if img is not None]
#     return images

# images = load_image_from_folder_parellel(image_path)


def load_images_in_batches(folder, batch_size = 50):
    image_paths = [os.path.join(folder, filename) for filename in os.listdir(folder)]
    for i in range(0, len(image_paths)):
        batch_paths = image_paths[i:i+batch_size]
        images = []
        for path in batch_paths:
            print(path)
            img = cv2.imread(path)
            if img is not None:
                images.append(img)
        yield images
    
for image_batch in load_images_in_batches(image_path):
    # print(image_batch)
    del image_batch