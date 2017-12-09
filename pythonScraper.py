from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

#Feed commands in this order: python3 pythonScraper.py <FILENAME> <SEARCHTERM>

def main():

    scraper(sys.argv[1], navTo(sys.argv[2],"https://www.newegg.com/"))


def navTo(search_term, ADDRESS):
    browser = webdriver.Firefox()
    browser.get(ADDRESS)
    search_box = browser.find_element_by_id("haQuickSearchBox") #this is the id of the searchbox element on newegg.com
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.submit()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID,"baBreadcrumbTop")))

    browser.find_element_by_xpath("//a[@title='Desktop Graphics Cards']").click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID,"baBreadcrumbTop")))
    url = browser.current_url
    browser.close()
    print(url)
    return url


def scraper(FILE_NAME, SCRAPE_URL):
    f = open(FILE_NAME, "w")

    headers = "brand, product_name, cost, shipping, rating, reviews\n"
    f.write(headers);

    page_next = 1
    #while page_next:
    #open connection
    uClient = uReq(SCRAPE_URL)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    i = 0
    #geteachproduct
    containers = page_soup.findAll("div",{"class":"item-container"})

    #For all the items on the page
    for container in containers:

        #Find the brand of the item
        brand = container.div.div.a.img["title"]

        print("brand: " + brand)

        #Find the product's name
        title_container = container.findAll("a",{"class":"item-title"})
        product_name = title_container[0].text
        print("name: " + product_name)

        #Find the rating of the product
        rating_container = container.findAll("a",{"class":"item-rating"})

        #If there is no rating for the product, set
        #its rating and reviews to -1
        if not rating_container:
            print("No ratings found for this card!\n")
            rating = "-1"
            reviews = "-1"
        #If found, save rating and reviews
        else:
            rating = rating_container[0]["title"]
            print("rating: " + rating)
            reviews = rating_container[0].span.text
            print("reviews: " + reviews)

        #Find the shipping cost of the product
        shipping_container = container.findAll("li",{"class","price-ship"})

        #If there is no shipping cost, there must also not be a price, so
        #set cost and shipping to -1
        if not shipping_container:
            print("No Shippping Cost found")
            shipping = -1
            cost = -1
        #else get the shipping cost of the container
        else:
            shipping = shipping_container[0].text.strip()
            print("shipping cost: " + shipping)

            #Find the cost of the product
            cost_container = containers[i].findAll("li",{"class","price-current"})

            #if for some reason there still isnt a price, then store it as -1
            if not cost_container:
                print("No Price found for this card!\n")
                cost = -1
            #Else save the cost
            else:
                cost = cost_container[0].strong.text + cost_container[0].sup.text
            print("cost: " + cost)
        i = i + 1



        print("\n")

        f.write(brand + "," + product_name.replace(",","|") + "," + cost + "," + shipping + "," + rating.replace("Rating +"," ") + "," + reviews + "\n")

    #container_page = page_soup.findAll("span",{"class","list-tool-pagination-text"})
    #rawPagecount = container_page[1].strong.text
    #currentPage = rawPagecount[0]
    #totalPages = rawPagecount[2:]
    #pageRatio = float(currentPage) / float(totalPages)
    #if pageRatio < 1:
    #    browser = webdriver.Firefox()
    #    browser.get(SCRAPE_URL)
    #    browser.find_element_by_xpath("//button[@title='Next']").click()
    #    wait = WebDriverWait(browser, 10)
    #    wait.until(EC.presence_of_element_located((By.ID,"baBreadcrumbTop")))
    #    SCRAPE_URL = browser.current_url
    #    browser.close()
    #else:
    #    page_next = 0

    f.close()

main();
