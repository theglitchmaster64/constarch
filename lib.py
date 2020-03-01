import cv2
import numpy
import PIL
from matplotlib import pyplot


class colImg():

    def __init__(self,inputFilename):
        self.img = cv2.imread(inputFilename)

    def info(self):
        print('shape:{0}\ndepth:{1}'.format(self.img.shape,self.img.dtype))

    def conStretch(self,low,high):
        for i in range(0,3):
            local_min = numpy.percentile(self.img[:,:,i],low)
            local_max = numpy.percentile(self.img[:,:,i],high)
            gmax = 255
            gmin = 0
            print('running for channel {0}\n\t{1}th percentile:{2}\n\t{3}th percentile:{4}'.format(i,low,local_min,high,local_max))
            self.img[:,:,i] = (self.img[:,:,i] - local_min)*((gmax-gmin)/(local_max-local_min)) + gmin


    def genHists(self):
        histlist = []
        for i in range(0,3):
            histlist.append(cv2.calcHist([self.img],[i],None,[256],[0,256]))
            for i in range(0,len(histlist)):
                pyplot.plot(histlist[i])
                pyplot.savefig('./histogram_channel{}'.format(i))
                pyplot.clf()


    def write(self,outputFilename):
        cv2.imwrite(outputFilename,self.img)

    def con2gray(self):
        pass


class greyImg():

    def __init__(self,inputFilename):
        temp = cv2.imread(inputFilename)
        self.img = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)

    def info(self):
        print('shape:{0}\ndepth:{1}'.format(self.img.shape,self.img.dtype))

    def conStretch(self,low,high):
        local_min = numpy.percentile(self.img[:,:],low)
        local_max = numpy.percentile(self.img[:,:],high)
        gmin=0
        gmax=255
        print('running for channel 0\n\t{0}th percentile:{1}\n\t{2}th percentile:{3}'.format(low,local_min,high,local_max))
        self.img[:,:] = (self.img[:,:] - local_min)*((gmax-gmin)/(local_max-local_min)) + gmin

    def genHists(self):
        histogram = cv2.calcHist([self.img],[0],None,[256],[0,256])
        pyplot.plot(histogram)
        pyplot.savefig('./histogram_grayscale')
        pyplot.clf()

    def write(self,outputFilename):
        cv2.imwrite(outputFilename,self.img)

    def colorize(self):
        self.img = cv2.cvtColor(self.img,cv2.COLOR_GRAY2BGR)
