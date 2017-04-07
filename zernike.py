__author__ = 'Sudheer'
import numpy as np
import cv2
import database
import mahotas
import result_values_file

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape)/2)
  rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape,flags=cv2.INTER_LINEAR)
  return result


def load_image(source,angle):
 photo = cv2.imread(source)
 photo = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
 photo = photo.astype(np.uint8)
 photo = cv2.copyMakeBorder(photo,15,15,15,15,cv2.BORDER_CONSTANT,value=255)
 photo = rotateImage(photo,angle)
 return photo


def threshold_image(photo):
    thresh = cv2.bitwise_not(photo)
    thresh[thresh > 0] = 255
    return thresh
    #cv2.imshow("Threshold",photo), cv2.waitKey(1000)

def draw_contours(photo,thresh):
 outline = np.zeros(photo.shape,dtype = "uint8")
 derp,cnts,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
 cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
 cv2.drawContours(outline, [cnts], -1, 255, -1)
 #cv2.imshow("outline",outline), cv2.waitKey(10000)
 return outline

class ZernikeMoments:
    def __init__(self, radius):
        self.radius = radius

    def describe(self,image):
        return mahotas.features.zernike_moments(image, self.radius)

def save_outlines_in_results_file(angle,outline):
    if angle == 30:
      result_values_file.image_1 = outline
    elif angle == 45:
      result_values_file.image_2 = outline
    elif angle == 60:
      result_values_file.image_3 = outline
    elif angle == 90:
      result_values_file.image_4 = outline
    elif angle == 180:
      result_values_file.image_5 = outline
    elif angle == 360:
      result_values_file.image_6 = outline
    else:
      pass

def calculate_zernike_moments(source,angle):
 photo = load_image(source,angle)
 thresholded_photo = threshold_image(photo)
 outline = draw_contours(photo,thresholded_photo)
 save_outlines_in_results_file(angle,outline)
 image_instance = ZernikeMoments(21)
 moments = image_instance.describe(outline)
 zernike_moments = []
 for x in moments:
     zernike_moments.append(x)
     #print x
 return zernike_moments

def identify_the_object(zernike_moments,mean):
 try:

    result_values_file.result = database.find_object_via_zernike_moments(zernike_moments)

 except Exception as e:
    object_name = raw_input("Enter the Objects name:\n")
    try:
        database.insert_zernike_moments_into_database(zernike_moments,mean,object_name)
        print "entered"
    except:
        print "Unexpected Error"

def controller_function(source,angle):
    zernike_moments = calculate_zernike_moments(source,angle)
    mean = sum(zernike_moments)
    if angle == 0:
        identify_the_object(zernike_moments,mean)
    return mean


