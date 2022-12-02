"""
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
"""


if __name__ == "__main__":
    """
    USING HTML FILES:
    # parsing the html file to beautifulsoup
    with open("Site1.html", encoding="utf-8") as s:
        soup = BeautifulSoup(s, "html.parser")
        # print(soup.prettify())  # prettify makes it indented properly

    # prints the 1st result on the page
    titles = soup.title.text  # adding .text makes it just print the text not the tag
    divs = soup.div
    """
    # print(titles)
    # print(divs)  # prints out the child tags as well

    """
    # using the find method to filter the div tags
    finder = soup.find("div", class_="article")  # locates the class attribute "article" and prints everything in it
    
    can use the find_all method to find all the tags rather than the 1st only
    """
    # print(finder.prettify())

    """
    # accessing child tags
    article = finder.li.a.text  # searches the 'li' tag, then the 'a' tag within that

    if the html has child tags such as a heading with text within it you can just do:
    article = finder.h2.a.text # this will get the the second heading (h2)
    summary = article.p.text # this will get you the text under the h2 heading
    
    Can use this to find any other information needed, just change the class or tag
    """
    # print(article)

    """
    USING RE TO SEARCH MORE DETAILED:
    tags = soup.find_all(text=re.compile("\$.*"))  # this will search the file for any $ symbol + information
    tags = soup.find_all(text=re.compile("\$.*"), limit=1)  # sets the limit of data to be printed
    for tag in tags:
        print(tag.strip())  # gets rid of white spaces
    """

    """
    USING URL LINKS:
    source = requests.get("https://www.jobkorea.co.kr/Search/?stext=english&local=N000").text
    soup = BeautifulSoup(source, "html.parser")
    # print(soup.prettify())

    for article in soup.find_all("body"):
        # print(article.prettify())

        title = article.h1.a.text
        # print(title)

        summary = article.find("div", class_="post-list-info").span.text
        # print(summary)

        try:
            # Gaining video files
            vid = article.find("iframe", class_="youtube-player")["src"]
            vidID = vid.split("/")[4]  # splits the data from / than selects the 4th item
            vidID = vidID.split("?")[0]  # splits the already split data again with ? taking the 1st item
            link = f"https://youtube.com/watch?v={vidID}"   # prints the whole video link
        except Exception as e:
            vidID = None
        """

    # print(vidID)

    """
    USING PANDAS TO DUMP THE DATA TO EXCEL: 
    file = pd.DataFrame(article, columns=["Location", "Requirements", "Cost"])
    file.set_index("Location", inplace=True)
    file.to_csv("JobKoreaEnglish.csv")
    """

    """
    USING SELENIUM WITH EVERYTHING:
    # Setting up Selenium with Chrome
    timeout = 30
    try:
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "Location")))
    except TimeoutException:
        driver.quit()

    # Finding the ID Element
    categoryElement = driver.find_element(By.ID, "Location").text

    # Using XPATH to get unordered lists
    listCategoryElements = driver.find_element(By.XPATH, "//*[@id='J_icms-5000498-1511516689962']/div/ul")
    links = listCategoryElements.find_elements(By.CLASS_NAME, f"jobkorea-site-menu-root-menu")
    """
    # [print(f"element in list, {soup[1].text}") for i in enumerate(soup)]

    """
    # Automating the scraper
    element = driver.find_elements(By.CLASS_NAME("J_ChannelsLink")[1])
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

    # Extracting all the lists
    productTitles = driver.find_elements(By.CLASS_NAME("title"))
    """
    # [print(f"{title.text}") for title in productTitles]

    """
    # Extracting the title, size, price and rating
    containers = driver.find_elements(By.CLASS_NAME("container"))
    size = driver.find_elements(By.CLASS_NAME("productSize"))
    price = driver.find_elements(By.CLASS_NAME("productPrice"))
    score = driver.find_elements(By.CLASS_NAME("productScore"))

    for container in containers:
        productTitles.append(container.find_element(By.CLASS_NAME("title").text))
        size.append(container.find_element(By.CLASS_NAME("productSize").text))
        price.append(container.find_element(By.CLASS_NAME("productPrice").text))
        score.append(container.find_element(By.CLASS_NAME("productScore").text))
    """
    # print(container)
