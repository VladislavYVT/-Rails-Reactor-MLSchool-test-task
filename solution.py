import sys
import numpy as np
from PIL import Image
from os import listdir


def check_similarity(img, img_list, imgs, image_name):
    similar_pairs = []
    im = np.asarray(img.resize((4,4), resample=Image.BICUBIC),dtype=float)
    for k in range(len(img_list)):
        if(np.sum(np.abs(im-img_list[k]))/255)<=2:
            similar_pairs.append([image_name,imgs[k]])
    return similar_pairs

try:
    directory = sys.argv[1]+'/'
    files = listdir(sys.argv[1])

    imgs = [directory+f for f in files]

    all_images=[]
    for i in range(len(imgs)):
        base = Image.open(imgs[i])
        arr_imag=np.asarray(base.resize((4,4), resample=Image.BICUBIC),dtype=float)
        all_images.append(arr_imag)
    all_images = np.array(all_images)

    result = []
    for i in imgs:
        result.append(check_similarity(Image.open(i), all_images, imgs, i))

    xd = []
    for j in result:
        for k in j:
            if k[0] != k[1] and [k[1], k[0]] not in xd:
                xd.append(k)

    print(np.expand_dims(xd, axis=0))
except FileNotFoundError:
    print('Wrong path to directory with images')