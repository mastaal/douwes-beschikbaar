# douwes-beschikbaar
Python script to check if a book is available on boekhandeldouwes.nl, using an
ISBN and/or a book title, either from input or .csv file.

Includes a tkinter GUI.

# Usage

For this program, you need a .csv file with ISBN and book titles in the following
format:

```
ISBN,title
ISBN,"title with spaces"
```

The path in this file has to be specified by setting the "book_file" variable
accordingly.

## douwes_beschikbaar.py

```
douwes_beschikbaar.py ISBN
```

If you ommit specifying an ISBN in your call, you will be prompted to enter one.

## douwes_beschikbaar_gui.py

Execute the program, fill in an ISBN and hit "Zoeken". A result will be printed
on the window within a few moments.
