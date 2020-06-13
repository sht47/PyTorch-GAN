import glob
from tqdm import tqdm
from PIL import Image

img_files_testA = glob.glob("cad2real_A/testA/*JPG")
img_files_testB = glob.glob("cad2real_B/testB/*JPG")
img_files_trainA = glob.glob("cad2real_A/trainA/*JPG")
img_files_trainB = glob.glob("cad2real_B/trainB/*JPG")
print(len(img_files_testA))
print(len(img_files_testB))
print(len(img_files_trainA))
print(len(img_files_trainB))
# for img_file in tqdm(img_files):
#     # print(img_file)
#     img = Image.open(img_file).convert("RGB")
#     if img.size[0] != 256 or img.size[1] != 256:
#         print(img_file)
    # img_256 = img.resize((256, 256))
    # img_256.save(img_file)
    # print(img.size)
