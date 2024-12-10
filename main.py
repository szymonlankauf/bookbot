import sys

def main ():
  sys.set_int_max_str_digits(0)
  with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words_count = count_words(file_contents)
    letters_counter = count_letters(file_contents)
    sorted_list = characters_sorted(letters_counter)
    print_letters_count(sorted_list, words_count)
    

def count_words (text):
  words = text.split()
  return len(words)

def count_letters (text):
  counter = {}
  text = text.lower()
  for c in text:
    if c in counter:
      counter[c] += 1
    else:
      counter[c] = 1
  return counter

def sort_by_num(dict):
  return dict["num"]

def characters_sorted(letters_count):
  sorted_list = []
  for char in letters_count:
    if (char.isalpha()):
      new_char_dict = {
        "char": char,
        "num": letters_count[char]
      }
      sorted_list.append(new_char_dict)
      sorted_list.sort(reverse=True, key=sort_by_num)
  return sorted_list

def print_letters_count(letters_list, words_count):
  print('--- Begin report of books/frankenstein.txt ---')
  print(f'{words_count} words found in the document')
  print()
  for letter in letters_list: 
    print(f"The '{letter["char"]}' character was found  {letter["num"]} times")
  print('--- End report ---')

main()