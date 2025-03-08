# -*- coding: UTF-8 -*-

import csv
import datetime
import dblp
import operator
import pickle
import os

authors = {}

# Load the existing authors if they exist
if os.path.exists("authors.data"):
    authors_file = open("authors.data", 'rb')
    authors = pickle.load(authors_file)

print(len(authors))

# Update from the CSV
with open('faculty-affiliations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        authors[row['name'].strip()] = row['affiliation'].strip()

if os.path.exists("authors.data"):
    authors_file.close()

# write new authors file
authors_file = open("authors.data", 'wb')
pickle.dump(authors, authors_file)
authors_file.close()
