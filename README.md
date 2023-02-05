# Airflight-Ticket-Tracker
This is a webscraping program that checks flight tickets for a specific destination and date, which you have to write into the file  manually. The program goes through 3 different websites (Expedia, Kayak, and Skyscanner) and writes the result into an excell file. There is a sample file included with all the values filled in for a flight between Rio de Janeiro and London. These are the variables that have to be put written in the file before you run:


## Setup

#### Selenium and Chromedriver
The python file imports and uses Selenium library for the scraping. Selenium requires that Chromedriver is installed in order to access the websites. It also requires openpyxl in order to manage the excell file.

[Downloading Selenium](https://selenium-python.readthedocs.io/installation.html)

[Downloading Chromedriver](https://chromedriver.chromium.org/getting-started)

[Downloading Openpyxl](https://pypi.org/project/openpyxl/)

## Python file

In order to configure the flights you want to search for, you need to fill in the following variables in the Ticket_Tracker.py file.

**Departing Information:** 
- departing = city you are leaving
- departing_code = code for city you are leaving (airport code or the first three letter of the city should work)

**Destination Information:**
- destinations = list of cities you want to go to
- destination_codes = list of codes for each of the cities in the destinations list

**Date:**
- start_month = month departing
- start_day = day departing
- start_year = year departing
- end_month = month returning
- end_day = day returning
- end_year = year returning


*Example*

![image](https://user-images.githubusercontent.com/98294696/216842968-6dcf9f03-87e8-4cdf-bdd7-a0e674e7a2c9.png)

## XLSX file

There are three sheets on the excell file for each of the websites the program gets prices from. On each of the sheets, you should put the name of the destination cities in the header (substitute it for city1, city2, city3, etc). They should be in the same order as the destinations list in the python file

*Example*

![image](https://user-images.githubusercontent.com/98294696/216845293-fe7916d1-42c5-4bd2-b527-b17830c4a78a.png)

## Windows Task Scheduler

Finally, use the Windows Task Scheduler to configure the file to run everyday
