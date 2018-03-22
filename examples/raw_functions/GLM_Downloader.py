 
def GLM_Downloader(bucket,year,month,day,hour):

    """        GLM_Downloader(bucket,year,month,day,hour): All these variables are strings.
    The first argument is the Bucket it's the reposity where has the contents from the satellite, example:  

    Bucket='noaa-goes16'
    year  = type List for Year date: example = ['2017','2018'] 
    month = type List for month date: example = ['03','04']
    day   = type List for day date: example = ['10','20','30']
    hour   = type List for hour need be UTC coordinate time date: example = ['06','12','18']"""
    
    from createPathGoesData import createPathGoesData
    from __isAList import __isAList
    from checkFiles import checkFiles
    from checkSize import checkSize
    import boto3
    import botocore
    import datetime

                
    julianDay = str(datetime.datetime.strptime('{0}-{1}-{2}'.format(year,month,day), 
    '%Y-%m-%d').timetuple().tm_yday).zfill(3)
    s3 = boto3.resource('s3', 
    config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    goes16 = s3.Bucket(bucket)
    product = 'GLM-L2-LCFA'
    days=00
    year,month,day,product,hour,julianDay = __isAList(year,month,day,product,hour,julianDay=julianDay)
    
    for i in year:
        for mth in month:
            while days <= len(day)-1 and days <= len(julianDay)-1:
                for prod in product:
                    for nindex in hour:
                        print("Baixando dado para {0} UTC".format(nindex))
                        objs = goes16.objects.filter(Delimiter='/',
                        Prefix="{0}/{1}/{2}/{3}/".format(prod,i,julianDay[days],nindex))
                        print("{0}/{1}/{2}/{3}/".format(prod,i,julianDay[days],nindex))
                        for object in objs:
                            filename = object.key.rsplit('/',1)[1]
                            pathFile =  createPathGoesData(bucket,i,mth,day[days],prod,nindex)
                            if checkFiles(pathFile,filename):
                                if checkSize(pathFile,filename,object.size):
                                    pass
                                else:
                                    print("Dado: {0}\n".format(filename))
                                    print("Tamanho: {0} Bytes \n".format(object.size))
                                    goes16.download_file(object.key,pathFile+filename,)
                            else:
                                print("Dado: {0}\n".format(filename))
                                print("Tamanho: {0} Bytes \n".format(object.size))
                                goes16.download_file(object.key,pathFile+filename,)
    
                days += 1

    return 0