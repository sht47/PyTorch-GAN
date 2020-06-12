import os
import shutil
import glob 
import random 

# img_paths = glob.glob('celebA/*png')
# print(len(img_paths))
# random.shuffle(img_paths)
os.makedirs('celebA/train', exist_ok=True)
os.makedirs('celebA/val', exist_ok=True)
os.makedirs('celebA/test', exist_ok=True)

## train_paths = img_paths[:7000] 
## val_paths = img_paths[7000:8500] 
## test_paths = img_paths[8500:10000]
## 
## for train_path in train_paths:
##     new_path = train_path.replace('celebA', 'celebA/train')
##     shutil.move(train_path, new_path)
## for val_path in val_paths:
##     new_path = val_path.replace('celebA', 'celebA/val')
##     shutil.move(val_path, new_path)
## for test_path in test_paths:
##     new_path = test_path.replace('celebA', 'celebA/test')
##     shutil.move(test_path, new_path)

print('train: {}\nval: {}\ntest : {}\n'.format(len(os.listdir('celebA/train')), len(os.listdir('celebA/val')), len(os.listdir('celebA/test'))))
