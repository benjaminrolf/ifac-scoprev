import pandas as pd
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

'''matches the bibtex files with the excel export of Scopus and Web of Science
   and adds a column with the corresponding bibtex key to the csv file'''

# read excel and bibtex files
pubs = pd.read_csv('0_resources/publications.csv')

with open('0_resources/export/Scopus_Bib_Export.bib', encoding='utf8') as f:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    scopus_bib = bibtexparser.load(f, parser=parser)

with open('0_resources/export/WoS_Bib_Export.bib', encoding='utf8') as f:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    wos_bib = bibtexparser.load(f, parser=parser)

# dict for databases
DATABASES = {scopus_bib: 'Scopus', wos_bib: 'Web of Science'}

# iterate scopus and web of science bibtex entries
for database in DATABASES.items():
    for entry in database[0].entries_dict:

        # match by DOI or by title and find index
        try:
            doi = database[0].entries_dict[entry]['doi']
            idx = pubs.index[pubs['DOI'] == doi].to_list()
        except:
            title = database[0].entries_dict[entry]['title']
            idx = pubs.index[pubs['Article Title'] == title].to_list()

        source = database[1]

        # write bibtex key in dataframe
        for val in idx:
            if pubs.at[val, 'Source'] == source:
                pubs.at[val, 'Bibtex Key'] = entry

# export excel file
pubs.to_csv('0_resources/publications.csv')