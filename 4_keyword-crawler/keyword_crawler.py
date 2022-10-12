import os
import pandas as pd
import pdfplumber

''''''

### SETTINGS ###
# saves pages with marked search results as images
SAVE = True
PATH = 'C:/Users/benja/Documents/Python Projects/ifac-scoprev/keyword-crawler/library'
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
                hits = page.search('gnn model', case=False)
                search_results.extend(hits)

                # save marked pages as images
                if SAVE:
                    if len(hits) > 0:
                        im = page.to_image(resolution=150)
                        im.draw_rects(hits)
                        im.save('keyword-crawler/results/{key}_page_{page_num}.png'.format(
                            key = filename[:-4],
                            page_num = page.page_number
                            ), format='PNG')

    # print search results
    print('Found {num} occurences of *{keyword}* in {publication}!'.format(
        num = len(search_results),
        keyword = KEYWORDS[0],
        publication = filename
        ))