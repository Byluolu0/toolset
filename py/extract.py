#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import sys
import os
import os.path
import json


def utf82gbk(dir, fileName, outDir):
	print(dir, fileName, outDir)
	realOutDir = outDir + "\\" + dir
	if not os.path.exists(realOutDir):  
		os.makedirs(realOutDir)
	fullName = os.path.join(dir, fileName)
	outputName = realOutDir + "\\" + fileName
	file_object = open(fullName, encoding='UTF-8')
	outputFile = open(outputName, mode='w', encoding='GBK')
	head = "排名,玩家Id,区服Id,玩家名字,情侣Id,情侣区服Id,情侣名字,分数\n" 
	outputFile.write(head)
	try:
		i = 0
		playerId = ""
		playerName = ""
		ranking = ""
		score = ""
		temp = ""
		while True:
			line = file_object.readline()
			if line:
				line = line.strip().strip('\n').strip('\r')
				line = line.replace("ObjectId", "")
				line = line.replace("NumberInt", "")
				line = line.replace("(", "")
				line = line.replace(")", "")
				temp += line
				if line[0] == '}':
					i += 1
					if i % 2 == 0:
						obj = json.loads(temp)
						#print(obj)
						temp = ""
						output_line = "%d,%d,0,%s,%d,0,%s,%d\n" % (obj["ranking"], obj["role_id"], obj["extra"]["playerName"], obj["extra"]["fereId"], obj["extra"]["fereName"], obj["score"])
						outputFile.write(output_line)
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