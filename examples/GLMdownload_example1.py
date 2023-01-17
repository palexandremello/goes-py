""" This example we will aproach about get the dataset from GLM-L2-LCFA total lightning (intra to cloud and ground to cloud) with the goespy """
""" First you need import the library necessary to Download goespy for the GLM-LCFA"""
from goespy.Downloader import GLM_Downloader ## goespy.Downloader it's where the main function
                                                     ## to download the products by GOES in the AWS
                                                     ## in the goespy.Downloader we have
                                                     # ABI_Downloader = ABI-Sensors
                                                     # GLM_Downloader = Total Lightning product
                                                     # So if you need the ABI_Downloader, just change
                                                     # the GLM_Downloader to ABI_Downloader or import both
                                                     # example: from goespy.Downloader import ABI_Downloader
### to use GLM_Downloader, you need 7 arguments:
### to see more information about GLM_Downloader, use help(GLM_Downloader)


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

## The Bucket is the variable contains the name of dataset server from goes on AWS
Bucket = 'noaa-goes16' ## in the future on AWS they will have goes17.
## Now we will call the function GLM_Downloader:

Abi = GLM_Downloader('noaa-goes16',year,month,day,hour)

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
                                    |-----> Product(GLM_LCFA)
                                                |
                                                |
                                                |------> UTC hour
                                                            |
                                                            |
                                                            |-------> 240 .nc files per hour'''
