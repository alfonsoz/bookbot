#open and return book text from specified path
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count words in text
def word_count(text):
    return len(text.split())




def main():
    book = get_book_text('books/frankenstein.txt')
    num_words = word_count(book)
    print(f"Found {num_words} total words")


main()