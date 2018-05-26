# goes-py 0.2.1v 

 It's a free Python package to acess and get the dataset from GOES satellite next generation on Amazon Web Service(AWS)
 
 For more details, look online documentation (soon)

## HOWTO-Install 
 
 ### 1. Source code:
 
 If you want to build this package, just clone this repository:

 >**git clone https://github.com/palexandremello/goes-py.git**

 Go to folder:

>**cd goes-py** 

 And install manually

>**python setup.py install**

But if you don't want to build the cloned repository, just use the pip on terminal.

 ### 2. Pip Install: 
 
  Acess a terminal and use the command **pip**:
  
  > **pip install goespy**

 ### 3. Update the package:
 
The goespy will have more new version in the future, so when this release comes. you need upgrade your package, so use this command on terminal. (new release 0.2v)

 > **pip install --upgrade goespy** 
 
 Or if you want build again the new source code
 
 ## Examples how to use:

 This package has two main function, can be used to get dataset from GOES:

 ### 1. HOW TO get from ABI-sensors:
 
First open a file with the filename **firstexample.py** and put the next command on header's script.

> **from goespy.Downloader import ABI_Downloader**

You will import the **ABI_Downloader** function, and the **ABI_Downloder** needs 7 arguments to be used:

> **ABI_Downloader(bucket,year,month,day,hour,product,channel)**

>bucket: name of reposity from GOES on the Amazon Web Service (AWS)

>year: year string 

>month: month string 

>day: day string

>hour: hour string, but it's need be UTC coordinate not local time

>product: "ABI-sensors" for this example we will use FullDisk L2

>channel: channels of your choose, can be C01 at C16

Below do the initialization for these variable in your firstexample.py :

>  bucket = 'noaa-goes16'

>  year='2018'

> month='03'

> day='22'

> hour='12'

> product='ABI-L2-CMIPF'

> channel='C13'

Now, you can call the function, so write it on your **firstexample.py**:

> ABI = ABI_Downloader(bucket,year,month,day,hour,product,channel)


And run the script 

> python firstexample.py 

wait for download to complete (you can see the progress)


Now, you can call the function, so write it on your **firstexample.py** after you initialized the variables above:
> ABI = ABI_Downloader(bucket,year,month,day,hour,product,channel)

And run the script 

> python firstexample.py 

wait for download to complete (you can see the progress)

After the download to finishes, check your home directory (**Linux and mac OS X users**) and your dataset will be in a directory has the same name from the satellite used on bucket variable. In this case: **goes16**.

 ### 2. HOW TO get from GLM total lightning:
 
> **from goespy import GLM_Downloader**

For the GLM use an especific example on the **examples/** in the source directory.

 ## Contributors: 
 Centro de Pesquisas e Previsões Meteorológicas Prof. Darci Pegoraro Casarin ( <a href="https://wp.ufpel.edu.br/cppmet/">CPMET</a>) for the place and computers necessary to work on this project 

