import numpy as np
from PIL import Image
import kernels

kernels = kernels.get_kernels()


img = Image.open("../../plane.jpg")
img_gray = img.convert('L')

img_normalized = np.array(img_gray)
img_normalized -= img_normalized.min()
img_normalized = img_normalized.astype('float64')

img_normalized /= img_normalized.max()
img_normalized = img_normalized

w, h = img.size


transformed_img = np.zeros_like((w, h))

