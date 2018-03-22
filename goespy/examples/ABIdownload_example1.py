""" This example we will aproach about get the dataset from ABI-Sensors with the goespy """
""" First you need import the library necessary to Download goespy for the ABI-Sensors"""
from goespy.Downloader import ABI_Downloader ## goespy.Downloader it's where the main function
                                                     ## to download the products by GOES in the AWS
                                                     ## in the goespy.Downloader we have
                                                     # ABI_Downloader = ABI-Sensors 
                                                     # GLM_Downloader = Discharge eletric product
                                                     # So if you need the GLM_Downloader, just change
                                                     # the ABI_Downloader to GLM_Downloader or import both 
                                                     # example: from goespy.Downloader import GLM_Downloader
### to use ABI_Downloader, you need 7 arguments:
### to see more information about ABI_Downloder, use help(ABI_Downloader) 


## If you want to get the dataset at real-time from the GOES in the AWS, just use this library
import datetime as dt ## More information about the datetime library acesse this link:
                      ## Link aqui


### Getting the current date (in UTC coordinate)
## All these variables need be string
utcDateTime = dt.datetime.utcnow() 
## current year
year = utcDateTime.strftime("%Y")
# current month
month = utcDateTime.strftime("%m")
## current day
day = utcDateTime.strftime("%d")
## current hour in UTC 
hour = utcDateTime.strftime("%H")
##Choose a channel from your preference (can be C01-C16)
channel = ["C13"]

## In GOES satellite they have 9 products
## 3 are L1b-Rad(M,C,F)
## 3 are L2-CMIP(M,C,F)
## 3 are L2-MCMIP(M,C,F)
### In your case we will get the CMIPF, F means FullDisk (all the projection by the satellite)
product = 'ABI-L2-CMIPF'

## The Bucket is the variable contains the name of dataset server from goes on AWS
Bucket = 'noaa-goes16' ## in the future on AWS they will have goes17.
## Now we will call the function ABI_Downloader:

Abi = ABI_Downloader('noaa-goes16',year,month,day,hour,product,channel)

##After all the dataset is downloaded, they are in your home directory with that structure:
'''goes16
    |
    |
    |---------> Year
                 |
                 |
                 |----> Month
                          |
                          |
                          |------> Day
                                    |
                                    |
                                    |-----> Product(ABI-*)
                                                |
                                                |
                                                |------> UTC hour
                                                            |
                                                            |------> Channel (C01-C16)
                                                                           |
                                                                           |-------> 4 files in .nc'''
