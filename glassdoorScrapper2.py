#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:42:22 2021

@author: anupsukumaran
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd


def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
    url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)
        
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        time.sleep(.4)

        #Test for the "Sign Up" prompt and get rid of it.
        try:
            #driver.find_element_by_class_name("selected").click()
            driver.find_element_by_css_selector("a.css-l2wjgv.e1n63ojh0.jobLink").click()
            
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
            print(' x out worked')
        except NoSuchElementException:
            print(' x out failed')
            pass

        try:
            #jblist = driver.find_elements_by_class_name("hover.p-0.css-7ry9k1.exy0tjh5")
            element = driver.find_element_by_id("MainCol")
            job_buttons = element.find_elements_by_tag_name("li")
            print("jblist.Count = {}",len(job_buttons))
        except NoSuchElementException:
            print('Failed Listing1')
            pass
        
        
        # #Going through each job in this page
        # try:
        #     job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
        #     print("job_buttons.Count = {}",len(job_buttons))
        # except NoSuchElementException:
        #     print('Failed Listing2')
        #     pass
        
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  #You might 
            time.sleep(3)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    print("While loop successed")
                    #company_name = job_button.find_element_by_xpath('.//*[@id="MainCol"]/div[1]/ul/li[1]/div[2]/div[1]/a/span"]').text # //*[@id="MainCol"]/div[1]/ul/li[1]/div[2]/div[1]/a/span
                    company_name = job_button.find_element_by_css_selector("a.css-l2wjgv.e1n63ojh0.jobLink").text
                    print(f"company_name = {company_name}")
                    location = job_button.find_element_by_class_name("pr-xxsm.css-1ndif2q.e1rrn5ka0").text
                    print(f"location = {location}")
                    job_title = job_button.find_element_by_css_selector("a.jobLink.css-1rd3saf.eigr9kq2").text
                    print(f"job_title = {job_title}")
                    job_description = driver.find_element_by_class_name("jobDescriptionContent.desc").text
                    print(f"job_description = {job_description}")
                    # print("company_name = {}",company_name)
                    # location = driver.find_element_by_xpath('.//div[@class="location"]').text
                    # job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                    # job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    print("While loop failed")
                    time.sleep(5)

            try:
                #salary_estimate = driver.find_element_by_xpath('.//span[@class="gray salary"]').text css-56kyx5 css-16kxj2j e1wijj242
                print("salary tried and ")
                #salary_estimate = driver.find_element_by_css_selector('s.css-56kyx5.css-16kxj2j.e1wijj242').text
                #salary_estimate = driver.find_element_by_xpath('.//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span/text()').text
                salary_estimate = driver.find_element_by_class_name("css-56kyx5.css-16kxj2j.e1wijj242").text
                print(f"salary_estimate = {salary_estimate}")
                print("..succeeded ")
            except NoSuchElementException:
                print("..failed ")
                salary_estimate = -1 #You need to set a "not found value. It's important."
            
            try:
                #rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
                rating = driver.find_element_by_class_name("css-1m5m32b.e1tk4kwz2").text
                print(f"rating = {rating}")
                print("..succeeded ")
            except NoSuchElementException:
                print("..failed ")
                rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            
           
            
            try:
                #driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()
                companyTabs = driver.find_elements_by_css_selector("div.css-lt549m.ef7s0la1")
                for t in companyTabs:
                    if t.text == "Company":
                        print("Company tab found")
                        t.click()
                        time.sleep(2)
                    else:
                        print("Company tab not found")
            
                print("SUCCESSSS>>>>>")
        
                
                
                
                try:
                    #<div class="infoEntity">
                    #    <label>Headquarters</label>
                    #    <span class="value">San Francisco, CA</span>
                    #</div>
                    headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                    print(f"headquarters = {headquarters}")
                except NoSuchElementException:
                    print("Failed-headquarters")
                    headquarters = -1

                try:
                    #size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                    size = driver.find_element_by_class_name("css-i9gxme.e1pvx6aw2").text
                    print(f"size = {size}")
                except NoSuchElementException:
                    print("Failed-size")
                    size = -1

                try:
                    #founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
                    founded = driver.find_element_by_class_name("css-i9gxme.e1pvx6aw2").text
                    print(f"founded = {founded}")
                except NoSuchElementException:
                    print("Failed-founded")
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_class_name("css-i9gxme.e1pvx6aw2").text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_class_name("css-i9gxme.e1pvx6aw2").text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_class_name("css-i9gxme.e1pvx6aw2").text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_class_name("css-i9gxme.e1pvx6aw2").text
                except NoSuchElementException:
                    revenue = -1

                try:
                    competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                except NoSuchElementException:
                    competitors = -1

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                print("FAILEDD>>>>>")
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                competitors = -1

                
            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Headquarters" : headquarters,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            "Competitors" : competitors})
            #add job to jobs
            
            
        #Clicking on the "next page" button
        try:
            #driver.find_element_by_xpath('.//li[@class="next"]//a').click() //*[@id="FooterPageNav"]/div/ul/li[7]/a
            #driver.find_element_by_xpath('.//*[@id="FooterPageNav"]/div/ul/li[7]/a').click()
            driver.find_element_by_class_name("css-114lpwu.e1gri00l4").click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.