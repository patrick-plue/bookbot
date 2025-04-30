from stats import count_words, count_characters, sort_dictionaries

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    content = get_book_text(path)
    num_words = count_words(content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    count_char = count_characters(content)
    sorted_count_char = sort_dictionaries(count_char)

    print("--------- Character Count -------")
    for x in sorted_count_char:
        for key, value in x.items():
            if(key.isalpha() ):
                print(f"{key}: {value}")

    print("============= END ===============")
        


main()