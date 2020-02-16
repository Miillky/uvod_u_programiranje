import cv2
import numpy as np
import pytesseract

screenCnt = None
gray = cv2.imread('auto-reg.jpeg', cv2.IMREAD_GRAYSCALE)
gray = cv2.resize(gray, (620, 480))
ret, threshold = cv2.treshold(gray, 180, 255, cv2.THRESH_BINARY)
cnts, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# loop over our contours
for c in cnsts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)
    # kandidati su konture s 4 točke
    if len(approx) == 4:
        x1, x2, x3, x4 = approx[0][0][0], approx[1][0][0], approx[2][0][0], approx[3][0][0]
        y1, y2, y3, y4 = approx[0][0][1], approx[1][0][1], approx[2][0][1], approx[3][0][1],
        if x3 - x2 > 45:
            screenCnt = approx
            break

# Masking the part other than the number plate
mask = np.zeros(gray.shape, np.uint8)
newImage = cv2.drawContours(mask, [screenCnt], 0, 255, -1)
newImage = cv2.bitwise_and(gray, gray, mask=mask)

# Izreži detektirani oblik
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
Cropped = cv2.bilateralFilter(Cropped, 55, 17, 17)

# Rotacija izrezane tablice
(h, w) = Cropped.shape[:2]
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 4, 1.0)
Cropped = cv2.warpAffine(Cropped, M (w, h))

#pytesseract.pytesseract.tesseract_cmd = r'./filePath'
text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("Detected Number is: ", text)