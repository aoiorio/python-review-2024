import sys
sys.path.append(
    "/Users/atoatoatomu/Desktop/2024-programming-class/python_review/face-glasses/face-glasses-env/lib/python3.12/site-packages"
)

import face_glasses_def
from PIL import Image

image_path = "/Users/atoatoatomu/Downloads/aaa.jpg"
glasses_image = Image.open("/Users/atoatoatomu/Downloads/glasses.jpg")
image_path_open = Image.open(image_path)

# get Coordinate of face line, detector means 顔検出器
face_detect = face_glasses_def.recognize_face(image_path)

# for pasting glasses image to monariza, I'll resize it.
(width, height) = (glasses_image.width // 20, glasses_image.height // 20)
glasses_resized = glasses_image.resize((width, height))
glasses_resized.save('glasses_resized.png', quality=95)

# set resized glasses image
glasses_image = Image.open("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/face-glasses/glasses_resized.png")

with Image.open(image_path) as back_ground_image:
    back_image = back_ground_image.copy()
    back_image.paste(glasses_image, face_detect, glasses_image)
    back_image.save('/Users/atoatoatomu/Downloads/result-glasses.jpg', quality=95)
