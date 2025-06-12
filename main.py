def get_book_text(books):
    with open(books, 'r', encoding='utf-8') as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
