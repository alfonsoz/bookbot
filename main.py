from stats import word_count, get_book_text, letter_count

def main():
    book = get_book_text('books/frankenstein.txt')
    num_words = word_count(book)
    print(f"Found {num_words} total words")
    lettercount = letter_count(book)
    print(f"Letter count: {lettercount}")


main()