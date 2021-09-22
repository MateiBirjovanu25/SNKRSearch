import threading
import tkinter as tk
from tkinter import Button, Canvas, Entry, Frame, Label, Scrollbar, StringVar, Toplevel, filedialog, Text,ttk,messagebox
import os
import tkinter
from tkinter import font
from tkinter.constants import ACTIVE, ANCHOR, CENTER, NO, RIDGE, RIGHT, Y
from PIL import ImageTk,Image
from scraping import Scraper
from threading import Thread
import concurrent.futures

root = tk.Tk()
root.configure(background="#C38D9E")

gotInfo=False

def tree_click_handler(event):
    try:
        cur_item = pairTree.item(pairTree.focus())
        col = pairTree.identify_column(event.x)
        root.clipboard_clear()
        root.clipboard_append(cur_item['values'][2])
    except:
        print("ayaye")


def searchFunc():
    global searchEntry
    scraper = Scraper()
    global resultWindow
    resultWindow = Toplevel()
    resultWindow.configure(background="#00ab90")
    entryText = searchEntry.get()
    #print(entryText)
    
    with concurrent.futures.ThreadPoolExecutor() as exec:
        t1 = exec.submit(scraper.SneakerIndustryScraper,str(entryText))
        t2 = exec.submit(scraper.BuzzSneakersScraper,str(entryText))
        t3 = exec.submit(scraper.TikeScraper,str(entryText))
        t4 = exec.submit(scraper.FootshopScraper,str(entryText))
        t5 = exec.submit(scraper.SportvisionScraper,str(entryText))
        t6 = exec.submit(scraper.EpantofiScraper,str(entryText))
    pairString=""
    pairString=str(t1.result())+str(t2.result())+str(t3.result())+str(t5.result())+str(t6.result())

    '''
    pairString = scraper.SneakerIndustryScraper(SearchText=str(entryText))
    pairString+=scraper.BuzzSneakersScraper(SearchText=str(entryText))
    pairString+=scraper.TikeScraper(SearchText=str(entryText))
    pairString+=scraper.FootshopScraper(SearchText=str(entryText))
    pairString+=scraper.SportvisionScraper(SearchText=str(entryText))
    pairString+=scraper.EpantofiScraper(SearchText=str(entryText))
    '''

    pairList = pairString.split("!")
    
    num=0
    global pairTree

    treeFrame = Frame(resultWindow,width=300)
    treeFrame.pack()

    treeScroll = Scrollbar(treeFrame)
    treeScroll.pack(side=RIGHT,fill=Y)
    

    pairTree = ttk.Treeview(treeFrame,yscrollcommand=treeScroll.set)

    treeScroll.config(command=pairTree.yview)

    treeStyle = ttk.Style()
    treeStyle.theme_use("default")

    treeStyle.configure("Treeview",
        background= "#bffff5",
        fieldbackground="#00ab90"
    )
    treeStyle.configure("Treeview.Heading",
        background= "#00ab90",
        fieldbackground="#007865"
    )
    treeStyle.map("Treeview",background=[('selected',"#00AB78")])

    


    pairTree['columns']=("Site","Price","Link")
    pairTree.column("#0",width=0,minwidth=0)
    pairTree.column("Site",anchor="w",width=105)
    pairTree.column("Price",anchor=CENTER,width=70)
    pairTree.column("Link",anchor="w",width=300)

    pairTree.heading("#0",text="")
    pairTree.heading("Site",text="Site",anchor=CENTER)
    pairTree.heading("Price",text="Price",anchor=CENTER)
    pairTree.heading("Link",text="Link",anchor=CENTER)
    pairTree.bind('<ButtonRelease-1>', tree_click_handler)
    pairTree.pack()

    #messagebox.showinfo("info","click a line to copy the link")

    for pair in pairList:
        if "@" in pair:
            pairTree.insert(parent="",index="end",iid=num,values=(pair.split("@")[0],pair.split("@")[1].lstrip(),pair.split("@")[2]))
            num+=1
        


centralFrame = Frame(root,bg="#41b3a3",border=100,borderwidth=10)
centralFrame.pack(anchor="center")

canvasCentral = Canvas(centralFrame,bg="#41b3a3")
#canvasCentral.grid(row=0,column=0,columnspan=3)

logoImg = ImageTk.PhotoImage(Image.open("logo2.png"))
labelImg = Label(centralFrame,image=logoImg,bg="#41b3a3",anchor="e")
labelImg.grid(row=0,column=1)


searchEntry = Entry(centralFrame,width=50,bg="#bffff5",font="Helvetica 12")
searchEntry.grid(row=1,column=1,padx=0,ipady=6)

curentValue = StringVar()
spinSize = ttk.Spinbox(centralFrame,from_=35,to=47,textvariable=curentValue,width=10,background="#E27D60")
#spinSize.grid(row=2,column=0,columnspan=2,pady=10,)

buttonImg = ImageTk.PhotoImage(Image.open("search.png"))
btnSearch = Button(centralFrame,image=buttonImg,bg="#41b3a3",borderwidth=0,width=30,padx=0,command=searchFunc)
btnSearch.grid(row=1,column=0,padx=1,sticky="e")

root.mainloop()
