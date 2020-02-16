import cv2

img = cv2.imread('oblaci.jpg')

cv2.line(img, (100, 400), (400, 300), (255,255,255), 10)
cv2.rectangle(img, (400, 300), (100, 400), (0, 0, 255), 15)
cv2.circle(img, (120, 380), 10, (0,255,0), 4)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'Oblaci!', (400, 300), font, 2, (200, 255, 155), 5, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()