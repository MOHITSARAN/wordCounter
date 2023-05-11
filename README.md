# Word Counter

Problem statement:

Write a command line program in Python that accepts as input a filename of common words and a filename of text that outputs the word counts of the text after the common words are removed sorted by count descending and formatted nicely.

Example Output:
Alice: 10000\
Foo: 50\
Bar: 40\
Baz: 10

Solution:

Read File give by the user\
Turn all the letters of document into lower case\
Cleaning and Extracting words from text & avoiding words like in, be, or, the etc (Use Regex)\
Exclude Specific Common word from Document (alice)\
Sorting dictionary by descending order\
Write output in file with all the words\
Print all the words where count is > 3

Usage via Command line you have two options

## Read file from arguments:

- `python3 uncommonwords.py common.txt alice.txt`

## Read file from user input:

- `python3 uncommonwords.py`

#### Enter Common file name example: common.txt

#### Enter Document file name example: alice.txt

## Added Unit Test On File Operation

- `python3 -m unittest unit_test.py`

## Run via Docker

- `docker image build -t wordcounter .`
- `docker run wordcounter`

## Output will be shows in two ways:

## 1. On console/terminal all the words which has repeated more then 3 times and most frequent words on the top!

## 2. It will write overall result to > output.txt
