import detectFace
import compareFaces

a = detectFace.returnFaceToken("face1.jpg")
if a=="don't have face":
    print(a)
elif a=="检测人脸失败，重新尝试":
    print(a)
else:
    print(a)
    print("是否保存")




b = detectFace.returnFaceToken("face4.jpg")
print(b)

compareFaces.compareFace(a,b)

