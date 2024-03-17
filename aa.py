import cv2
import streamlit as st
import numpy as np

SUPPORTED_IMAGE_FORMATS = ("jpg", "jpeg", "png")  # List of supported formats

def sketch(image):
  """Converts an image to a pencil sketch using OpenCV."""
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  inverted = 255 - gray_image
  blur = cv2.GaussianBlur(inverted, (21, 21), 0)
  inverted_blur = 255 - blur
  sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
  return sketch

def main():
  st.title("Image to Pencil Sketch Converter")

  uploaded_file = st.file_uploader("Choose an image to convert:", type=SUPPORTED_IMAGE_FORMATS)

  if uploaded_file is not None:
    # Validate file extension
    file_name = uploaded_file.name
    file_extension = file_name.split(".")[-1].lower()
    if file_extension not in SUPPORTED_IMAGE_FORMATS:
      st.error(
        f"Unsupported file format. Please upload an image in one of the following formats: {', '.join(SUPPORTED_IMAGE_FORMATS)}"
      )
      return

    try:
      image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
      sketch_image = sketch(image)

      st.subheader("Original Image")
      st.image(image, channels="BGR")

      st.subheader("Pencil Sketch")
      st.image(sketch_image, channels="grayscale")

      st.success("Sketch conversion successful!")
    except Exception as e:
      st.error(f"An error occurred during image processing: {e}")

if __name__ == "__main__":
  main()
