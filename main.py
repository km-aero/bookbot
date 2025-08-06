from stats import count_book_words, count_unique_chars, get_book_text, sorted_dict
import sys

args = sys.argv

if len(args) != 2:
  print("Usage: python3 main.py <path_to_book>")
  exit(1)

def main():
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  text = get_book_text(args[1])
  num_words = count_book_words(text)

  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  unique_char_dict = count_unique_chars(text)
  character_count = sorted_dict(unique_char_dict)

  for char in character_count:
    print(f"{char["char"]}: {char["num"]}")

  print("============= END ===============")

main()