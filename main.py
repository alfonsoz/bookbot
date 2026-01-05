from stats import word_count, get_book_text, letter_count, sort_dict

BOOK_PATH = 'books/frankenstein.txt'

def main():
    book = get_book_text(BOOK_PATH)
    #total amount of words
    num_words = word_count(book)
    #lettercount is a dictionary with characters and the amount of characters in the text
    lettercount = letter_count(book)
    #sorted output is a list with every lettercount item, but sorted from highest to lowest
    sorted_output = sort_dict(lettercount)

    #output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {BOOK_PATH}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #show sorted items as a readable list
    for item in sorted_output:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()