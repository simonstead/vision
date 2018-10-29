#from pyimagesearch.shapedetector import ShapeDetector
import cv2
import imutils
import unittest


class VisionTests(unittest.TestCase):
    def test_vision(self):
        filename = 'img.jpg'
        image = cv2.imread(filename)
        resized = imutils.resize(image, width=300)
        ratio = image.shape[0] / float(resized.shape[0])

        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        
        print(len(cnts))

        print(cnts[0])
        self.fail('test')

