import os
import pandas as pd
import pdfplumber


### SETTINGS ###
# saves pages with marked search results as images
SAVE = False
PATH = 'C:/Users/benja/Documents/ifac-scoprev/keyword-crawler/library'
KEYWORDS = ['artificial intelligence']

# read csv file
pubs = pd.read_csv('publications.csv')

# initialize list for search results
search_results = []

# loop through pdf files
for filename in os.listdir(PATH):
    if filename.endswith('.pdf'):

        # open the pdf file
        with open(os.path.join(PATH, filename), 'rb') as f:
            pdf = pdfplumber.open(f)

            # loop through the pages and search for keywords
            for page in pdf.pages:
                hits = page.search('graph', case=False)
                search_results.extend(hits)

                # save marked pages as images
                if SAVE:
                    im = page.to_image(resolution=150)
                    im.draw_rects(hits)
                    im.save('page_{}.png'.format(page.page_number), format='PNG')

    # print search results
    print('Found {num} occurences of *{keyword}* in {publication}!'.format(
        num = len(search_results),
        keyword = KEYWORDS[0],
        publication = filename
        ))