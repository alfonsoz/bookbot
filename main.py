from stats import word_count, get_book_text

def main():
    book = get_book_text('books/frankenstein.txt')
    num_words = word_count(book)
    print(f"Found {num_words} total words")


main()