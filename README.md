# goes-py

[![Downloads](https://pepy.tech/badge/goespy)](https://pepy.tech/project/goespy) 
[![Version](https://img.shields.io/pypi/v/goespy.svg)](https://pypi.org/project/goespy/)

 It's a Python package to acess and get the dataset from GOES satellite next generation on Amazon Web Service(AWS)
 
## HOWTO-Install 
 
 ### 1. Source code:
 
 If you want to build this package, just clone this repository:
```bash
$ git clone https://github.com/palexandremello/goes-py.git

$ cd goes-py

$ python setup.py install
```
But if you don't want to build the cloned repository, just use the pip on terminal.

 ### 2. Pip Install: 
 
  Acess a terminal and use the command **pip**:
  ```bash
  $ pip install goespy
  ```
 ### 3. Update the package:
 
The goespy will have more new version in the future, so when this release comes. you need upgrade your package, so use this command on terminal. (new release 0.2v)
 ```bash
 $ pip install --upgrade goespy 
 ```
 Or if you want build again the new source code
 
 ## Examples how to use:

 This package has two main function, can be used to get dataset from GOES:

 ### 1. HOW TO get from ABI-sensors:
 
First open a file with the filename **firstexample.py** and put the next command on header's script.

```py
from goespy.Downloader import ABI_Downloader
```

You will import the **ABI_Downloader** function, and the **ABI_Downloder** needs 8 arguments to be used:

```py
ABI_Downloader(destination_path, bucket,year,month,day,hour,product,channel)
```

```**
destination_path: path where you want to save your goes satellite data
bucket: name of reposity from GOES on the Amazon Web Service (AWS)
year: year string 
month: month string 
day: day string
hour: hour string, but it's need be UTC coordinate not local time
product: "ABI-sensors" for this example we will use FullDisk L2
channel: channels of your choose, can be C01 at C16**
```
Below do the initialization for these variable in your firstexample.py :

```py
destination_path = '/home/paulo/Downloads/goes_data/'
bucket = 'noaa-goes16'
year='2018'
month='03'
day='22'
hour='12'
product='ABI-L2-CMIPF'
channel='C13'
```

Now, you can call the function, so write it on your **firstexample.py**:

```py
ABI = ABI_Downloader(destination_path, bucket,year,month,day,hour,product,channel)
```


And run the script 

```sh
python firstexample.py
```

After the download to be finishes, check your destination path (**Linux and mac OS X users**) and your dataset will be in a directory with the same name from the satellite used on bucket variable. In this case: **goes16**.

 ### 2. HOW TO get from GLM total lightning:
 
```py
from goespy import GLM_Downloader
```

For the GLM use an especific example on the **examples/** in the source directory.

 ## Contributors: 
 Centro de Pesquisas e Previsões Meteorológicas Prof. Darci Pegoraro Casarin (<a href="https://wp.ufpel.edu.br/cppmet/">CPMet</a>) for the place and computers necessary to work on this project 

