""" The modules reponsive about the has files on the new directory created with the createPathGoesData,
    and if has a same File, check if are broken"""


def checkSize(path, singleFile, singleSize):
    """  
              That function will check if the file on the path created with the
                        createPathGoesData function is the same on the bucket.
                The variable path is create with the createPathGoesData
            The singleFile is the filename from the data in the bucket 'noaa-goes16'
            and the singleSize is the real size from the same singleFile on the bucket.
    And Will check if the size on the singleFile on the path created with the createPathGoesData is
                equals of the size of the singleSize var form the bucket.

    """

    import os
    from checkFiles import checkFiles
    if checkFiles(path, singleFile):
        if os.path.getsize(path + singleFile) == singleSize:
            return True
        else:
            return False