import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while(True):
    ret, frame = cap.read()

    if ret:
        sivo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        boja = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('Prozor1', frame)
        cv2.imshow('Prozor2', boja)
        cv2.imshow('Prozor3', sivo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
