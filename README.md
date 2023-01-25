# Airflight-Ticket-Tracker
# Plane ticket finder 
Web scraping program that checks flight tickets for a specific destination and date, which you have to write into the file  manually. The program goes through 2 different websites (Expedia and Kayak) and writes the result into an excell file. There is a sample file included with all the values filled in for a flight between Rio de Janeiro and London. These are the variables that have to be put written in the file before you run:

**Location:** 
departing, arriving 

**Airport Code:**
departing_code, arriving_code

**Date:**
start_month, start_day, start_year 
end_month, end_day, end_year


## Requirements

#### Selenium and Chromedriver
The python file imports and uses Selenium library for the scraping. Selenium requires that Chromedriver is installed in order to access the websites

[Downloading Selenium](https://selenium-python.readthedocs.io/installation.html)

[Downloading Chromedriver](https://chromedriver.chromium.org/getting-started)

