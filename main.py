import detectFace
import compareFaces

a = detectFace.returnFaceToken("face1.jpg")
print(a)

b = detectFace.returnFaceToken("face1.jpg")
print(b)

compareFaces.compareFace(a,b)

