def createPathGoesData(home, bucket, year, month, day, product, hour, channel=None):
    """ The modules reponsive about the has files on the new directory created with the createPathGoesData,
    and if has a same File, check if are broken"""
    """Function used create a directory, with the calendar date the user give to function"""

    from goespy import os
    import errno
    pathReturn = ''
    '''that part will get your home directory and the Satellite bucket you're getting your dataset
                                                                                               '''
    satGoesPath = bucket.partition('noaa-')[2]

    if channel == None:
        ## the code will try create the directory where the GOES-data will be saved, if has a except error as existent directory
        ## that error will be finish
        try:
            os.makedirs(
                "{0}/{1}/{2}/{3}/{4}/{5}/{6}/".format(home, satGoesPath, year, month, day, product, hour))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        pathReturn = "{0}/{1}/{2}/{3}/{4}/{5}/{6}/".format(
            home, satGoesPath, year, month, day, product, hour)

    else:

        if os.path.exists("{0}/{1}/{2}/{3}/{4}/{5}/{6}/{7}/".format(
                home, satGoesPath, year, month, day, product, hour, channel)):
            pass

        else:
            try:
                os.makedirs(
                    "{0}/{1}/{2}/{3}/{4}/{5}/{6}/{7}/".format(
                        home, satGoesPath, year, month, day, product, hour,channel))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        pathReturn = "{0}/{1}/{2}/{3}/{4}/{5}/{6}/{7}/".format(
            home, satGoesPath, year, month, day, product, hour, channel)

    return pathReturn


def checkFiles(path, singleFile):
    """   checkFiles(path,singleFile): That function will check if has files on the recent created path with the
                                createPathGoesData function
                    The variable path is created with the createPathGoesData
                The singleFile is the filename from the data in the bucket 'noaa-goes16'
                     and will check the singleFile exists on the created path
    """
    from goespy import os
    if os.path.isfile("{0}/{1}".format(path, singleFile)):
        return True
    else:
        return False


""" The modules reponsive about existence of files on the new directory created with the createPathGoesData,
    and if has a same File, check if is broken"""


def checkSize(path, singleFile, singleSize):
    """
              That function will check if the file on the path created with the
                        createPathGoesData function is the same on the bucket.
                The variable path is create with the createPathGoesData
            The singleFile is the filename from the data in the bucket 'noaa-goes16'
            and the singleSize is the real size from the same singleFile on the bucket.
    And check if the size on the singleFile on the path created with the createPathGoesData is
                          equal to the original file on the bucket.

    """

    from goespy import os

    if checkFiles(path, singleFile):
        if os.path.getsize(path + singleFile) == singleSize:
            return True
        else:
            return False

def pythonVersion():
## The function is necessary to check yout python version
# IF the your python is < or equal 2.7 so put a True bool
## Else (python > 2.7) put a False bool
    import sys
    if (sys.hexversion <= 34017264):
        return True
    else:
        return False

def setHome():
## Function necessary to check if your python version is < 2.7 or > 2.7
### if your python is more than 2.7 the function will default uses the pathlib function to get your home directory
### but if you use the python version 2.7, so the function will uses the os.path to get your home directory
    from os.path import expanduser

    if  pythonVersion():

        return expanduser("~")

    else:
        from pathlib import Path
        return str(Path.home())
