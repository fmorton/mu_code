import cv2 as cv
import time

WINDOW_NAME = "opencv_window"

cv.startWindowThread()
cv.namedWindow(WINDOW_NAME)  # , cv.CV_WINDOW_AUTOSIZE)

images = []
# flags = cv.IMREAD_GRAYSCALE
flags = cv.IMREAD_COLOR

images.append(cv.imread("/Users/fmorton/Desktop/Keep/0.webp", flags))
images.append(cv.imread("/Users/fmorton/Desktop/Keep/0-1.webp", flags))
images.append(cv.imread("/Users/fmorton/Desktop/Keep/0-2.webp", flags))
images.append(cv.imread("/Users/fmorton/Desktop/Keep/0-3.webp", flags))
images.append(cv.imread("/Users/fmorton/Desktop/Keep/0-4.webp", flags))
images.append(cv.imread("/Users/fmorton/Desktop/Keep/0-5.webp", flags))
images.append(cv.imread("/Users/fmorton/Desktop/Keep/0-6.webp", flags))
images.append(cv.imread("/Users/fmorton/Desktop/Keep/0-7.webp", flags))

for times in range(60):
    for image in images:
        cv.imshow(WINDOW_NAME, image)
        cv.waitKey(1)


cv.waitKey(1)
cv.destroyAllWindows()
cv.waitKey(1)
