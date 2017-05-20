#!/usr/bin/python3

"""
check_available.py:
    Python script to check if a book is available on boekhandeldouwes.nl, using
    ISBN and/or a book title, either from input or .csv file.

Copyright 2017 Martijn Staal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import csv
import urllib.request
import sys
import re

book_file = "uitverkochte_titels.csv"
isbn_dict = {}

#availability_regex = re.compile("class=\"col-md-4 book-highlight-price\".{500}")
availability_regex = re.compile("Niet leverbaar")

def init_dict(book_file_name):
    """Initialize isbn_dict dictionary"""
    with open(book_file) as csvf:
        creader = csv.reader(csvf, delimiter=',')
        for row in creader:
            try:
                isbn_dict[row[0]] = row[1]
            except:
                pass

def gen_url(isbn):
    """Generate boekhandeldouws.nl url for given isbn"""
    try:
        book = isbn_dict[isbn]
    except:
        raise Exception("Non-defined ISBN")
    return "https://www.boekhandeldouwes.nl/boek/" + isbn + "-" + book.replace(' ', '-')

def check_available(isbn):
    """Check if isbn is available"""
    url = gen_url(isbn)
    print(url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        if availability_regex.search(str(html)) != None:
            print("Niet leverbaar")
        else:
            print("Leverbaar")

init_dict(book_file)
if len(sys.argv) > 1:
    check_available(sys.argv[1])
else:
    check_available(input("ISBN = "))
