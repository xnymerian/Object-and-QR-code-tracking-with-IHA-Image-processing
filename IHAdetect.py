import cv2
import numpy as np

def iha_tespiti(frame):
    # HSV renk uzayına dönüşüm
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #u İha rengi için bir maske oluştur
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Morfolojik operasyonlar
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Konturları bulTR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Konturları çiz
    for contour in contours:
    contours, _ = cv2.findContours(mask.copy(), cv2.RE
        if cv2.contourArea(contour) > 1000:
            (x, y, w, h) = cv2.bondingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

# Video akışı başlat
cap = cv2.VideoCapture(0)

while True:
    # Frame okuma
    ret, frame = cap.read()

    # İha tespiti
    result_frame = iha_tespiti(frame)

    # Sonuçları göster
    cv2.imshow('Iha Tespiti', result_frame)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video akışını kapat
cap.release()
cv2.destroyAllWindows()
