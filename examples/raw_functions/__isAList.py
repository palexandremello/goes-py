"""        __isAList(year,month,day,product,hour,channel=None,julianDay=None): All these variables are strings.
             This function will "convert" every single string on a List of string, to be use in the Foor loops:
                    If all the arguments are List of string, the function will not convert to List.

        The first argument is the Bucket it's the reposity where has the contents from the satellite, example:

    Bucket='noaa-goes16'
    year  =  single string to Year date: example =  "2018" -> ['2018']
    month =  single string to month date: example = "03" -> ['03']
    day   =  single string for day date: example =  "20" -> ['20']
    hour   = single string to hour, and need be UTC coordinate time date: example =  "06" -> ['06']
    product= single string for ABI sensors products from GOES satellite next-generation example:  "ABI-L1b-RadF" -> ['ABI-L1b-RadF']
    channel = single string for the channels from ABI sensors. Example =  "13" -> ['13']
    """


def __isAList(year, month, day, product, hour, channel=None, julianDay=None):

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

    if julianDay == None:
        return year, month, day, product, hour
    else:
        if not isinstance(julianDay, (list, )):
            julianDay = [julianDay]

    return year, month, day, product, hour, julianDay
