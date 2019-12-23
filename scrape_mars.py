from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time



def init_browser():
    executable_path = {"executable_path": r"C:\Users\Brittany\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrapenews():

    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")


    article = soup.find('div', class_='list_text')
    headlines = article.find('div', class_='content_title').text
    article_txt = article.find('div', class_='article_teaser_body').text

    return headlines, article_txt

def scrapeimg():

    browser = init_browser()
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = bs(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    mars_image = "https://www.jpl.nasa.gov" + image
    
    return mars_image

def scrapeweather():

    browser = init_browser()
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    html = browser.html
    soup = bs(html, "html.parser")
    weather_tweet = soup.find("div", attrs={"class": "tweet", "data-name": "Mars Weather"})
    mars_weather = weather_tweet.find('p', class_='tweet-text').get_text()
    return mars_weather

def scrapefacts():
    
    import pandas as pd
    df = pd.read_html('https://space-facts.com/mars/')[0]
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    html_facts = df.to_html()
    return html_facts

def scrapehemis():
    
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemisphere_image_urls = []
    links = browser.find_by_css("a.product-item h3")

    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        hemisphere['title'] = browser.find_by_css("h2.title").text
        hemisphere_image_urls.append(hemisphere)
        browser.back()

    return hemisphere_image_urls


