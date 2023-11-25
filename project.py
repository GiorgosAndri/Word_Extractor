import re
from collections import Counter
import docx
from pdfminer.high_level import extract_text as pdf_extract_text
import pandas as pd


#Hello, let's take a quick look at the program

#Creation of Character_extractor class
class Character_extractor:
    def __init__(self, file_path, specials=""):
        self.file_path = file_path
        self.words = []
        self.special_words = []
        self.special_characters = []
        self.urls = []
        #words chosen by the user to be checked if they are in the text
        self.specials = specials


    def extract_words(self, text):

        #Extracts individual words from the text.

        words = re.findall(r'\b(?![0-9\W_])\w+\b', text.lower())
        self.words = words


    def extract_special_words(self, text):

        #Detects and extracts special words or features that the user chose.

        special_ws = re.findall(r'\b('+self.specials+')\s+\w+', text)
        self.special_words = special_ws

    def extract_special_characters(self, text):

        #Identifies and lists special characters that appear in the text.

        special_chars = re.findall(r'[^a-zA-Z0-9\s]', text)
        special_char_counts = Counter(special_chars)
        self.special_characters = special_char_counts

    def extract_urls(self, text):

        #Extracts URLs from the text.

        urls = re.findall(r'https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+(?:/\S*)?', text)
        self.urls = urls


    def process_text(self):

        #Main method to process the functions and extract words, chaacters and specials.

        text = extract_text(self.file_path)
        self.extract_words(text)
        self.extract_special_words(text)
        self.extract_special_characters(text)
        self.extract_urls(text)

def extract_text(file_path):
        #Extracts text from different file formats: plain text, PDF, and Word documents.

        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif file_path.endswith('.pdf'):
            pdf_text = pdf_extract_text(file_path)
            return pdf_text
        elif file_path.endswith('.docx'):
            doc = docx.Document(file_path)
            return "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            raise ValueError("Unsupported file format")


def special_chars(answer=""):
    #Asking the user if they want any special words, phrases or characters to be searched
    while answer.lower() not in ["yes", "no", "y", "n"]:
        answer = input("Do you want to look fo specific words or chaacters?(yes/no): ")
    if answer in ["yes", "y"]:
        specials = []
        while True:
            try:
                specials.append(input("Insert special word or character: "))
            except EOFError:
                if len(specials) > 0:
                    return "|".join(specials)
    else:
     return ""

def to_excel(dataset, export = "yes"):
    #Creating a dataframe to create the excel. We give it the option to not create one
    #and return the dataframe for testing reasons
    if len(dataset.specials) == 0:
        data = {"words": sorted(list(set(dataset.words))), 'URLs': sorted(list(set(dataset.urls))),
                "special characters": sorted(list(set(dataset.special_characters)))}
    else:
        data = {"words": sorted(list(set(dataset.words))), 'URLs': sorted(list(set(dataset.urls))),
                "special characters": sorted(list(set(dataset.special_characters))),
                "special words":sorted(list(set(dataset.special_words)))}

    series_list = [pd.Series(value, name=key) for key, value in data.items()]
    df = pd.concat(series_list, axis=1)
    if export == "yes":
        df.to_excel('extracted_characters.xlsx', index=False)
    return df
#Thanks for watching!
def main():
    file_path = input("insert text file path: ")
    book_extractor = Character_extractor(file_path)
    book_extractor.specials = special_chars()
    book_extractor.process_text()
    to_excel(book_extractor)

if __name__ == "__main__":
    main()