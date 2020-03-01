#!/usr/bin/python3

import cv2
import numpy
import PIL
from matplotlib import pyplot
import argparse
from lib import *

parser = argparse.ArgumentParser(description='image manipulation module 3')
parser.add_argument('input',help='input file name')
parser.add_argument('output',help='output file name')
parser.add_argument('--color',dest='color',action='store_true')
parser.add_argument('--histogram',dest='hist',action='store_true')
parser.add_argument('n1',type=float)
parser.add_argument('n2',type=float)
args = parser.parse_args()

inputFile = args.input
outputFile = args.output
n1 = args.n1
n2 = args.n2


if __name__ == '__main__':
	if args.color:
		col = colImg(inputFile)
		col.info()
		if args.hist:
			col.genHists()
		col.conStretch(n1,n2)
		col.write(outputFile)
	else:
		gry = greyImg(inputFile)
		gry.info()
		if args.hist:
			gry.genHists()
		gry.conStretch(n1,n2)
		gry.write(outputFile)
