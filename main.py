import detectFace
import compareFaces
import cv2
#import gui

def LBP(FaceMat, R=2, P=8):
    cv2.imshow("Image", FaceMat)
    im_gray = cv2.cvtColor(FaceMat, cv2.COLOR_BGR2GRAY)




img = cv2.imread("face1.jpg")

LBP(img)






# a = detectFace.returnFaceToken("face1.jpg")
# if a=="don't have face":
#     print(a)
# elif a=="检测人脸失败，重新尝试":
#     print(a)
# else:
#     print(a)
#     print("是否保存")
#
# b = detectFace.returnFaceToken("face4.jpg")
# print(b)
#
# compareFaces.compareFace(a,b)

