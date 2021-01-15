""" That module contents the functions necessary to downloader the ABI-sensors and GLM-L2 Total Lightning
     from the GOES satellite """


def ABI_Downloader(home, bucket, year, month, day, hour, product, channel):
    """        ABI_Downloader(home, bucket,year,month,day,hour,product,channel): All these variables are strings.
    The second argument is the Bucket it's the reposity where has the contents from the satellite, example:  
    
    home  = string, set directory to download ABI products
    bucket='noaa-goes16'
    year  = can be List or a single string to Year date: example = ['2017','2018'] or "2018
    month = can be List or a single string to month date: example = ['03','04'] or "03"
    day   = can be List or a single string for day date: example = ['10','20','30'] or "20"
    hour   = can be List or a single string to hour, and need be UTC coordinate time date: example = ['06','12','18'] or "06"
    product = can be a List or a single string for ABI sensors products from GOES satellite next-generation example: ["ABI-L2-CMIPF"] or "ABI-L1b-RadF"
    channel = Required only for "ABI-L1b-Rad" and "ABI-L2-CMIP" products. Can be a List or a single string for the channels from ABI sensors. Example = ['01','02'] or "13" (channel is ignored for other ABI products)
    """
    from goespy.utils import __isAList
    from goespy.utils import ProgressPercentage
    from goespy import checkData
    from goespy import boto3
    from goespy import botocore

    julianDay = ''
    days = 0
    s3 = boto3.resource(
        's3',
        config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    goes16 = s3.Bucket(bucket)

    year, month, day, product, hour,channel, julianDay = __isAList(
        year, month, day, product, hour,channel, julianDay=julianDay)

    ## for loop to all variable year (it's a list var)
    for y in year:

        ## same think above
        for mth in month:

            ## I used that while loop, because I think it's a solution more "presentable"
            ## that while will travel on the days list, same to the julianDay
            while days <= len(day) - 1 and days <= len(julianDay) - 1:
                for prod in product:
                    print("Downloading... the product %s " % prod)
                    for nindex in hour:
                        print("Downloading dataset to... {0} UTC".format(nindex))
                        ## all these loops it's necessary to travel all the lenght of the variables
                        ## maybe that's not a elegant solution.
                        ## s3.objects.filters it's a function from boto3 to list all keys on the bucket
                        ## using a prefix
                        objs = goes16.objects.filter(
                            Delimiter='/',
                            Prefix="{0}/{1}/{2}/{3}/".format(
                                prod, y, julianDay[days], nindex))
                        
                        for obj in objs:
                            ## the keys it's a "path"+"filename" in the bucket, solution
                            ### we need only the filename, that's why used the rsplit function.
                            
                            filename = obj.key.rsplit('/', 1)[1]

                            if ( (prod[:-1] == "ABI-L1b-Rad") or (prod[-1] == "ABI-L2-CMIP") ):
                                for ch in channel:
                                    ## when the filename has the same Channel from the user channel variable
                                    ## call the function from download, but before it's done somes check files and directory
                                    if filename.partition(ch)[1] == ch:

                                        # creating the new directory where we will put the dataset from the bucket
                                   
                                        path = checkData.createPathGoesData(home, bucket,
                                            y, mth, day[days], prod, nindex, ch)
                                        
                                        #checking if the file exist on the new directory and your size
                                        if checkData.checkFiles(path, filename):
                                            
                                            if checkData.checkSize(
                                                    path, filename, obj.size):
                                                pass
                                            
                                            else:

                                                # Downloading the file with the boto3
                                                goes16.download_file(
                                                    obj.key, path + filename,Callback=ProgressPercentage(filename,obj.size))
                                        else:
                                        
                                            # Downloading the file with the boto3
                                            goes16.download_file(
                                                obj.key, path + filename,Callback=ProgressPercentage(filename,obj.size))
                            else:
                                # creating the new directory where we will put the dataset from the bucket
                                   
                                path = checkData.createPathGoesData(home, bucket,
                                    y, mth, day[days], prod, nindex)
                                
                                #checking if the file exist on the new directory and your size
                                if checkData.checkFiles(path, filename):
                                    
                                    if checkData.checkSize(
                                            path, filename, obj.size):
                                        pass
                                    
                                    else:

                                        # Downloading the file with the boto3
                                        goes16.download_file(obj.key, path + filename,Callback=ProgressPercentage(filename,obj.size))
                                else:
                                
                                    # Downloading the file with the boto3
                                    goes16.download_file(obj.key, path + filename,Callback=ProgressPercentage(filename,obj.size))
                days += 1

    return 0


def GLM_Downloader(home, bucket, year, month, day, hour):
    """        GLM_Downloader(home, bucket,year,month,day,hour): All these variables are strings.
    The first argument is the Bucket it's the reposity where has the contents from the satellite, example:  

    home  = string, set directory to download GLM products
    bucket='noaa-goes16'
    year  = type List for Year date: example = ['2017','2018'] 
    month = type List for month date: example = ['03','04']
    day   = type List for day date: example = ['10','20','30']
    hour   = type List for hour need be UTC coordinate time date: example = ['06','12','18']"""

    from goespy.utils import __isAList
    from goespy.utils import ProgressPercentage
    from goespy import checkData
    from goespy import boto3
    from goespy import botocore
    julianDay = ''
    s3 = boto3.resource(
        's3',
        config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    goes16 = s3.Bucket(bucket)
    product = 'GLM-L2-LCFA'
    days = 00
    year, month, day, product, hour, julianDay = __isAList(
        year, month, day, product, hour, julianDay=julianDay)

    for y in year:
        for mth in month:
            while days <= len(day) - 1 and days <= len(julianDay) - 1:
                for prod in product:
                    print("Downloading... the product %s " % prod)
                    for nindex in hour:
                        print("Downloading... the dataset from {0} UTC".format(
                            nindex))
                        objs = goes16.objects.filter(
                            Delimiter='/',
                            Prefix="{0}/{1}/{2}/{3}/".format(
                                prod, y, julianDay[days], nindex))

                        #print("{0}/{1}/{2}/{3}/".format(prod,y,julianDay[days],nindex))
                        for obj in objs:

                            filename = obj.key.rsplit('/', 1)[1]
                            ## creating the directory where will put the dataset from the bucket
                            pathFile = checkData.createPathGoesData(
                                home, bucket, y, mth, day[days], prod, nindex)

                            # checking if the data exist and your size!!!
                            if checkData.checkFiles(pathFile, filename):
                                if checkData.checkSize(pathFile, filename,
                                                       obj.size):
                                    pass

                                else:
                                                                        
                                    # Downloading the file with the boto3
                                    goes16.download_file(obj.key,pathFile+filename,Callback=ProgressPercentage(filename,obj.size))
                                    print('\n')
                            else:
                                
                                # Downloading the file with the boto3
                                goes16.download_file(obj.key,pathFile+filename,Callback=ProgressPercentage(filename,obj.size))
                                print('\n')

                days += 1

    return 0
