#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import sys
import os
import os.path

def utf82gbk(dir, fileName, outDir):
	print(dir, fileName, outDir)
	realOutDir = outDir + "\\" + dir
	if not os.path.exists(realOutDir):  
		os.makedirs(realOutDir)
	fullName = os.path.join(dir, fileName)
	outputName = realOutDir + "\\" + fileName
	file_object = open(fullName, encoding='UTF-8')
	outputFile = open(outputName, mode='w', encoding='GBK')
	try:
		all_the_text = file_object.read()
		outputFile.write(all_the_text)
	finally:
		file_object.close()
		outputFile.close()

def transInDir(dirName, outDir):
	for parent, dirnames, filenames in os.walk(dirName):    
		for fileName in filenames:                      
			utf82gbk(parent, fileName, outDir)

transInDir(sys.argv[1], sys.argv[2])