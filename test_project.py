from project import Character_extractor, special_chars, to_excel, extract_text


def main():
    test_format()
    test_columns()
    test_special()


def test_format():
    #Checking if it will raise an error in case of receiving a wrong type of format
    try:
        extract_text("Book1.xlsx")
    except ValueError:
        pass
    else:
        assert False, "Function extract_text did not raise a ValueError"

def test_columns():
    #Checking if the columns are correct
    file_path = "test_text.txt"
    book_extractor = Character_extractor(file_path)
    book_extractor.process_text()
    df = to_excel(book_extractor, "no")
    set_check = {"words", "special characters", "URLs"}.issubset(set(df.columns))
    assert set_check == True

def test_special():
    #Checking for the returning of specials when the user doesn't want any
    assert special_chars("no") == ""

if __name__ == "__main__":
    main()

