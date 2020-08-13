import cv2
import qr_code_decoder
capture = cv2.VideoCapture(1, cv2.CAP_DSHOW) ## remove the cv2.CAP_DSHOW if any errors occour
while True:
    _, frame = capture.read()

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    try:
        print(qr_code_decoder.decode_qr_codes(frame))
        break
    except IndexError:
        continue
capture.release()    
cv2.destroyAllWindows()
