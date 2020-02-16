import cv2

img = cv2.imread('auto.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.imwrite('siviauto.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
