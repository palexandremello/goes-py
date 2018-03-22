"""### Function used create a directory, with the calendar date the user give to function"""


def createPathGoesData(bucket, year, month, day, product, hour, channel=None):
    import os
    from pathlib import Path
    pathReturn = ''
    '''## that part will get your home directory and the Satellite bucket you're getting your dataset
                                                                                               ######'''
    satGoesPath = bucket.partition('noaa-')[2]
    home = str(Path.home())

    if channel == None:

        if not os.path.exists("{0}/{1}/{2}/{3}/{4}/{5}/{6}/".format(
                home, satGoesPath, year, month, day, product, hour)):

            os.makedirs(
                "{0}/{1}/{2}/{3}/{4}/{5}/{6}/".format(
                    home, satGoesPath, year, month, day, product, hour),
                exist_ok=True)

        pathReturn = "{0}/{1}/{2}/{3}/{4}/{5}/{6}/".format(
            home, satGoesPath, year, month, day, product, hour)

    else:

        if os.path.exists("{0}/{1}/{2}/{3}/{4}/{5}/{6}/{7}/".format(
                home, satGoesPath, year, month, day, product, hour, channel)):
            pass

        else:

            os.makedirs(
                "{0}/{1}/{2}/{3}/{4}/{5}/{6}/{7}/".format(
                    home, satGoesPath, year, month, day, product, hour,
                    channel),
                exist_ok=True)

        pathReturn = "{0}/{1}/{2}/{3}/{4}/{5}/{6}/{7}/".format(
            home, satGoesPath, year, month, day, product, hour, channel)

    return pathReturn
