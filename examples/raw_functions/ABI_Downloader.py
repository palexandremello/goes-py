"""        ABI_Downloader(bucket,year,month,day,hour,product,channel): All these variables are strings.
    The first argument is the Bucket it's the reposity where has the contents from the satellite, example:

    Bucket='noaa-goes16'
    year  = can be List or a single string to Year date: example = ['2017','2018'] or "2018
    month = can be List or a single string to month date: example = ['03','04'] or "03"
    day   = can be List or a single string for day date: example = ['10','20','30'] or "20"
    hour   = can be List or a single string to hour, and need be UTC coordinate time date: example = ['06','12','18'] or "06"
    product = can be a List or a single string for ABI sensors products from GOES satellite next-generation example: ["ABI-L2-CMIPF"] or "ABI-L1b-RadF"
    channel = can be a List or a single string for the channels from ABI sensors. Example = ['01','02'] or "13"
        """


def ABI_Downloader(bucket, year, month, day, hour, product, channel):
    from goesdownloader.utils import __isAList
    from goesdownloader.utils import daytoJulian
    from goesdownloader import checkData
    from goesdownloader import boto3
    from goesdownloader import botocore

    julianDay = daytoJulian(year, month, day)

    days = 0
    s3 = boto3.resource(
        's3',
        config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    goes16 = s3.Bucket(bucket)

    year, month, day, product, hour, julianDay = __isAList(
        bucket, year, month, day, product, hour, julianDay=julianDay)
    for i in year:
        for mth in month:
            while days <= len(day) - 1 and days <= len(julianDay) - 1:
                for prod in product:
                    for nindex in hour:
                        print("Baixando dado para {0} UTC".format(nindex))
                        objs = goes16.objects.filter(
                            Delimiter='/',
                            Prefix="{0}/{1}/{2}/{3}/".format(
                                prod, i, julianDay[days], nindex))
                        for object in objs:
                            filename = object.key.rsplit('/', 1)[1]
                            for ch in channel:
                                if filename.partition(ch)[1] == ch:

                                    path = checkData.createPathGoesData(
                                        i, mth, day[days], prod, nindex, ch)
                                    if checkData.checkFiles(path, filename):
                                        if checkData.checkSize(
                                                path, filename, object.size):
                                            pass
                                        else:
                                            print(
                                                "Dado: {0}\n".format(filename))
                                            print(
                                                "Tamanho: {0} Bytes \n".format(
                                                    object.size))
                                            goes16.download_file(
                                                object.key, path + filename)
                                    else:
                                        print("Dado: {0}\n".format(filename))
                                        print("Tamanho: {0} Bytes \n".format(
                                            object.size))
                                        goes16.download_file(
                                            object.key, path + filename)
                days += 1

    return 0
