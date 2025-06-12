from stats import get_num_words, get_char_count, sort_char_counts

def get_book_text(books):
    with open(books, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text) #Get word count
    char_count = get_char_count(book_text) #Get char count
    sorted_char_list = sort_char_counts(char_count) #convert dict to sorted list of char freqs
   
       # Print formatted report
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {book_path}...\n")

    print("-" * 11 + " Word Count " + "-" * 11)
    print(f"Found {word_count} total words\n")

    print("-" * 10 + " Character Count " + "-" * 10)

    # Print only alphabetical characters in descending order of frequency
    for entry in sorted_char_list:
        char = entry["char"]
        if char.isalpha():  # Skip non-alphabetical characters
            print(f"{char}: {entry['num']}")

    print("=" * 12 + " END " + "=" * 12)

if __name__ == "__main__":
    main()
