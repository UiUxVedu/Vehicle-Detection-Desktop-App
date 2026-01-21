import cv2
import numpy as np

def segment_characters(plate_img):
    chars = []

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        plate_img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # clean noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Filter by size
        if h > 40 and w > 10 and h < 75:
            char = thresh[y:y+h, x:x+w]
            chars.append((x, char))

    # Sort left -> right
    chars = sorted(chars, key=lambda x: x[0])

    # Return only images
    return [c[1] for c in chars]
