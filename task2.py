import cv2

cap = cv2.VideoCapture(0)
downpoints = (600, 600)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, downpoints, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        boundary =  max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(boundary)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: #27 = ESC
       break

cap.release()
cv2.destroyAllWindows()