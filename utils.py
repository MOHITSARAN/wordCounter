import os
import sys


# To get the current working directory
directory = os.getcwd()

# Check file is empty or not
def checkFileIsEmpty(file) -> str:
    if os.path.getsize(file) == 0:
        print("Error: The file %s is empty:" % (file))
        sys.exit()
    else:
        return file


# Check file is on correct path or not
def fileReaderHandler(file) -> str:
    try:
        isFile = checkFileIsEmpty(file)
        file = open(directory + '/' + isFile, "r")
        # convert all the words in lowercase which is easier to apply regular expression
        contents = file.read().lower()
        file.close()
        return contents
    except IOError:
        print("Error: The file %s provided does not appear to exist at the location: %s" % (
            file, directory))
        sys.exit()


# Write the output into the file.
def fileWriterHandler(sorted_dict):
    # Saving the reference of the standard output
    original_stdout = sys.stdout
    try:
        output_file = open(directory + '/' + "output.txt", "w")
        sys.stdout = output_file
        for words in sorted_dict.keys():
            print(words, ":", sorted_dict[words])
        sys.stdout = original_stdout
        output_file.close()
    except IOError:
        print("Error: The file output.txt provided does not appear to exist at the location: %s" % (
            directory))
        sys.exit()
