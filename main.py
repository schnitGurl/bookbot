def get_book_text(books):
    with open(books, 'r', encoding='utf-8') as f:
        return f.read()
    
from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()
