import pandas as pd


'''aggregates the exports from Scopus and Web of Science in a single file and
   drops duplicates'''

# import publications
scopus = pd.read_csv('0_resources/export/Scopus_Export.csv')
wos = pd.read_csv('0_resources/export/WoS_Export.csv')

# create empty dataframe for publications
pubs = pd.DataFrame(
    columns=[
        'DOI', 'Year', 'Authors', 'Article Title', 'Source Title', 'Volume',
        'Issue', 'Start Page', 'End Page', 'Keywords','Times cited',
        'Affiliations', 'Abstract', 'Link', 'Source'
    ])

# add scopus publications to pubs
for index, row in scopus.iterrows():
    pubs = pubs.append(
        {
            'DOI': row['DOI'],
            'Year': row['Year'],
            'Authors': row['Authors'],
            'Article Title': row['Title'],
            'Source Title': row['Source title'],
            'Volume': row['Volume'],
            'Keywords': row['Author Keywords'],
            'Issue': row['Issue'],
            'Start Page': row['Page start'],
            'End Page': row['Page end'],
            'Affiliations': row['Affiliations'],
            'Times cited' : row['Cited by'],
            'Abstract': row['Abstract'],
            'Link': row['Link'],
            'Bibtex Key': 'None',
            'Source': 'Scopus'
        },
        ignore_index=True)

# add wos publications to pubs
for index, row in wos.iterrows():
    pubs = pubs.append(
        {
            'DOI': row['DOI'],
            'Year': row['Publication Year'],
            'Authors': row['Authors'],
            'Article Title': row['Article Title'],
            'Source Title': row['Source Title'],
            'Volume': row['Volume'],
            'Keywords': row['Author Keywords'],
            'Issue': row['Issue'],
            'Start Page': row['Start Page'],
            'End Page': row['End Page'],
            'Affiliations': row['Affiliations'],
            'Times cited' : row['Times Cited'],
            'Abstract': row['Abstract'],
            'Link': row['DOI Link'],
            'Bibtex Key': 'None',
            'Source': 'Web of Science'
        },
        ignore_index=True)


# remove duplicates
pubs = pubs.drop_duplicates(subset=['DOI', 'Article Title'], keep='first')

# print statistics
print('Number of Publications in Scopus: ', len(scopus))
print('Number of Publications in Web of Science: ', len(wos))
print('Number of Publications without Duplicates: ', len(pubs))
print('Number of Duplicates: ', len(scopus) + len(wos) - len(pubs))

# create csv file
pubs.to_csv('0_resources/publications.csv', index=False)