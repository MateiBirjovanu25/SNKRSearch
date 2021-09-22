from os import pardir
from bs4 import BeautifulSoup
import bs4
import requests
import re
import random

class Scraper:
    def SneakerIndustryScraper(self,SearchText=None,SearchSize=None):
        
        returnString=""

        SearchText=str(SearchText).replace(" ","+")
        if SearchSize==None:
            url = "https://sneakerindustry.ro/ro/cautare?s="+str(SearchText)
        else:
            url = "https://sneakerindustry.ro/ro/cautare?s="+str(SearchText)+"&q=Marime+-"+str(SearchSize)
        print(url)
        html = requests.get(url).text
        #print(html)
        soup = BeautifulSoup(html,"lxml")

        eroare = soup.find(class_="text-center error-msg")
        if eroare == None:
            site = soup.find(class_="container-fluid category-page")
            soup = BeautifulSoup(str(site),"lxml")
            pairList = soup.find_all(class_="product-miniature home-product")
            for pair in pairList:
                if pair!=None:
                    soupPrice = BeautifulSoup(str(pair),"lxml")
                    price = soupPrice.find(class_="price")
                    link = soupPrice.find("a")['href']
                    localString="Sneaker Industry"+"@"+str(price.text)+"@"+link
                    returnString=returnString+localString+"!"
        return returnString
    


    def BuzzSneakersScraper(self,SearchText=None,SearchSize=None):
        returnString=""

        
        if SearchSize==None:
            url = "https://www.buzzsneakers.com/RON_ro/produse?search="+str(SearchText)
            SearchText=str(SearchText).replace(" ","+")
        else:
            SearchText=str(SearchText).replace(" ","%20")
            url = "https://www.buzzsneakers.com/RON_ro/produse/?sizeEU="+str(SearchSize)+"&search="+str(SearchText)
        print(url)
        html = requests.get(url).text
        #print(html)
        soup = BeautifulSoup(html,"lxml")
        pairList = soup.findAll("div",class_="item-data col-xs-12")
        for pair in pairList:
            soup = BeautifulSoup(str(pair),"lxml")
            price = soup.find(class_="current-price price-with-discount")
            if price == None:
                price = soup.find(class_="current-price")
                price.text.replace(" ","")
            price=str(price.text).replace(" ","")
            price=str(price).replace("\n","")
            price=str(price).replace("\v","")
            link = soup.find("a")['href']
            localString="Buzz Sneakers"+"@"+price+"@"+link
            returnString=returnString+localString+"!"
        return returnString



    def FootshopScraper(self,SearchText=None,SearchSize=None):
        returnString=""
        HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
                   'Accept-Language': 'en-GB,en,q=0.5' ,
                   'Referer': "https://gooogle.com",
                   'DNT': '1'
        }

        SearchText=str(SearchText).replace(" ","+")
        if SearchSize==None:
            url = "https://www.footshop.ro/ro/search?search_query="+str(SearchText)
        else:
            url = "https://www.footshop.ro/ro/search/size_footwear_eur-"+str(SearchSize)+"?search_query="+str(SearchText)
        print(url)
        html = requests.get(url,headers=HEADERS).text
        #print(html)
        soup = BeautifulSoup(html,"lxml")

        pairList = soup.findAll("div",class_="Products_product_1JtLQ")
        for pair in pairList:
            soup = BeautifulSoup(str(pair),"lxml")
            price = soup.find(class_="ProductPrice_price_137oS ProductPrice_sale_3MiPz")
            if price == None:
                price = soup.find(class_="ProductPrice_price_137oS")
            else:
                price=price.strong
            price=str(price.text).replace(" ","")
            link = soup.find("a")['href']
            localString="Footshop"+"@"+price+"@"+link
            returnString+=localString+"!"
        return returnString

    


    def CollectiveScraper(self,SearchText=None,SearchSize=None):
        returnString=""
        HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
                   'Accept-Language': 'en-GB,en,q=0.5' ,
                   'Referer': "https://gooogle.com",
                   'DNT': '1'
        }

        SearchText=str(SearchText).replace(" ","+")
        if SearchSize==None:
            url = "https://www.collectiveonline.com/ro-ro/search?st="+str(SearchText)
        else:
            url = "https://sneakerindustry.ro/ro/cautare?s="+str(SearchText)+"&q=Marime+-"+str(SearchSize)
        print(url)
        #url = 'https://httpbin.org/headers'
        html = requests.get(url,headers=HEADERS).text
        print(html)
        soup = BeautifulSoup(html,"lxml")

        pairList = soup.findAll("div",class_="Products_product_1JtLQ")
    


    def TikeScraper(self,SearchText=None,SearchSize=None):
        returnString=""

        
        if SearchSize==None:
            SearchText=str(SearchText).replace(" ","+")
            url = "https://www.tike.ro/produse?search="+str(SearchText)
        else:
            SearchText=str(SearchText).replace(" ","%20")
            url = "https://www.tike.ro/produse/?sizeEU="+str(SearchSize)+"&search="+str(SearchText)
        print(url)
        html = requests.get(url).text
        #print(html)
        soup = BeautifulSoup(html,"lxml")

        pairList = soup.findAll("div",class_="item-data col-xs-12")
        for pair in pairList:
            soup = BeautifulSoup(str(pair),"lxml")
            price = soup.find(class_="current-price price-with-discount")
            if price == None:
                price = soup.find(class_="current-price")
            price=str(price.text).replace(" ","")
            #print(price)
            link = soup.find("a")['href']
            localString="Tike"+"@"+price+"@"+link
            returnString=returnString+localString+"!"
        return returnString
    

    def SportvisionScraper(self,SearchText=None,SearchSize=None):
        returnString=""

        SearchText=str(SearchText).replace(" ","+")
        if SearchSize==None:
            url = "https://www.sportvision.ro/produse?search="+str(SearchText)
        else:
            url = "https://www.sportvision.ro/produse/?sizeEU="+str(SearchSize)+"&search="+str(SearchText)
        print(url)
        html = requests.get(url).text
        #print(html)
        soup = BeautifulSoup(html,"lxml")

        pairList = soup.findAll("div",class_="item-data col-xs-12")
        for pair in pairList:
            soup = BeautifulSoup(str(pair),"lxml")
            price = soup.find(class_="current-price price-with-discount")
            if price == None:
                price = soup.find(class_="current-price")
            price=str(price.text).replace(" ","")
            #print(price)
            link = soup.find("a")['href']
            localString="Sportvision"+"@"+price+"@"+link
            returnString=returnString+localString+"!"
        return returnString
    

    def EpantofiScraper(self,SearchText=None,SearchSize=None):
        returnString=""

        SearchText=str(SearchText).replace(" ","+")
        if SearchSize==None:
            url = "https://www.epantofi.ro/s.html?q="+str(SearchText)
        else:
            url = "https://www.epantofi.ro/s/marime:"+str(SearchSize)+".html?q="+str(SearchText)
        print(url)
        html = requests.get(url).text
        #print(html)
        soup = BeautifulSoup(html,"lxml")

        pairList = soup.findAll("div",class_="products-list__item-wrapper")
        wordList = str(SearchText).split("+")
        for pair in pairList:
            verifyAuth = True
            soup = BeautifulSoup(str(pair),"lxml")
            price = soup.find(class_="products-list__special-price")
            if price == None:
                price = soup.find(class_="products-list__regular-price")
            price=str(price.text).replace(" ","")
            #print(price)
            link = soup.find("a")['href']
            for word in wordList:
                if word not in link:
                    verifyAuth = False
                    break
            if verifyAuth == True:
                localString="Epantofi"+"@"+price+"@"+link
                returnString=returnString+localString+"!"
        return returnString
    
    
scraper = Scraper()
#print(scraper.EpantofiScraper(SearchText="air force"))