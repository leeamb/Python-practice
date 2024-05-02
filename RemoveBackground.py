from rembg import remove
import cv2

input_path ="/Users/leena/Desktop/Flower.JPG"
output_path = "/Users/leena/Desktop/Flower2.JPG"

input_file = cv2.imread(input_path)
output_file = remove(input_file)
cv2.imwrite(output_path, output_file)
