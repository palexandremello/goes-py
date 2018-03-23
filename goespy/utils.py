""" Utilites uses on the goespy 

"""

def daytoJulian(year,month,day):
    from goespy import datetime

    i,j,k = 0,0,0
    julianDay=[]
    while i <= len(year)-1:
        while j <= len(month)-1:
            while k <= len(day)-1:
                julian = str(datetime.datetime.strptime('{0}-{1}-{2}'.format(year[i],month[j], day[k]),
                '%Y-%m-%d').timetuple().tm_yday).zfill(3)
                julianDay.append(julian)
                
                k += 1
            j+= 1
        i+=1
    
    
    return julianDay


    
def __isAList(year, month, day, product, hour, channel=None, julianDay=None):
    """ All these variables are strings. This function will "convert" every single string on a List of string, 
    to be use in the Foor loops: If all the arguments are List of string, the function will not convert to List.
        The first argument is the Bucket it's the reposity where has the contents from the satellite, example:  
    
    Bucket='noaa-goes16'
    year  =  single string to Year date: example =  "2018" -> ['2018']
    month =  single string to month date: example = "03" -> ['03']
    day   =  single string for day date: example =  "20" -> ['20']
    hour   = single string to hour, and need be UTC coordinate time date: example =  "06" -> ['06']
    product= single string for ABI sensors products from GOES satellite next-generation example:  "ABI-L1b-RadF" -> ['ABI-L1b-RadF']
    channel = single string for the channels from ABI sensors. Example =  "13" -> ['13']
    """

    if not isinstance(hour, (list, )):
        hour = [hour]
    if not isinstance(year, (list, )):
        year = [year]

    if not isinstance(month, (list, )):
        month = [month]

    if not isinstance(day, (list, )):
        day = [day]

    if not isinstance(product, (list, )):
        product = [product]
    
    if not isinstance(julianDay, (list, )):
        julianDay = daytoJulian(year,month,day)
    if channel  == None:
        return year, month, day, product, hour, julianDay
    else:
        if not isinstance(channel, (list, )):
            channel = [channel]
        
        return year, month, day,product, hour, channel, julianDay

class ProgressPercentage(object):
    def __init__(self, filename,objectSize):
        from goespy import threading
        self._filename = filename
        self._size = objectSize
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        from goespy import sys
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = round((self._seen_so_far / self._size) * 100,2)
            sys.stdout.write('\r{0}: [{1}] {2}%  {3} MB/{4} MB'.format(self._filename, '#'*int((percentage/10)), int(percentage),
                                                                           self._seen_so_far/1e6, self._size/1e6))
            #sys.stdout.write("\r%s  %s MB | %s MB  (%.2f%%)" % (self._filename, str(float(self._seen_so_far/1e6)),
            #                                 str(float(self._size/1e6)), percentage) )
            
            
            sys.stdout.flush()


def bannerDisplay(version):
    text='goes-py'
    ch='=' 
    length=90
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    print("")
    print(banner)
    print(" A Python package can be useful to download dataset from goes satellite on AWS  %sv" % version)
    print("==========================================================================================")