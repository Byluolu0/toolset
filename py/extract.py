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
		i = 0
		playerId = 0
		playerName = ""
		ranking = 0
		score = 0
		while True:
		    line = file_object.readline()
		    if line:
		    	line.strip()
		    	if line[0] == '{':
		    		i = i + 1
		    	elif line[3] == 'n':
		    		ranking = line[19:]
		    	elif line[1] == 'p' and line[7] == 'I':
		    		playerId = line[20:]
		    	elif line[1] == 'p' and line[7] == 'N':
		    		playerName = line[13:]
		    	elif line[1] == 's':
		    		score = line[17:]
		    	elif line[0] == '}':
		    		outputFile.write(ranking + "," + playerId + "," + playerName + "," + score + "\n")
		    else:
		        break
	finally:
		file_object.close()
		outputFile.close()

def transInDir(dirName, outDir):
	for parent, dirnames, filenames in os.walk(dirName):    
		for fileName in filenames:                      
			utf82gbk(parent, fileName, outDir)


transInDir(sys.argv[1], sys.argv[2])