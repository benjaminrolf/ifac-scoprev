import os
import pandas as pd
import PyPDF2


# read csv file
pubs = pd.read_csv('publications.csv')

# define directory and keywords
path = 'C:/Users/benja/Documents/ifac-scoprev/keyword-crawler/library'
keywords = ['and']

# loop through all PDFs in specified directory
for filename in os.listdir(path):
    if filename.endswith(".pdf"):
        # open the pdf file
        with open(os.path.join(path, filename), 'rb') as f:
            object = PyPDF2.PdfReader(f)        
            # search for keywords
            for i in range(object.numPages):
                page = object.pages[i]
                text = page.extract_text()
                search_text = text.lower().split()
                print(search_text)
                for word in keywords:
                    if word in search_text:
                        print("The word '{}' was found in '{}'".format(word, filename)) 