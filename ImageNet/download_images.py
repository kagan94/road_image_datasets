import os.path
import urllib.request, urllib.error

tgt_file = 'list_of_road_image_from_imagenet.synset.txt'
res_dir = 'images'
img_urls = []
with open(tgt_file, 'r') as f:
    for line in f:
        img_url = line.strip()
        img_urls.append(img_url)

total = len(img_urls)
for i, img_url in enumerate(img_urls):
    # if i < 493:
    #     continue
    try:
        res_fpath = os.path.join(res_dir, ('%s.jpg' % i))
        urllib.request.urlretrieve(img_url, res_fpath)
    except urllib.error.HTTPError as e:
        print('Can\'t download the image %s (HTTP error)' % img_url)
    except urllib.error.URLError as e:
        print('Can\'t download the image %s (URL error)' % img_url)
    except UnicodeEncodeError as e:
        print('Can\'t download the image %s (UnicodeEncode error)' % img_url)
    print('%s/%s' % (i, total))


# ==============================
# Remove non-found Flickr images

import cv2
import numpy as np
from Road_classification_NN.helpers import get_file_paths

# dir = 'images'
# not_found_img_path = os.path.join(dir, '1201.jpg')
# img_not_found = cv2.imread(not_found_img_path)
# imgs = get_file_paths(dir)
# while imgs:
#     img_path = imgs.pop(0)
#     img = cv2.imread(img_path)
#     if np.all(img == img_not_found):
#         os.remove(img_path)
#         print('Removed %s' % img_path)
#     print(img_path, len(imgs))
