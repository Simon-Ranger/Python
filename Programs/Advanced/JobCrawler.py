# Imports
from requests import get
from bs4 import BeautifulSoup as bs
from contextlib import suppress as sr
from pandas import DataFrame as df
from openpyxl.workbook import Workbook


def extract(page):
    # Grabs the user agents being used
    headers = {f"User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/108.0.0.0 Safari/537.36"}
    # Sets the website being scraped
    url = f"https://www.jobkorea.co.kr/Search/?stext=english&local=N000&focusTab=&focusGno=40303904&tabType=recruit" \
          f"&Page_No={page}"

    # Grabs the url and header, letting data be taken
    request = get(url, headers)

    # Parses the data
    soup = bs(request.content, "html.parser")
    return soup


def transform(soup):
    # Runs an exception check
    with sr(Exception):
        # Finds all the divs under the class "post" within the url
        divs = soup.find_all("div", {"class": "post"})
    # Loops through the found class "post" for specific data
    for detail in divs:
        with sr(Exception):
            # Grabs the company name
            title = detail.find("a").text.strip()
            # Grabs the job title
            company = detail.find("div", {"class": "post-list-info"}).a.text.strip()
            # Grabs general requirements of the job
            exp = detail.find("p", {"class": "option"}).text.strip().replace("\n", "")

            # Puts the data into a dictionary
            jobs = {
                "title": title,
                "company": company,
                "exp": exp
            }

            # Joins the data into a list
            data.append(jobs)
    return


if __name__ == '__main__':
    # The list that has the data added to
    data = []

    # Loops through the 1st page of the site, grabbing the specified amount of jobs per page
    for i in range(0, 10, 5):
        c = extract(0)
        transform(c)

    # Converts the data from a list into a data frame
    frame = df(data)
    # Doesn't show company information when printing
    print(frame)

    # Saving the data to an Excel (.csv) file
    frame.to_excel("JobKorea.xlsx", index=False)
