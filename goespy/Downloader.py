""" That module contents the functions necessary to downloader the ABI-sensors and GLM-L2 Total Lightning
     from the GOES satellite """
from goespy.utils import __isAList
from goespy.utils import ProgressPercentage
from goespy import checkData
from goespy.services.awsService import BucketAcessService
from dateutil.rrule import rrule, HOURLY


def ABI_Downloader(home, bucket, initial_date, final_date, product, channel):
    """ABI_Downloader(home, bucket,year,month,day,hour,product,channel): All these variables are strings.
    The second argument is the Bucket it's the reposity where has the contents from the satellite, example:
    home  = string, set directory to download ABI products
    bucket='noaa-goes16'
    product = can be a List or a single string for ABI sensors products from GOES satellite
              next-generation example: ["ABI-L2-CMIPF"] or "ABI-L1b-RadF"
    channel = Required only for "ABI-L1b-Rad" and "ABI-L2-CMIP" products.
              Can be a List or a single string for the channels from ABI sensors.
              Example = ['01','02'] or "13" (channel is ignored for other ABI products)
    """

    goes16 = BucketAcessService().get_public_bucket(bucket)
    # for loop to all variable year (it's a list var)

    for eachDatetime in rrule(HOURLY, dtstart=initial_date, until=final_date):
        objects = goes16.objects.filter(
            Delimiter="/",
            Prefix=f"{product}/{eachDatetime:%Y}/{eachDatetime:%j}/{eachDatetime:%H}/",
        )
        for eachDownlodableObject in objects:
            filename = eachDownlodableObject.key.rsplit("/", 1)[1]
            # creating the directory where will put the dataset from the bucket
            pathFile = checkData.createPathGoesData(
                home,
                bucket,
                f"{eachDatetime:%Y}",
                f"{eachDatetime:%m}",
                f"{eachDatetime:%d}",
                product,
                f"{eachDatetime:%H}",
            )
            # checking if the data exist and your size!!!
            if checkData.checkFiles(pathFile, filename):
                if checkData.checkSize(pathFile, filename, eachDownlodableObject.size):
                    pass
                else:
                    # Downloading the file with the boto3
                    goes16.download_file(
                        eachDownlodableObject.key,
                        pathFile + filename,
                        Callback=ProgressPercentage(
                            filename, eachDownlodableObject.size
                        ),
                    )
            else:
                # Downloading the file with the boto3
                goes16.download_file(
                    eachDownlodableObject.key,
                    pathFile + filename,
                    Callback=ProgressPercentage(filename, eachDownlodableObject.size),
                )


def GLM_Downloader(home, bucket, year, month, day, hour):
    """GLM_Downloader(home, bucket,year,month,day,hour): All these variables are strings.
    The first argument is the Bucket it's the reposity where has the contents from the satellite, example:
    home  = string, set directory to download GLM products
    bucket='noaa-goes16'
    year  = type List for Year date: example = ['2017','2018']
    month = type List for month date: example = ['03','04']
    day   = type List for day date: example = ['10','20','30']
    hour   = type List for hour need be UTC coordinate time date: example = ['06','12','18']"""

    julianDay = ""
    goes16 = BucketAcessService().get_public_bucket(bucket)
    product = "GLM-L2-LCFA"
    days = 00
    year, month, day, product, hour, julianDay = __isAList(
        year, month, day, product, hour, julianDay=julianDay
    )

    for y in year:
        for mth in month:
            while days <= len(day) - 1 and days <= len(julianDay) - 1:
                for prod in product:
                    print("Downloading... the product %s " % prod)
                    for nindex in hour:
                        print("Downloading... the dataset from {0} UTC".format(nindex))
                        objs = goes16.objects.filter(
                            Delimiter="/",
                            Prefix="{0}/{1}/{2}/{3}/".format(
                                prod, y, julianDay[days], nindex
                            ),
                        )

                        # print("{0}/{1}/{2}/{3}/".format(prod,y,julianDay[days],nindex))
                        for obj in objs:

                            filename = obj.key.rsplit("/", 1)[1]
                            # creating the directory where will put the dataset from the bucket
                            pathFile = checkData.createPathGoesData(
                                home,
                                bucket,
                                y,
                                mth,
                                day[days],
                                prod,
                                nindex,
                            )

                            # checking if the data exist and your size!!!
                            if checkData.checkFiles(pathFile, filename):
                                if checkData.checkSize(pathFile, filename, obj.size):
                                    pass

                                else:

                                    # Downloading the file with the boto3
                                    goes16.download_file(
                                        obj.key,
                                        pathFile + filename,
                                        Callback=ProgressPercentage(filename, obj.size),
                                    )
                            else:

                                # Downloading the file with the boto3
                                goes16.download_file(
                                    obj.key,
                                    pathFile + filename,
                                    Callback=ProgressPercentage(filename, obj.size),
                                )

                days += 1

    return 0
