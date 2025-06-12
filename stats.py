def get_num_words(text):
    word_count = text.split()
    return len(word_count)

def get_char_count(text):
    char_count = {}  # Dictionary to store character -> count

    for char in text.lower():  # Convert to lowercase for consistency
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count  # Return the dictionary of counts

def sort_char_counts(char_count):
    """Takes a character count dictionary and returns a sorted list of dictionaries."""
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    
    # Sort list by count in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    return char_list