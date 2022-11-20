data driven on selenium pyhton project

Sample test side used in this project is - http://www.techfios.com/billing/?ng=admin/

Page Object Model is followed in this framework

configuration directory contains the configuration files

data from excel folder conatains excel file data need to be tested

reports folder  contains screenshot

src folder conatains two packages: base page and pages
    first package : base page
           for base page contains locators file (all webelements locators needed to perform this project)
    second package : pages 
           for login page file contains different methods needed to login
           for add customer file contains different methods needed to add customer, validation and delete added customer

test_1 folder contains one package: test_page
    conatins login page test
    contains add customer test 
    contains add customer from Excel file test 

utilities folder contains two files excel utils and read properties
    for excel utils file implimenting different methods used for reading date from excel data file
    for resd properties file implimenting differnt methos used for reading data from configurate file
    
            
    



