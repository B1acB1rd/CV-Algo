import cv2
import numpy as np

img = cv2.imread(r"C:\Users\HP\Downloads\ChatGPT Image Aug 15, 2025, 06_23_02 PM.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)


Ix2 = grad_x * grad_x
Iy2 = grad_y * grad_y
IxIy = grad_x * grad_y


Ix2_blurred = cv2.GaussianBlur(Ix2, (5, 5), 0)
Iy2_blurred = cv2.GaussianBlur(Iy2, (5, 5), 0)
IxIy_blurred = cv2.GaussianBlur(IxIy, (5, 5), 0)


k = 0.04
det = (Ix2_blurred * Iy2_blurred) - (IxIy_blurred * IxIy_blurred)
trace = Ix2_blurred + Iy2_blurred
harris_response = det - k * (trace ** 2)


threshold = 0.01 * harris_response.max()
result = (harris_response > threshold) * 255


cv2.imshow('Final Corners', result.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()