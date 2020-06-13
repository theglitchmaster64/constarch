#!/usr/bin/python3

import cv2
import numpy
import PIL
from matplotlib import pyplot
import argparse
from lib import *
import sys

parser = argparse.ArgumentParser(description='image manipulation module 3')
parser.add_argument('input',help='input file name')
#parser.add_argument('output',help='output file name')
parser.add_argument('--color',dest='color',action='store_true')
parser.add_argument('--grey',dest='grey',action='store_true')
parser.add_argument('--lum',dest='lum',action='store_true')
parser.add_argument('--split',dest='split',action='store_true')
parser.add_argument('--histogram',dest='hist',action='store_true')
parser.add_argument('n1',type=float)
parser.add_argument('n2',type=float)
args = parser.parse_args()

inputFile = args.input
outputFile = str(inputFile.split('.')[0]+'_output')
n1 = args.n1
n2 = args.n2


if __name__ == '__main__':

	if args.color:
		col = colImg(inputFile)
		col.info()
		if args.hist:
			col.genHists(inputFile.split('.')[0]+'_rgb_before_histogram')
		col.conStretch(n1,n2)
		if args.hist:
			col.genHists(inputFile.split('.')[0]+'_rgb_after_histogram')
		col.write(outputFile+'_color.png')
		sys.exit(0)

	elif args.grey:
		gry = greyImg(inputFile)
		gry.info()
		if args.hist:
			gry.genHists(inputFile.split('.')[0]+'_grey_before_histogram')
		gry.conStretch(n1,n2)
		if args.hist:
			gry.genHists(inputFile.split('.')[0]+'_grey_after_histogram')
		gry.write(outputFile+'_grey.png')
		sys.exit(0)

	elif args.lum:
		lum = lumImg(inputFile)
		lum.info()
		if args.hist:
			lum.genHists(inputFile.split('.')[0]+'_before_Y_stretch')
		lum.conStretchY(n1,n2)
		if args.hist:
			lum.genHists(inputFile.split('.')[0]+'_after_Y_stretch')
		lum.write(outputFile+'_ycrcb.png')
		sys.exit(0)

	elif args.split:
		print('feature not supported')
		sys.exit(0)
