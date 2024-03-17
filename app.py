import cv2
import streamlit as st
import numpy as np

SUPPORTED_IMAGE_FORMATS = ("jpg", "jpeg", "png")  # Add more formats if needed

def sketch(image):
  """
  Converts an image to a pencil sketch using OpenCV.

  Args:
      image: A NumPy array representing the image data.

  Returns:
      A NumPy array representing the grayscale pencil sketch.
  """
  # Convert image to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Invert the grayscale image
  inverted_image = 255 - gray_image

  # Apply Gaussian blurring to the inverted image
  blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

  # Dodge blend the original grayscale image with the blurred image
  pencil_sketch = cv2.divide(gray_image, blurred_image, scale=256.0)

  return pencil_sketch

def main():
  """
  Streamlit application for image upload and conversion to sketch.
  """
  st.title("Image to Pencil Sketch Converter")

  uploaded_file = st.file_uploader("Choose an image to convert:", type=SUPPORTED_IMAGE_FORMATS)

  if uploaded_file is not None:
    # Validate file extension
    file_name = uploaded_file.name
    file_extension = file_name.split(".")[-1].lower()
    if file_extension not in SUPPORTED_IMAGE_FORMATS:
      st.error(f"Unsupported file format. Please upload an image in one of the following formats: {', '.join(SUPPORTED_IMAGE_FORMATS)}")
      return

    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    sketch_image = sketch(image)

    # Display original and sketch images side-by-side
    st.subheader("Original Image")
    st.image(image, channels="BGR")
    st.subheader("Pencil Sketch")
    st.image(sketch_image, channels="grayscale")

if __name__ == "__main__":
  main()
