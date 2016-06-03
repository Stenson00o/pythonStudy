#!/usr/bin/env python
# coding=utf-8

import cookielib
import urllib2
import urllib
import sys
#

def getSchoolData():
    #ji ben url
    loginurl = " http://211.83.241.251/StuExpbook/student/login.jsp"
    #store cookie file
    filename = 'cookie.txt'
    Submit = '%E7%99%BB%E5%BD%95'
    #sheng ming yige duixiang baocun cookielib
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({
        'no':'201131003040',
        'password':'201131003040',
        'Submit':Submit
    })

    result = opener.open(loginurl, postdata)
    print result.info()
    print result.getcode()
    print result.read()
    cookie.save(ignore_discard = True, ignore_expires = True)

#getSchoolData()

def accessByCookie():
    filename = 'cookie.txt'
    loginurl = " http://211.83.241.251/StuExpbook/student/login.jsp"
    
    cookie = cookielib.MozillaCookieJar()
    cookie.load(filename, ignore_discard = True, ignore_expires = True)

    request = urllib2.Request(loginurl)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    respone = opener.open(request)

    print respone.info()
    print respone.getcode()
    print respone.read()

#iaccessByCookie()

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print "Usage: --get  or ---access-by-cookie"

    elif '--get' == args[0]:
        getSchoolData()

    elif '--access-by-cookie' == args[0]:
        accessByCookie()

    else:
        print "Usage: --get  or ---access-by-cookie"
        

