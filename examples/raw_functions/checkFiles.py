""" The modules reponsive about the has files on the new directory created with the createPathGoesData,
    and if has a same File, check if are broken"""


def checkFiles(path, singleFile):
    """   checkFiles(path,singleFile): That function will check if exist the file on the path create with the
                                createPathGoesData function
                    The variable path is create with the createPathGoesData
                The singleFile is the filename from the data in the bucket 'noaa-goes16'
            and will check if the singleFile in the path create in the createPathGoesData
    """
    import os
    if os.path.isfile("{0}/{1}".format(path, singleFile)):
        return True
    else:
        return False
