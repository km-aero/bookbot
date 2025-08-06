def count_book_words(text):
  return len(text.split())

def desc_sort(dict):
  return dict["num"]

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def sorted_dict(dict):
  sorted_dict = []

  for key in dict.keys():
    if key.isalpha():
      sorted_dict.append({"char": key, "num": int(dict[key])})

  sorted_dict.sort(reverse=True, key=desc_sort)
  
  return sorted_dict

def count_unique_chars(text):
  lower_book = text.lower()
  unique_char_count = {}

  for char in lower_book:
    # if character in unique_char_count add 1 to char
    if char in unique_char_count.keys():
      unique_char_count[char] += 1
    # else set to 1
    else:
      unique_char_count[char] = 1
  return unique_char_count
