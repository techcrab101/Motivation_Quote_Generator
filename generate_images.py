from skimage import transform
from skimage import filters
from skimage import img_as_ubyte
import cv2
# import argparse
import numpy as np
import imutils

# ap = argparse.ArgumentParser()
# ap.add_argument('-i', '--image', required=True,
#         help='Path to input image')
# args = vars(ap.parse_args())

# img = cv2.imread(args['image'])


def carve_image(img, size = 480, target_size = 720):
    width, height = img.shape[1], img.shape[0]
   
    direction = 'vertical'

    rotate = False
    if width < height:
        rotate = True
        img = imutils.rotate_bound(img, 90)
    
    if height > size:
        img = cv2.resize(img, None, fx=size/height, fy=size/height, interpolation=cv2.INTER_AREA)
        width, height = img.shape[1], img.shape[0]
    
    seams_to_remove = max([width, height]) - min([width, height])
    
    normal_resize = cv2.resize(img, None, fx=height/width, fy=1, interpolation=cv2.INTER_AREA)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mag = filters.sobel(gray.astype('float'))
    
    for numSeams in range(1, seams_to_remove):
        try:
            carved = img_as_ubyte(carved)
            gray = cv2.cvtColor(carved, cv2.COLOR_BGR2GRAY)
            mag = filters.sobel(gray.astype('float'))
            carved = transform.seam_carve(carved, mag, direction, 1)
        except:
            carved = transform.seam_carve(img, mag, direction, numSeams)
    
    carved = img_as_ubyte(carved)
    if rotate:
        carved = imutils.rotate_bound(carved, 270)

    width, height = carved.shape[1], carved.shape[0]
    carved = cv2.resize(carved, None, fx=target_size/height, fy=target_size/height, interpolation=cv2.INTER_AREA)

    return carved

# carved = carve_image(img)

# index = args['image'].find('.')
# new_img_path = args['image'][:index]+'_carved'+args['image'][index:]
# cv2.imwrite(new_img_path, carved)
