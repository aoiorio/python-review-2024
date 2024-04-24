import sys

# pathの設定 (pip showで出てきた、LocationのPATHを以下に設定) Set path
sys.path.append("/usr/local/lib/python3.11/site-packages")

import cv2

# Load the input images
image1 = cv2.imread("/Users/atoatoatomu/Downloads/ikemen.jpg")
image2 = cv2.imread("/Users/atoatoatomu/Downloads/images-angry.jpeg")

# Load the pre-trained face detection classifier
cascade_path = "/Users/atoatoatomu/Downloads/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Detect faces in the images
faces = face_cascade.detectMultiScale(image1)
faces1 = face_cascade.detectMultiScale(image2)

if len(faces) > 0:
    for x, y, w, h in faces:
        # Crop the face region from the first image
        cropped_face = image1[y : y + h, x : x + w]

        # Calculate dimensions for resizing the face from the second image
        desired_width = faces1[0][0] + faces1[0][2]
        desired_height = faces1[0][1] + faces1[0][3]

        # Resize the cropped face to match dimensions
        resized_cropped_face = cv2.resize(cropped_face, (desired_width, desired_height))

        # Position the resized face on the first image
        x_position = x
        y_position = y
        image1[
            y_position : y_position + desired_height,
            x_position : x_position + desired_width,
        ] = resized_cropped_face

    # Display the result
    cv2.imshow("Result", image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No faces found in the first image.")
