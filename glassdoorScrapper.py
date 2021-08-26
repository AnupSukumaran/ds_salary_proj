# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pandas as pd


def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    print("get_jobs - Func")
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
   

    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    jobs = []
    
    # time.sleep(slp_time)
    
    # main = driver.find_element_by_id("MainCol") #find_element_by_class_name("hover p-0  css-7ry9k1 exy0tjh5")
    # #main = driver.find_element_by_class_name("p-0_css-4ik2ye_exy0tjh1")
    # print("MAINDATR = {}",main.text)
    
   # search = driver.find_element("Data Science") #find_element_by_name("Data Science")
    # search.send_keys("iOS Developer")
    # search.send_keys(Keys.RETURN)
    
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "MainCol")) )
        #print("MAINDATR = {}",element.text)
        lists = element.find_elements_by_tag_name("li")
        print("Count = {}", len(lists))
        
        newlist = element.find_elements_by_css_selector("a.css-l2wjgv.e1n63ojh0.jobLink")
        print("newCount = {}", len(newlist))
        
        for item in lists:
            #title = item.find_element_by_class_name(".css-l2wjgv.e1n63ojh0.jobLink")
            title = item.find_element_by_css_selector("a.css-l2wjgv.e1n63ojh0.jobLink")
            #title = item.find_element(By.CLASS_NAME,".css-l2wjgv.e1n63ojh0.jobLink")
            print("title = {}", title.text)
    
    except ElementClickInterceptedException:
        print("NoSuchElementException-2344")
        pass

    #while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        #time.sleep(slp_time)

        #Test for the "Sign Up" prompt and get rid of it.
        
        # try:
        #     driver.find_element_by_css_selector('react-job-listing css-7x0jr eigr9kq3').click()
        # except ElementClickInterceptedException:
        #     print("NoSuchElementException-2344")
        #     pass
        
        
        # try:
        #     driver.find_element_by_class_name("hover p-0  css-7ry9k1 exy0tjh5").click()
        # except NoSuchElementException:
        #     print("NoSuchElementException-1112")
        #     pass
        # except ElementClickInterceptedException:
        #     print("NoSuchElementException-1110")
        #     pass

        # time.sleep(.1)
        
        # try:
        #     driver.find_element_by_css_selector('[alt="Close"]').click()
        # except ElementClickInterceptedException:
        #     print("NoSuchElementException-2344")
        #     pass

        # try:
        #     driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()  #clicking to the X.
        # except NoSuchElementException:
        #     print("NoSuchElementException-11")
        #     pass

        
        # #Going through each job in this page
        # job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
        # for job_button in job_buttons:  

        #     print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
        #     if len(jobs) >= num_jobs:
        #         break

        #     job_button.click()  #You might 
        #     time.sleep(1)
        #     collected_successfully = False
            
        #     while not collected_successfully:
        #         try:
        #             company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
        #             location = driver.find_element_by_xpath('.//div[@class="location"]').text
        #             job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
        #             job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
        #             collected_successfully = True
        #         except:
        #             time.sleep(5)

        #     try:
        #         salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
        #     except NoSuchElementException:
        #         print("NoSuchElementException-12")
        #         salary_estimate = -1 #You need to set a "not found value. It's important."
            
        #     try:
        #         rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
        #     except NoSuchElementException:
        #         print("NoSuchElementException-13")
        #         rating = -1 #You need to set a "not found value. It's important."

        #     #Printing for debugging
        #     if verbose:
        #         print("Job Title: {}".format(job_title))
        #         print("Salary Estimate: {}".format(salary_estimate))
        #         print("Job Description: {}".format(job_description[:500]))
        #         print("Rating: {}".format(rating))
        #         print("Company Name: {}".format(company_name))
        #         print("Location: {}".format(location))

        #     #Going to the Company tab...
        #     #clicking on this:
        #     #<div class="tab" data-tab-type="overview"><span>Company</span></div>
        #     try:
        #         driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()

        #         try:
        #             #<div class="infoEntity">
        #             #    <label>Headquarters</label>
        #             #    <span class="value">San Francisco, CA</span>
        #             #</div>
        #             headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-1")
        #             headquarters = -1

        #         try:
        #             size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-2")
        #             size = -1

        #         try:
        #             founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-3")
        #             founded = -1

        #         try:
        #             type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-4")
        #             type_of_ownership = -1

        #         try:
        #             industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-5")
        #             industry = -1

        #         try:
        #             sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-6")
        #             sector = -1

        #         try:
        #             revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-7")
        #             revenue = -1

        #         try:
        #             competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
        #         except NoSuchElementException:
        #             print("NoSuchElementException-8")
        #             competitors = -1

        #     except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
        #         print("NoSuchElementException-9")
        #         headquarters = -1
        #         size = -1
        #         founded = -1
        #         type_of_ownership = -1
        #         industry = -1
        #         sector = -1
        #         revenue = -1
        #         competitors = -1

                
        #     if verbose:
        #         print("Headquarters: {}".format(headquarters))
        #         print("Size: {}".format(size))
        #         print("Founded: {}".format(founded))
        #         print("Type of Ownership: {}".format(type_of_ownership))
        #         print("Industry: {}".format(industry))
        #         print("Sector: {}".format(sector))
        #         print("Revenue: {}".format(revenue))
        #         print("Competitors: {}".format(competitors))
        #         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        #     jobs.append({"Job Title" : job_title,
        #     "Salary Estimate" : salary_estimate,
        #     "Job Description" : job_description,
        #     "Rating" : rating,
        #     "Company Name" : company_name,
        #     "Location" : location,
        #     "Headquarters" : headquarters,
        #     "Size" : size,
        #     "Founded" : founded,
        #     "Type of ownership" : type_of_ownership,
        #     "Industry" : industry,
        #     "Sector" : sector,
        #     "Revenue" : revenue,
        #     "Competitors" : competitors})
        #     #add job to jobs

        # #Clicking on the "next page" button
        # try:
        #     driver.find_element_by_xpath('.//li[@class="next"]//a').click()
        # except NoSuchElementException:
        #     print("NoSuchElementException-10")
        #     print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
        #     break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.


# #This line will open a new chrome window and start the scraping.
# df = get_jobs("data scientist", 5, False)
# df