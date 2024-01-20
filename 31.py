# Number of word in the text 

def count_words(text):
    words = text.split()
    return len(words)

# Example usage
input_text = "This is an example sentence with seven words in it"
word_count = count_words(input_text)
print("Number of words:", word_count)
