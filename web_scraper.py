
import requests
from bs4 import BeautifulSoup




def graph():
    # website
    base_url = "https://www.google.com/search?q=coronavirus+facts&source=lmns&bih=937&biw=1920&rlz=1C1CHBF_enUS750US750&hl=en&ved=2ahUKEwiUlISU5q7oAhVjHzQIHfbPB8UQ_AUoAHoECAEQAA"

    # url to be requested
    url = base_url
    wiki_page = requests.get(url)
    # beautiful soup object is being placed(html.parser is important)
    #  raw data with no html tags
    # raw_data = BeautifulSoup(wiki_page.content, 'html.parser').get_text()
    # wiki_soup_page will be used to extract paragraphs
    wiki_soup_page = BeautifulSoup(wiki_page.content, 'html.parser')
    # raw div carries all info included in the search
    print(wiki_soup_page)
    raw_div = wiki_soup_page.find(id='mw-content-text').get_text()
    # data with html tags still
    wiki_div = wiki_soup_page.find(id='mw-content-text')
    # ai starts processing data
    # function to clean data




