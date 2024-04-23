import sys

# pathの設定 (pip showで出てきた、LocationのPASSを以下に設定) Set path
sys.path.append('/Users/atoatoatomu/Desktop/2024-programming-class/python_review/photo-cut-circle/photo-cut-circleenv/lib/python3.12/site-packages')

import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Get the image's coordinate
im_gray = cv2.imread('/Users/atoatoatomu/Downloads/cuisine.png', cv2.IMREAD_GRAYSCALE)

y = im_gray.shape[0]
x = im_gray.shape[1]
radius = x / 4

# Read image
img_rgb = plt.imread('/Users/atoatoatomu/Downloads/cuisine.png')
fig, ax = plt.subplots()
im = ax.imshow(img_rgb)

# Move the point to the center
patch = patches.Circle((x / 2, y / 2), radius=radius, transform=ax.transData)

im.set_clip_path(patch)
ax.axis('off')
plt.savefig('clip_circle.jpg',dpi=150)