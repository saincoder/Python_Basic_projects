import pywhatkit as kit
import cv2
handwritten = input("Enter your text to convert in handwriting: ")
kit.text_to_handwriting(handwritten, save_to='shahid.png')
img = cv2.imread('shahid.jpg')
cv2.imshow('shahid.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
