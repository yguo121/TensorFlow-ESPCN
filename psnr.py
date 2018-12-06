import numpy as np
import math
from PIL import Image
import os

TEST_IMAGE_DIR = './test_images/Set14/'
TEST_RESULT_DIR = './result/Set14/'


def PSNR(image_a, image_b):
    image_a_data = np.asarray(image_a).astype('float32')
    image_b_data = np.asarray(image_b).astype('float32')
    diff = image_a_data - image_b_data
    diff = diff.flatten('C')
    rmse = math.sqrt(np.mean(diff ** 2.))
    return 20*math.log10(255.0/rmse)


if __name__ == '__main__':
    img_list = [filename for filename in os.listdir(
        TEST_IMAGE_DIR) if filename.endswith('jpg')]
    for img_name in img_list:
        try:
            hr_image = Image.open(
                TEST_RESULT_DIR+img_name.replace('.jpg', '_hr.jpg'))
            sr_image = Image.open(
                TEST_RESULT_DIR+img_name.replace('.jpg', '_sr.jpg'))
            lr_image = Image.open(
                TEST_RESULT_DIR+img_name.replace('.jpg', '_lr.jpg'))
        except:
            continue
        bi_image = lr_image.resize(sr_image.size, Image.BICUBIC)
        lr_image = lr_image.resize(sr_image.size)

        hr_lr_value = PSNR(hr_image, lr_image)
        hr_sr_value = PSNR(hr_image, sr_image)
        hr_bi_value = PSNR(hr_image, bi_image)
        print(img_name, '\t\tLR:\t%f\tESPCN:\t%f\tBICUBIC:\t%f' %
              (hr_lr_value, hr_sr_value, hr_bi_value))
