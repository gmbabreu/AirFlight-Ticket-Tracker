# Imports for Selenium tester
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from openpyxl import load_workbook

# Departing Information
departing = "New York"
departing_code = "NYC"

# Destination information 
destinations = ["London", "Paris"]
destination_codes = ["LON","PAR" ]

# Dates
start_month = "11"
start_day = "30"
start_year = "2023"

end_month = "12"
end_day = "26"
end_year = "2023"

# Set up driver and date
driver = webdriver.Chrome()
today = date.today().strftime("%m/%d/%y")

def main():   
    """
    Operates the main excell file
    """    
    # Open excell file and add data
    wb = load_workbook(filename = 'Ticket_tracker.xlsx')
   
    kayak(wb)
    expedia(wb)
    #skyscanner(wb)
    
    wb.save('Ticket_tracker.xlsx') 
         

def kayak(wb):
    """
    Goes through the kayak search bar and finds lowest price
    """
    data = (today,)

    # iterate through each destination
    for i in range(len(destinations)):

        dcode = destination_codes[i]

        # Search Link
        link = "https://www.kayak.com/flights/"+departing_code+"-"+dcode+"/"+start_year+"-"+start_month+"-"+start_day+"/"+end_year+"-"+end_month+"-"+end_day+"?sort=price_a"
        driver.get(link)

        # Get Price
        time.sleep(10)
        element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@class, "price-text")]')))
        price = element.text[1:4]
        data = data + (price,)

    # Append price
    wb.get_sheet_by_name("kayak").append(data)

    return price
    

def expedia(wb): 
    """
    Goes through the expedia search bar and finds lowest price
    """
    data = (today,)

    # iterate through each destination
    for i in range(len(destinations)):
        arriving = destinations[i]
        arriving_code = destination_codes[i]

        # Search link
        name1 = departing.replace(" ", "%20")
        name2 = arriving.replace(" ", "%20")
        link = "https://www.expedia.com/Flights-Search?leg1=from%3A"+name1+"%20%28"+departing_code+"%20-%20All%20Airports%29%2Cto%3A"+name2+"%20%28"+arriving_code+"-All%20Airports%29%2Cdeparture%3A"+start_month+"%2F"+start_day+"%2F"+start_year+"TANYT&leg2=from%3A"+name2+"%20%28"+arriving_code+"-All%20Airports%29%2Cto%3A"+name1+"%20%28"+departing_code+"%20-%20All%20Airports%29%2Cdeparture%3A"+end_month+"%2F"+end_day+"%2F"+end_year+"TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&trip=roundtrip "
        driver.get(link)

        # Get Price
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[contains(@class, "uitk-lockup-price")]')))
        price = element.text.replace("$", "")
        data = data + (price,)

    # Append price
    wb.get_sheet_by_name("expedia").append(data)

    return price

def skyscanner(wb):
    """
    Goes through the Skyscanner website and finds the lowest price
    """
    data = (today,)

    # iterate through each destination
    for i in range(len(destinations)):

        dcode = destination_codes[i]

        # Search Link
        link = "https://www.skyscanner.com/transport/flights/"+departing_code+"/"+dcode+"/"+start_year[-2:]+start_month+start_day+"/"+end_year[-2:]+end_month+end_day+"/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27544008&inboundaltsenabled=false&infants=0&originentityid=27539525&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
        driver.get(link)

        # Get Price
        element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@class = "FqsTabs_fqsTabWithSparklePriceSelected__ODBjZ"]//span[1]')))
        price = element.text
        data = data + (price,)
        
    # Append price
    wb.get_sheet_by_name("skyscanner").append((today, price))

    return price

if __name__ == "__main__":
    main()
