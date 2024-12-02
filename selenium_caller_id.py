from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


phone_numbers_file = "phone_numbers.txt"  


results_file = "results.txt"  


driver_path = "/usr/barret/chromedriver/bin"  


website_url = "https://www.truecaller.com"  


def read_phone_numbers(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]


def write_results(file_path, results):
    with open(file_path, "w") as file:
        for phone_number in results:
            file.write(f"{phone_number}\n")


driver = webdriver.Chrome(driver_path)
filtered_numbers = []

try:
   
    driver.get(website_url)
    time.sleep(1) 

    
    phone_numbers = read_phone_numbers(phone_numbers_file)

    for phone_number in phone_numbers:
       
        text_field = driver.find_element(By.ID, "phoneFieldId")  

        
        text_field.clear()
        text_field.send_keys(phone_number)
        text_field.send_keys(Keys.RETURN)  

        
        time.sleep(1)

        
        try:
            name_element = driver.find_element(By.ID, "nameFieldId")  
            name = name_element.text
        except Exception:
            name = "Not Found"

        # optional we could generate all the result , further with help of crunch we can filter out results 
        if name == "Surabhi Kumari":
            print(f"Found: {phone_number} belongs to {name}")
            filtered_numbers.append(phone_number)

        
        time.sleep(1)

finally:
   
    write_results(results_file, filtered_numbers)

    
    driver.quit()
