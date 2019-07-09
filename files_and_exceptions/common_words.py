def word_count(file_to_analyze, words_to_search_for) :
  """Count how many times a set of words appear in a txt file"""
  with open(file_to_analyze, 'r+') as f :
    text = f.read()
    for word in words_to_search_for :
      appearances = text.count(word)
      print(f"The word '{word}' appears {appearances} times in {file_to_analyze}")


print("enter q to quit at any time.")
print('Welcome to Common Word Counter v-0.0.1\nThis program will count how many times the')
print('ten most common words in English appear in a text.')
print('Make sure the file you want to check is in the same directory as this one.')
common_words = ['the ', 'be ', 'to ', 'of ', 'and ', 'a ', 'in ', 'that ', 'have ', 'I ']
while True:
  file_name = input('Enter the name of the file you would like to check (Hint: you better put the extension, too!):\n')
  if file_name == 'q' :
    break
  else :
    try :
      word_count(file_name, common_words)
    except FileNotFoundError :
      print(f"Hey, the file {file_name}, wasn't found in this directory. Make sure the file is in the directory and you've inputted it's name correctly.")

