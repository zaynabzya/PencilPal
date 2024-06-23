
import streamlit as st
import numpy as np

import cv2
from io import BytesIO
import matplotlib.pyplot as plt

st.title("PencilPal")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_image:
    # Read image using OpenCV
    Image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)

plt.imshow(Image)
plt.title("Original Image")
plt.axis('off')  # Hide the axis
plt.show()

inverted_image = 255 - Image
plt.imshow(inverted_image)
plt.title("Inverted Image")
plt.axis('off')  # Hide the axis
plt.show()

pencil_sketch = cv2.GaussianBlur(inverted_image, (21, 21), 0)
plt.imshow(blurred_image)
plt.title("Blurred Image")
plt.axis('off')  # Hide the axis
plt.show()

st.image(pencil_sketch, caption="Pencil Sketch")

buf = BytesIO()
cv2.imencode('.jpg', pencil_sketch, [cv2.IMWRITE_JPEG_QUALITY, 80])[1].tobytes()
st.download_button("Download Pencil Sketch", buf.getvalue(), "pencil_sketch.jpg", "image/jpg")
