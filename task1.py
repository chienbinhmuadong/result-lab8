import cv2
import numpy as np

img = cv2.imread("variant-5.jpg", cv2.IMREAD_COLOR)

gaussian_noise = np.random.normal(0, 100, img.shape)

img_noise = gaussian_noise + img

img_noised = np.clip(img_noise, 0, 255).astype(np.uint8)
cv2.imwrite("variant-5.jpg", img_noised)