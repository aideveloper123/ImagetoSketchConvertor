import cv2
# image =cv2.imread(r"image path")
image =cv2.imread(r"D:\learning\python\scripts\image.jpg")
# D:\learning\python\scripts\image.jpg

if image is None:
    print("could not open or find the file")
else:
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    inverted=255-gray_image

    blur=cv2.GaussianBlur(inverted,(21,21),0)
    inverted_blur=255-blur

    sketch=cv2.divide(gray_image,inverted_blur,scale=256.0)
    cv2.imwrite("sketch_image.png",sketch)
    cv2.imshow("sketch Image",sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                            

