# Imports
import re
import pandas as pd
from contextlib import suppress as sr
import requests
from bs4 import BeautifulSoup as bs

# Creating the URL link as a variable & printing it as text
number = []
site = requests.get(f"https://www.jobkorea.co.kr/Search/?stext=english&local=N000&Page_No={number}")

# Parsing the url to BeautifulSoup
soup = bs(site.content, "html.parser")
print(f"{soup.prettify()}")


# Locating all the Company names
def companyNames():
    """
    Goal is to print a list of the companies
    """
    print(f"\nCompany Names are:")
    for company in soup.find_all("div", class_="post-list-corp"):
        try:
            companies = company.a.text
            print(f"{companies}")
        except AttributeError:
            return f"No more information on a tags found..."


# Locating the title of the job ad
def jobTitles():
    """
    Goal is to have it print all the job titles, then under it the information within the ad
    """
    print(f"\nJob Titles are:")
    for job in soup.find_all("div", class_="post-list-info"):
        try:
            jobs = job.a.text
            info = job.span.text
            print(f"{jobs.strip()}\n{info.strip()}")
        except AttributeError:
            return f"No more information on a tags found..."


# Locating the general salary options of the companies
def salaryOptions():
    """
    the ads themselves don't give the salary offered, this is another part of the site that lets you select what salary
    to search. Goal is to display the ads available for each salary range
    """
    print(f"\nSalary Options are:")
    salary = soup.find_all(text=re.compile("만원.*"))
    [print(f"{cost.strip()}") for cost in salary]
    return f"{salary}"


def collectedInfo(soup: bs) -> list[dict]:
    data = []
    with sr(Exception):
        posts = soup.select("li.list-post")

        for post in posts:
            with sr(Exception):
                companyName = post.select_one(".name.dev_view").text
                titleName = post.select_one(".title.dev-view").text.strip()
                p = post.select_one("p")
                experience = p.select_one(".exp")
                education = p.select_one(".edu")

                info = {
                    "Company Name": companyName,
                    "Job Title": titleName,
                    "Required Experience": experience,
                    "Required Education": education
                }

                data.append(info)
        return data


# Dumping the found data into an Excel Sheet or printing in table format
def dataDump():
    """
    Goal is to have all the data either print out in table format or saved to an excel file
    """
    pass


if __name__ == '__main__':
    companyNames()
    jobTitles()
    salaryOptions()
    dataDump()
    data = collectedInfo(soup)
