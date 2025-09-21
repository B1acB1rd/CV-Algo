#Reads an image.
#Converts it to grayscale.
#Converts it into black & white (binary).
#Finds contours (shapes) in the image.
#Filters out small contours (noise).
#For each big contour:
#Calculates perimeter.
#Approximates the shape (polygon).
#Finds the convex hull (tight wrapper around shape).
#Draws both the polygon (green) and the hull (red) on the copy of the image.
#Displays the result.
import cv2
import numpy as np

img_path = r"C:\Users\HP\Downloads\PolyconvexTrainImage.png"
img = cv2.imread(img_path)
output_img = img.copy()
if img is None:
    print("Error: Could not read image. Please check the file path.")
else:
    pass
img =- cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)#this needs a grayscale image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 1000:
        perimeter = cv2.arcLength(cnt, True)

        epsilon = 0.001 * perimeter
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        hull = cv2.convexHull(cnt)
        cv2.drawContours(output_img, [approx], -1, (0, 255, 0), 3)
        cv2.drawContours(output_img, [hull], -1, (0, 0, 255), 3)

cv2.imshow("Image comaprison", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
