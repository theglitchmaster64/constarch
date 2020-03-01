#!/usr/bin/python3

import cv2
import numpy
import PIL
from matplotlib import pyplot
import argparse
import lib

parser = argparse.ArgumentParser(description='image manipulation module 3')
parser.add_argument('input',help='input file name')
parser.add_argument('output',help='output file name')
args = parser.parse_args()

inputFile = args.input
outputFile = args.output

#img = cv2.imread(inputFile)
#greyimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print('shape:\t{0}\nbit-depth:{1}'.format(greyimg.shape,greyimg.dtype))




if __name__ == '__main__':
	col = lib.greyImg(inputFile)
	col.conStretch(0.1,99.9)
	col.write(outputFile)
