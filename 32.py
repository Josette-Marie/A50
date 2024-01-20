# Capitalize first letters of each words in the array
    
def capitalize_first_letters(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Example usage
input_text = "this is an example sentence with words"
capitalized_text = capitalize_first_letters(input_text)
print("Capitalized text:", capitalized_text)
