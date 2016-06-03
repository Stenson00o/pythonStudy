#/usr/bin/env python
# -*- coding: UTF-8 -*- 

import re
import urllib2


class city():
	#init variable
	def __init__(self):
		self.file_path = '~/python/'
		self.file_name = 'city.txt'
		self.re_pattern = '(.*)\n(.*)\n(.*)\n\n'
	
	def loadCityFile(self, filename):
		try:
			f = open(filename)
			#get the city info  
			data = f.read()	
			return data
			#while the file not exists, deal with excption
		except Exception as e:
			print e.reason
			exit(1)
		finally:
			#must close the file
			if f:
				f.close()

	def parseData(self, data):
		#use the re get the data
		#example
		#--yun nan province
		#--kun ming,bao ji,.....
		#--seq1,seq2,......
		pattern = re.compile(self.re_pattern)
		#match the data, get the data list
		matchs = re.findall(pattern, data)
		#key == cityname, value == citycode
		city_dict = {}
		for match in matchs:
			s1 = match[1].replace("\"", "").split(",")
			s2 = match[2].replace("\"", "").split(",")
			for i in xrange(len(s1)):
				city_dict[s1[i]] = s2[i]	
		return city_dict			
		
        def getCity_Dictionary(self):
            data = self.loadCityFile('city2.txt')
            citys = self.parseData(data)
            return citys

def main():
    pass
#	w = Weather()
#	data = w.loadLocalData('city2.txt')
#	citys = w.parseData(data)
#for key in citys:
#		print key,citys[key]

if __name__ == "__main__":
	print 'hello'
	main()
    
