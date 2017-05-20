#!/usr/bin/python3

"""
douwes_beschikbaar.py:
    Python script to check if a book is available on boekhandeldouwes.nl, using
    ISBN and/or a book title, either from input or .csv file.

    Copyright 2017 Martijn Staal                                               
                                                                               
    This file is part of douwes-beschikbaar.                                   
                                                                               
    douwes-beschikbaar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
                                                                               
    douwes-beschikbaar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with douwes-beschikbaar.  If not, see <http://www.gnu.org/licenses/>.
"""

import csv
import urllib.request
import sys
import re

book_file = "uitverkochte_titels.csv"
isbn_dict = {}

not_available_regex = re.compile("Niet leverbaar")
available_regex = re.compile("voorraad|levertijd")

def check_isbn(isbn):
    """Check if isbn is a valid 13-digit ISBN"""
    if len(isbn) != 13:
        return False

    # Verify ISBN check digit
    given_check_digit = int(isbn[12])
    digit_sum = 0
    i = 0
    while i < 12:
        if (i % 2) != 0:
            digit_sum = digit_sum + 3*int(isbn[i])
        else:
            digit_sum = digit_sum + int(isbn[i])
        i = i + 1
    check_digit = 10 - (digit_sum % 10)
    if check_digit == 10:
        check_digit = 0

    if given_check_digit == check_digit:
        return True
    else:
        return False

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
        raise Exception("ISBN is not defined in isbn_dict")
    return "https://www.boekhandeldouwes.nl/boek/" + isbn + "-" + book.replace(' ', '-')

def check_available(isbn):
    """Check if isbn is available"""
    if check_isbn(isbn):
        pass
    else:
        raise Exception("Invalid ISBN supplied")
    url = gen_url(isbn)
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            if available_regex.search(str(html)) != None:
                # Book is available
                return (True, 0)
            else:
                # Check to be sure that it's not available
                if not_available_regex.search(str(html)) != None:
                    # Book is not available
                    return (False, 0)
                else:
                    return (True, 1)
    except urllib.error.HTTPError:
        # There's an error with locating the book on the website, thus it either
        # doesn't exist or the information in the database is wrong.
        print("HTTPError!")
        return (False, -1)

if __name__ == "__main__":
    init_dict(book_file)
    book = ""
    if len(sys.argv) > 1:
        book = sys.argv[1]
    else:
        book = input("ISBN = ")
    print(check_available(book))
