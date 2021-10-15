import os
import gdxray
import utils
import visualize
import numpy as np
from visualize import display_images
config = gdxray.TrainConfig()
DATA_DIR = os.path.expanduser("C:\\Users\\sushr\\Desktop\\akjfawlehfkajsgdfoawefbkajs\\maxfargsen\\GDXray") 


dataset = gdxray.XrayDataset()
dataset.load_gdxray(DATA_DIR, "train", "Castings")
   
# Must call before using the dataset
dataset.prepare()

print("Image Count: {}".format(len(dataset.image_ids)))
print("Class Count: {}".format(dataset.num_classes))
for i, info in enumerate(dataset.class_info):
    print("{:3}. {:50}".format(i, info['name']))

image_ids = np.random.choice(dataset.image_ids, 4)
for image_id in image_ids:
    image = dataset.load_image(image_id)
    mask, class_ids = dataset.load_mask(image_id)
    visualize.display_top_masks(image, mask, class_ids, dataset.class_names)