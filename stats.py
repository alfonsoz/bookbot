#open and return book text from specified path
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count words in text
def word_count(text):
    return len(text.split())

#count amount of duplicate letters in text
def letter_count(text):
    letter_dict = {}
    #lowercase for every char
    lowercase_text = text.lower()
    for letter in lowercase_text:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

