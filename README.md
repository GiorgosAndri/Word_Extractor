# Word Extractor

#### Video demo: <https://www.youtube.com/watch?v=mYQbHi4-GkA>
#### Description: Aprogram that extracts words and other various elements from a given text file.

## Overview
#### This is mu final project of CS50P. Word Extractor is a program that extracts various elements from a given text file. It supports plain text, PDF, and Word document formats. The primary features include extracting individual words, special words or features chosen by the user, special characters, and URLs. The extracted data are processed and exported to an Excel file.

### Libraries required:
#### pandas, pdfminer.six, python-docx, collections, re

### Usage

#### Run the program with the bash script python project.py.

#### Provide the program with the path to the text file, PDF, or Word document.

#### Provide Special Characters, Phrases and Words that you want to be searched. Press Control+D when you're done.

#### Download the excel output extracted_characters, which contains all of the words, URLs, special characters
#### and special words if you have given any.


## Test Program


#### Execute the test program test_project.py to ensure the functionality of key components:

#### test_format: Checks if an error is raised for an unsupported file format.
#### test_columns: Verifies the correctness of the Excel columns.
#### test_special: Ensures the correct handling when user doesn't want any special characters and words.


#### Requirements
### Python 3.x
### pandas
### pdfminer.six
### python-docx