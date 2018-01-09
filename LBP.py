from numpy import *
from numpy import linalg as la
import cv2
import os
import math

def minBinary(pixel):
    length = len(pixel)
    zero = ''
    for i in range(length)[::-1]:
        if pixel[i] == '0':
            pixel = pixel[:i]
            zero += '0'
        else:
            return zero + pixel
    if len(pixel) == 0:
        return '0'

        # 加载图像

def loadImageSet(add):
    FaceMat = mat(zeros((11, 100 * 100)))
    j = 0
    for i in os.listdir(add):
        try:
            img = cv2.imread(add + i, 0)
            FaceMat[j, :] = mat(img).flatten()
            j += 1
                # cv2.imwrite(str(i)+'.jpg',img)
        except:
            print('load %s failed' % i)

    return FaceMat


# 算法主过程
def LBP(FaceMat, R=2, P=8):
    pi = math.pi
    LBPoperator = mat(zeros(shape(FaceMat)))
    for i in range(shape(FaceMat)[1]):
        print(i)
        # 对每一个图像进行处理
        face = FaceMat[:, i].reshape(100, 100)
        W, H = shape(face)
        tempface = mat(zeros((W, H)))
        for x in range(R, W - R):
            for y in range(R, H - R):
                repixel = ''
                if face[x,y]:
                    pixel = int(face[x, y])
                else:
                    pixel = 254
                # 　圆形LBP算子
                for p in [2, 1, 0, 7, 6, 5, 4, 3]:
                    p = float(p)
                    xp = x + R * cos(2 * pi * (p / P))
                    yp = y - R * sin(2 * pi * (p / P))
                    xp=int(xp)
                    yp=int(yp)
                    if face[xp, yp] > pixel:
                        repixel += '1'
                    else:
                        repixel += '0'
                        # minBinary保持LBP算子旋转不变
                tempface[x, y] = int(minBinary(repixel), base=2)
        LBPoperator[:, i] = tempface.flatten().T
        # cv2.imwrite(str(i)+'hh.jpg',array(tempface,uint8))
    return LBPoperator

    # judgeImg:未知判断图像
    # LBPoperator:实验图像的LBP算子
    # exHistograms:实验图像的直方图分布
def judgeFace(judgeImg, LBPoperator, exHistograms):
    judgeImg = judgeImg.T
    ImgLBPope = LBP(judgeImg)
    #  把图片分为7*4份 , calHistogram返回的直方图矩阵有28个小矩阵内的直方图
    judgeHistogram = calHistogram(ImgLBPope)
    minIndex = 0
    minVals = inf

    for i in range(shape(LBPoperator)[1]):
        exHistogram = exHistograms[:, i]
        diff = (array(exHistogram - judgeHistogram) ** 2).sum()
        if diff < minVals:
            minIndex = i
            minVals = diff
    return minIndex


# 统计直方图
def calHistogram(ImgLBPope):
    Img = ImgLBPope.reshape(100, 100)
    W, H = shape(Img)
    # 把图片分为7*4份
    Histogram = mat(zeros((256, 7 * 4)))
    maskx, masky = W / 4, H / 7
    for i in range(4):
        for j in range(7):
            # 使用掩膜opencv来获得子矩阵直方图
            mask = zeros(shape(Img), uint8)
            mask[i * maskx: (i + 1) * maskx, j * masky:(j + 1) * masky] = 255
            hist = cv2.calcHist([array(Img, uint8)], [0], mask, [256], [0, 256])
            Histogram[:, (i + 1) * (j + 1) - 1] = mat(hist).flatten().T
    return Histogram.flatten().T

def runLBP():
    # 加载图像
    FaceMat = loadImageSet('C:\\Users\\mcnuggest\\Desktop\\01\\').T
    image = mat("face1.jpg")
    imageLBP = LBP2(image)
    cv2.imshow("111",imageLBP)
    cv2.waitKey(0)

    # LBPoperator = LBP(FaceMat)  # 获得实验图像LBP算子
    # cv2.imshow("111",LBPoperator[0])
    # cv2.waitKey(0)
    # print(type(LBPoperator))
    #
    # # 获得实验图像的直方图分布，这里计算是为了可以多次使用
    # exHistograms = mat(zeros((256 * 4 * 7, shape(LBPoperator)[1])))
    # for i in range(shape(LBPoperator)[1]):
    #     exHistogram = calHistogram(LBPoperator[:, i])
    #     exHistograms[:, i] = exHistogram
    #
    # judgeImg = cv2.imread("face1.jpg")
    # result = judgeFace(mat(judgeImg).flatten(), LBPoperator, exHistograms)
    # print(result)


        # 　下面的代码都是根据我的这个数据库来的，就是为了验证算法准确性，如果大家改了实例，请更改下面的代码
    # nameList = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    # characteristic = ['centerlight', 'glasses', 'happy', 'normal', 'leftlight', 'noglasses', 'rightlight', 'sad',
    #                   'sleepy', 'surprised', 'wink']
    # for c in characteristic:
    #     count = 0
    #     for i in range(len(nameList)):
    #         # 这里的loadname就是我们要识别的未知人脸图，我们通过15张未知人脸找出的对应训练人脸进行对比来求出正确率
    #         loadname = 'D:\python/face recongnition\YALE\YALE\unpadded\subject' + nameList[i] + '.' + c + '.pgm'
    #         judgeImg = cv2.imread(loadname, 0)
    #         if judgeFace(mat(judgeImg).flatten(), LBPoperator, exHistograms) + 1 == int(nameList[i]):
    #             count += 1
    #     print
    #     'accuracy of %s is %f' % (c, float(count) / len(nameList))  # 求出正确率


if __name__ == '__main__':
    # 测试这个算法的运行时间
    runLBP()
    from timeit import Timer

    # t1 = Timer("runLBP()", "from __main__ import runLBP")
    # print
    # t1.timeit(1)