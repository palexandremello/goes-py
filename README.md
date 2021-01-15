# goes-py

[![Downloads](https://pepy.tech/badge/goespy)](https://pepy.tech/project/goespy) 
[![Version](https://img.shields.io/pypi/v/goespy.svg)](https://pypi.org/project/goespy/)

 This Python package provides functions to download [GOES (GOES-16 & GOES-17) products from Amazon Web Services (AWS)](https://registry.opendata.aws/noaa-goes/).
 
## Installing goes-py
 
 ### Option 1: Installing from source code:
 
 If you want to build this package, just clone this repository:
 
```bash
$ git clone https://github.com/palexandremello/goes-py.git

$ cd goes-py

$ python setup.py install
```

 ### Option 2: Installing with pip: 
 
 If you don't want to build from the cloned source code repository, just use pip in a terminal.
 
  Access a terminal and use the command **pip**:
  ```bash
  $ pip install goespy
  ```
  
## Updating goes-py

 ### Option 1: Install again from source code:
 
 Build the package again from the new version of the source code to update goes-py.

 ### Option 2: Update with pip:
 
 The goes-py package will have new versions in the future, you will need upgrade your package to use these future releases. Use this command in a terminal to update goes-py. (new release 0.2v)

 ```bash
 $ pip install --upgrade goespy 
 ```
 
## Examples how to use:

 This package has two main functions to download GOES products from AWS:

 ### 1. HOW TO download ABI products:
 
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
channel: Required only for "ABI-L1b-Rad" and "ABI-L2-CMIP" products (can be C01 through C16). Channel is ignored for other ABI products.
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

 ### 2. HOW TO download GLM total lightning product:
 
```py
from goespy import GLM_Downloader
```

For the GLM use see the example in **examples/** in the source directory.

 ## Contributors: 
 
 * [Paulo Alexandre Mello](https://github.com/palexandremello)
 * Centro de Pesquisas e Previsões Meteorológicas Prof. Darci Pegoraro Casarin (<a href="https://wp.ufpel.edu.br/cppmet/">CPMet</a>) for the place and computers necessary to work on this project 
 * [Steven Pestana](https://github.com/spestana/)

