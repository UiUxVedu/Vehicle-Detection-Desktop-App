import pytesseract
import cv2

def recognize_plate(chars):
    plate_text = ""

    for char in chars:
        char = cv2.resize(char, (28, 28))
        char = cv2.bitwise_not(char)

        text = pytesseract.image_to_string(
            char,
            config='--psm 10 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        )

        plate_text += text.strip()

    return plate_text
