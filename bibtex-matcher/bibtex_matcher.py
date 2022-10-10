import pandas as pd
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


# read excel and bibtex files
pubs = pd.read_excel('publications_review.xlsx')
with open('bibtex-matcher/Scopus_Bib.bib', encoding='utf8') as f:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    scopus_bib = bibtexparser.load(f, parser=parser)

with open('bibtex-matcher/WoS_Bib.bib', encoding='utf8') as f:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    wos_bib = bibtexparser.load(f, parser=parser)

# iterate scopus bibtex entries
for entry in scopus_bib.entries_dict:

    # match by DOI or by title
    try:
        doi = scopus_bib.entries_dict[entry]['doi']
        idx = pubs.index[pubs['DOI'] == doi].to_list()
    except:
        title = scopus_bib.entries_dict[entry]['title']
        idx = pubs.index[pubs['Article Title'] == title].to_list()

    # find indices in dataframe


    # write bibtex key in dataframe
    for val in idx:
        pubs.at[val, 'Bibtex Key'] = entry

# write excel
pubs.to_excel('pubs.xlsx')

# filter relevant publications
#pubs_include = pubs[pubs['Stage 2 Decision'] == 'include']
#print(pubs.head())