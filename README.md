# earthengine-image-downloader
This script consists of the most suitable way to integrate geopy and google earth-engine in such a way that you can automatically download the
satellite images for training purposes in machine learning .I have tried the google-colab and the normal  terminal preinstalled packages but the task
here is to give the authentication key and its a difficult task in between code execution.So i prefer you to  use anaconda enviornment it will automatically stores the api in cache and it saves time from a user to reauthenticate.

 REQUIREMENTS FOR INSTALLING........
 
 1) INSTALL ANACONDA
    
      https://docs.anaconda.com/anaconda/install/
 
 2) CONFIGURING THE PACKAGES
   * To install this package with conda run one of the following:
   
       conda install -c conda-forge earthengine-api
       
       conda install -c conda-forge/label/gcc7 earthengine-api
       
       conda install -c conda-forge/label/cf201901 earthengine-api
   * Get Credentials
      Before getting credentials its better to try google earth engine is already authenticated so in your conda enviornment type
      
             # earthengine authenticate
3) Testing the API

   * Start a python interpreter from your conda by typing python
             # python 
   * Run the following Python lines one-by-one in python interpreter to print the metadata for a DEM dataset
   
             # import ee
             
             # ee.Initialize()
             
             # print(ee.Image('USGS/SRTMGL1_003').getInfo())
 
 
 
      EUREKA !!!! you have completed the level one :) smile
             

 

