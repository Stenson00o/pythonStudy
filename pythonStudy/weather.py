#!/usr/bin/env python
# coding=utf-8



import urllib2
import city
import json
'''
from the url:
http://www.weather.com.cn/data/cityinfo/101010100.html
get the json,example:
"weatherinfo":{"city":"鍖椾含","cityid":"101010100","temp1":"-2鈩�","temp2":"16鈩�","weather":"鏅�","img1":"n0.gif","img2":"d0.gif","ptime":"18:00"}}
so first, make a  request  from the ulr ,
next to get the data ,then encoding and decoding
'''

class Weather():
    ##init the variable in this
    def __init__(self, city , citycode):
        self.city = city
        self.citycode = citycode
        #self.defualtcode = "101010100"
        self.cityurl = "http://www.weather.com.cn/data/cityinfo/%s.html" %self.citycode

    def getDataByURL(self, url):
        try:
            # get one  response from web
            response = urllib2.urlopen(url)
            #the data in web encoding 'gbk'
            data = response.read()
            return data
        except Exception ,e :
            print e
        
    def parseWeatherData(self, data):
        if not data:
            return 

        weather_data  = json.loads(data)
        result = weather_data['weatherinfo']
        str_temp = ('%s\n%s~~~~%s')%(
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        
        print self.city + "\n", str_temp

def start():
    #load city data
    city_dict = city.city().getCity_Dictionary()

    while True:
        #input cityname for query
        cityname  = raw_input("Enter city name, Enter 'Q' quit")
        
            #    print input, city_dict[input]
        if cityname in city_dict.keys():
            citycode = city_dict[cityname]
            w = Weather(cityname, citycode)
            data = w.getDataByURL(w.cityurl)
            w.parseWeatherData(data)
        elif cityname  == 'Q':
            exit(1)
        else:
            print u'you input not china city'
            continue

def main():
    start()
   # w = Weather(u"北京", "101010100")
   # data = w.getDataByURL(w.cityurl)
   # w.parseWeatherData(data)

if __name__ == "__main__":
    main()
