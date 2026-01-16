# Counting Tokens – SFWRENG 4NL3 A1

---

## Files

normalize_text.py  
Main Python script that performs preprocessing, token counting, and visualization.

Frankenstein.txt  
Input text used for the assignment. The text was obtained from Project Gutenberg.

README.md  
Instructions for running the program and documentation of AI usage.

---

## Requirements

Python version 3.14 or higher

The following libraries are required depending on which preprocessing options are used:

matplotlib  
scikit-learn (required only when using stopword removal)  
nltk (required only when using stemming or lemmatization)

---

## How to Run

To run the program, execute the Python script and provide the path to a text file as the first argument.

Example usage:

python normalize_text.py Frankenstein.txt

---

## Optional Preprocessing Flags

The script supports multiple preprocessing options that can be enabled simultaneously.

-lowercase  
Converts all tokens to lowercase in order to reduce sparsity caused by capitalization.

-stopwords  
Removes common English stopwords using a predefined stopword list.

-stem  
Applies Porter stemming to reduce words to their stem forms. This option requires nltk.

-lemmatize  
Applies WordNet lemmatization to reduce words to their base lemma. This option requires nltk and WordNet data, which is downloaded automatically by the script.

-removegutenberg  
Removes the Project Gutenberg header and footer, which contain licensing and metadata text unrelated to the novel’s narrative content.

Example using multiple options:

python normalize_text.py Frankenstein.txt -lowercase -stopwords -removegutenberg

---

## AI Usage and Attribution

AI assistance was used in the following ways during development:

- Creation of the regular expression used to extract tokens from text  
- Creation of the regular expressions used to identify and remove Project Gutenberg header and footer text  
- Assistance with the approach for converting a list of tokens into a frequency mapping and sorting the results by frequency
- Creation of README.md file 

CO2 Emissisions = 4.32g*4 = 17.28g
---
