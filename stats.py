#open and return book text from specified path
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count words in text
def word_count(text):
    return len(text.split())

#count amount of duplicate letters in text, return value = dictionary
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

#helper function to sort items
def sort_on(items):
    return items["num"]

#sort input dictionary, return value = list
def sort_dict(dictionary):
    sorted = []    
    for key in dictionary:
        sorted.append({"char":key, "num":dictionary[key]})
    #sort list
    sorted.sort(reverse=True, key=sort_on)

    return sorted

