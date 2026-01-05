from stats import word_count, get_book_text, letter_count, sort_dict
#for using command line arguments, import sys
import sys

def main():
    if len(sys.argv) == 2:
        #use second argument of input as path (python3 main.py <path>)
        BOOK_PATH = sys.argv[1]

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
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()