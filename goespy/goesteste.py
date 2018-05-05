#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from goespy.Downloader import ABI_Downloader 
from goespy.checkData import createPathGoesData
import datetime as dt 
utcDateTime = dt.datetime.utcnow() 

year = utcDateTime.strftime("%Y")

month = utcDateTime.strftime("%m")

day = utcDateTime.strftime("%d")

hour = utcDateTime.strftime("%H")

channel = ["C13"]
hour = '00'
product = 'ABI-L2-CMIPF'

Bucket = 'noaa-goes16'
Abi = ABI_Downloader('noaa-goes16',year,month,day,hour,product,channel)
