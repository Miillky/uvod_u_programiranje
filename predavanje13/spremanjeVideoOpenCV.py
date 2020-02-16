import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (True):
    ret, frame = cap.read()

    if ret:
        out.write(frame)
        cv2.imshow('prozor', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
