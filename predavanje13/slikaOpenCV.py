import cv2 as cv
print(cv.__version__)

img = cv2.imread('predavanje13/auto.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.imwrite('predavanje13/siviauto.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()