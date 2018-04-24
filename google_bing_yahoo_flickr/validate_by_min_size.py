import os, cv2


def is_valid_by_min_size(img):
    h, w, _ = img.shape
    _min = min(h, w)
    return _min > 50


root_dir = os.path.join(os.getcwd())

# import glob
# for filename in glob.iglob(root_dir + '**/*', recursive=True):
#      print(filename)

folders = []
for root, sub_dirs, files in os.walk(root_dir):
    for folder in sub_dirs:
        if folder.startswith('thumbs'):
            path = os.path.join(root, folder)
            folders.append(path)
# print('\n'.join(folders))

total_removed = 0
for folder_path in folders:
    removed_in_this_dir = 0
    for f_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, f_name)
        img = cv2.imread(img_path)
        if img and is_valid_by_min_size(img) is False:
            os.remove(img_path)
            total_removed += 1
            removed_in_this_dir += 1
    print('%s %s' % (removed_in_this_dir, folder_path))
print(total_removed)
print('DONE')

