# Airflight-Ticket-Tracker
Web scraping program that checks flight tickets for a specific destination and date, which you have to write into the file  manually. The program goes through 2 different websites (Expedia and Kayak) and writes the result into an excell file. There is a sample file included with all the values filled in for a flight between Rio de Janeiro and London. These are the variables that have to be put written in the file before you run:


#### Variables
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


## Setup

#### Selenium and Chromedriver
The python file imports and uses Selenium library for the scraping. Selenium requires that Chromedriver is installed in order to access the websites

[Downloading Selenium](https://selenium-python.readthedocs.io/installation.html)

[Downloading Chromedriver](https://chromedriver.chromium.org/getting-started)

### Windows Task Scheduler

