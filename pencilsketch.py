import cv2
from io import BytesIO
import streamlit as st
import numpy as np

st.title("PencilPal")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])

Image = None  # Initialize Image variable

if uploaded_image:
    # Read image using OpenCV
    image_data = uploaded_image.read()
    nparr = np.frombuffer(image_data, np.uint8)
    Image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)  # Convert to RGB for display

if Image is not None:
    inverted_image = 255 - Image
    pencil_sketch = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    st.image(pencil_sketch, caption="Pencil Sketch")

    # Prepare download button
    buf = BytesIO()
    cv2.imencode('.jpg', pencil_sketch, [cv2.IMWRITE_JPEG_QUALITY, 80])[1].tofile(buf)
    st.download_button("Download Pencil Sketch", buf.getvalue(), "pencil_sketch.jpg", "image/jpg")
else:
    st.write("Upload an image to generate a pencil sketch.")
