Python
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
Use code with caution.
Explanation:

Import OpenCV: We import the cv2 library for image processing.
sketch function: This function takes the image path as input and performs the following steps:
Reads the image in grayscale mode using cv2.imread.
Inverts the grayscale image using bitwise NOT operation (255 - image).
Applies Gaussian blurring to the inverted image for edge detection using cv2.GaussianBlur.
Performs a Dodge blend between the original grayscale image and the blurred image using division (cv2.divide) to create a high-contrast sketch effect.
Optionally shows the original image and the sketch using cv2.imshow and waits for key press (cv2.waitKey).
Returns the grayscale sketch image.
Example usage: We call the sketch function with the image path and store the resulting sketch image in a variable.
Save the sketch: We use cv2.imwrite to save the sketch image to a new file named "pencil_sketch.jpg".
Note:

This is a basic implementation. You can experiment with different blurring techniques and parameters for a more artistic effect.
Remember to install OpenCV using pip install opencv-python before running the script.
Make sure you have the image file in the same directory as the script.