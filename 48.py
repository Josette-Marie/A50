# largest word in a text
def longest_word(text):
  longest_word = ""
  for word in text.split():
    if len(word) > len(longest_word):
      longest_word = word

  return longest_word

text = "This is a sentence with some words of varying lengths."
longest_word = longest_word(text)

print(longest_word)
