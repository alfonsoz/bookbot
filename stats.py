#open and return book text from specified path
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count words in text
def word_count(text):
    return len(text.split())
