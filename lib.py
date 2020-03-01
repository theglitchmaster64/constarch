import cv2
import numpy
import PIL
from matplotlib import pyplot
import argparse


class colImg():

    def __init__(self,inputFilename):
        self.img = cv2.imread(inputFilename)


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
            for i in range(0,3):
                pyplot.plot(histlist[i])
                pyplot.savefig('./hist_channel{}'.format(i))


    def write(self,outputFilename):
        cv2.imwrite(outputFilename,self.img)


class greyImg():

    def __init__(self,inputFilename):
        self.img = cv2.imread(inputFilename)

    def conStretch(self,low,high):
        local_min = numpy.percentile(self.img[:,:,0],low)
        local_max = numpy.percentile(self.img[:,:,0],high)
        gmin=0
        gmax=255
        print('running for channel 0\n\t{0}th percentile:{1}\n\t{2}th percentile:{3}'.format(low,local_min,high,local_max))
        self.img[:,:,0] = (self.img[:,:,0] - local_min)*((gmax-gmin)/(local_max-local_min)) + gmin

    def genHists(self):
        histogram = cv2.calcHist([self.img],[0],None,[256],[0,256])
        pyplot.plot(histogram)
        pyplot.savefig('./hist_channelU')

    def write(self,outputFilename):
        cv2.imwrite(outputFilename,self.img)
