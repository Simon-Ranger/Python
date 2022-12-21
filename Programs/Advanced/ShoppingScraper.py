# Created by Simon Ranger : December 17th 2022

"""
This is a more advanced project that is meant to look through a shopping site.

How to Use:
1. Change the link to the site you want to grab the data from.
2. When getting the results check the Excel file incase the data is too long for the output

Desired Output:
Grabs the specified information from the specified site, giving the results in the output as well as an Excel file.
"""

# Imports required
import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict
from contextlib import suppress as sr


@dataclass
class Data:
    item_name: str
    single_price: str
    kg_price: str
    overall_price: str


def get_html(page: int) -> HTMLParser:
    """
    Gets the html and connects it with the parser

    Args:
        page: int: lets you get the number of pages you want to scrape

    Returns:
        HTMLParser: lets you gather the data from the site
    """

    # Sets the website being scraped
    resp = httpx.get(url=f"https://www.coles.com.au/browse/fruit-vegetables?page={page}")
    return HTMLParser(resp.text)


def parse_products(html) -> list:
    """
    Gathers the specified data from the website

    Args:
        html: used to gather the data

    Returns:
        list: holds the data
    """

    products = html.css("div")
    results = []

    # loops through an exception to catch any errors while collecting the specified data
    with sr(Exception):
        for item in products:
            new_item = Data(
                item_name=item.css_first("h2").text(),
                single_price=item.css_first("div.price").text(),
                kg_price=item.css_first("span.price__calculation_method").text(),
                overall_price=item.css_first("span.price__calculation_method__description").text()
            )

            results.append(asdict(new_item))
    return results


def main() -> None:
    """
    Runs the other functions, including the loop required to set the amount of pages to be done. Tests to see if the
    tags collects the data properly.

    Args:

    Returns:
        None
    """

    # loops through an exception while also looping through the pages
    with sr(Exception):
        for i in range(1, 16):
            html = get_html(i)
            print(parse_products(html))


if __name__ == "__main__":
    main()
