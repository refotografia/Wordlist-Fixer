with open('file.txt', mode='r') as file:
  word_list = file.readlines()

for l_word in word_list:
  word = ("".join(l_word)).strip()
  if len(word.strip()) < 8 or len(word.strip()) > 10:
    pass
  else:
    with open('words.txt', mode='a') as destination:
      destination.write(f"{word}\n")
