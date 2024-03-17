import cv2

def sketch(image_path):
  """
  Converts an image to a pencil sketch using OpenCV.

  Args:
      image_path: Path to the input image file.

  Returns:
      A grayscale image representing the pencil sketch.
  """
  # Read the image in grayscale mode (0)
  image = cv2.imread(image_path, 0)

  # Invert the grayscale image
  inverted_image = 255 - image 

  # Apply Gaussian blurring to the inverted image
  blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

  # Dodge blend the original grayscale image with the blurred image
  pencil_sketch = cv2.divide(image, blurred_image, scale=256.0)

  # Show the original image and the sketch
  # cv2.imshow("Original Image", image)
  # cv2.imshow("Pencil Sketch", pencil_sketch)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

  return pencil_sketch

# Example usage (replace 'image.jpg' with your image path)
sketch_image = sketch('image.jpg')

# You can save the sketch image using OpenCV
cv2.imwrite('pencil_sketch.jpg', sketch_image)
