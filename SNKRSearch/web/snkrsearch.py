from flask import Flask,render_template,url_for,request,redirect
from scraping import Scraper, scraper
import logging
import sys
import concurrent.futures


app=Flask(__name__)

globalText = ""
globalSize = ""

@app.route('/', methods=['POST','GET'])
def index():
    global verifier
    global globalText
    global globalSize
    if request.method=="POST":
        globalText = request.form['content']
        globalSize = request.form['contentSize']
        if globalText!="":
            return redirect('/results')    
    return render_template('index.html')


@app.route('/results')
def results():
    global globalText
    global globalSize
    scraper = Scraper()

    with concurrent.futures.ThreadPoolExecutor() as exec:
        t1 = exec.submit(scraper.SneakerIndustryScraper,str(globalText),str(globalSize))
        t2 = exec.submit(scraper.BuzzSneakersScraper,str(globalText),str(globalSize))
        t3 = exec.submit(scraper.TikeScraper,str(globalText),str(globalSize))
        t4 = exec.submit(scraper.FootshopScraper,str(globalText),str(globalSize))
        t5 = exec.submit(scraper.SportvisionScraper,str(globalText),str(globalSize))
        t6 = exec.submit(scraper.EpantofiScraper,str(globalText),str(globalSize))
    pairText=""
    pairText+=str(t1.result())   #SnkInd
    pairText+=str(t2.result())   #Buzz
    pairText+=str(t3.result())   #Tike
    #pairText+=str(t4.result())   #FootShop
    pairText+=str(t5.result())   #SportVision
    pairText+=str(t6.result())   #Epantofi

    pairList = pairText.split("!")
    return render_template('results.html',pairs = pairList)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__=="__main__":
    app.run(debug=True)