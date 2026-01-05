#open and return book text from specified path
def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book = get_book_text('books/frankenstein.txt')
    print(book)


main()