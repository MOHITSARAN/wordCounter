import re
import sys
from utils import fileReaderHandler, fileWriterHandler

# arguments
files_in_args = len(sys.argv)

# Check if user pass file via arguments or Input
if files_in_args == 3:
    # Taking file from argument
    common_file = sys.argv[1]
    document_file = sys.argv[2]

else:
    # Taking file from user input
    common_file = input("Enter Common file name example: common.txt\n")
    document_file = input("Enter Document file name example: alice.txt\n")

# Just Handling the files should be in a correct format
if common_file.endswith('.txt') and document_file.endswith('.txt'):
    print("Files submitted by user", common_file, document_file)
else:
    print("Error: Files submitted by user is an unknown file format. Please provied file in .txt format.")
    sys.exit()

# Opening reading and closing file
common_file_content = fileReaderHandler(common_file)
document_file_content = fileReaderHandler(document_file)

# Making a set of common words as searching in set is faster
try:
    common_words_list = set(common_file_content.split("\n"))
except Exception as e:
    print('Error: Error occurred while splitting:', e)

# Cleaning and Extracting words from text & avoiding words like in, be, or, the etc
try:
    document_file_content = re.sub('[?|$|.|!]', ' ', document_file_content)
    document_words_list = re.findall(
        r'\b[a-z]{3,15}\b', document_file_content)
except Exception as e:
    print('Error: Error occurred while cleaning and extracting words:', e)

# Inserting uncommon words with count in dictionary
try:
    unsorted_dict = dict()
    for word in document_words_list:
        if word not in common_words_list:
            count = unsorted_dict.get(word, 0)
            unsorted_dict[word] = count + 1

    # Sorting dictionary by descending order
    sorted_dict = dict(
        sorted(unsorted_dict.items(), key=lambda count: count[1], reverse=True))
except Exception as e:
    print('Error: Error occurred while creating dictionary:', e)

# Write output in file with all the words
fileWriterHandler(sorted_dict)

# Print all the words where count is > 3
for words in sorted_dict.keys():
    if sorted_dict[words] > 3:
        print(words, ":", sorted_dict[words])

print("\nCheck output.txt file to see how many words are there overall :)\n")
