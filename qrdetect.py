import cv2
import numpy as np

# Sembol tanımlama
symbols = [cv2.QR_CODE, cv2.FRAME_HEIGHT]

# Video nesnesi oluşturma
cap = cv2.VideoCapture(0)

# Tanımlama
def detect_and_draw(frame, symbols):
    for symbol in symbols:
        # QR kodu veya kare tanıma
        data, corners, _ = cv2.QRCodeDetector().detectAndDecode(frame)

        # QR kodu tanındıysa
        if data:
            cv2.putText(frame, data, (corners[0][0], corners[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.putText(frame, "QR Code: {}".format(data), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Eşzamanlı bir kare tanıma için
        if symbol == cv2.FRAME_HEIGHT:
            frame_height = frame.shape[0]
            # Yatay ve dikey çizgiler
            line_thickness = int(frame_height / 160)
            cv2.line(frame, (0, frame_height // 2), (frame.shape[1], frame_height // 2), (0, 0, 255), thickness=line_thickness)
            cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 0, 255), thickness=line_thickness)
            break

    return frame

while True:
    ret, frame = cap.read()

    # Sadece eğer tanımlanabilir ise çerçeve tanıma
    if symbols[0] != cv2.QR_CODE:
        detect_and_draw(frame, symbols)

    # Görüntüyü göster
    cv2.imshow('Frame', frame)

    # Q tuşuna basıldığında çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
