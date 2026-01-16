import re
import argparse
import matplotlib.pyplot as plt
from collections import Counter

# Used llm for regex
TOKEN_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")

# Used llm for regex
GUTEN_START_RE = re.compile(
    r"\*\*\*\s*START OF THE PROJECT GUTENBERG EBOOK.*?\*\*\*",
    re.IGNORECASE | re.DOTALL
)

# Used llm for regex
GUTEN_END_RE = re.compile(
    r"\*\*\*\s*END OF THE PROJECT GUTENBERG EBOOK.*?\*\*\*",
    re.IGNORECASE | re.DOTALL
)

def tokenize(text):
    return TOKEN_RE.findall(text)

def strip_gutenberg(text):
    start = GUTEN_START_RE.search(text)
    if start:
        text = text[start.end():]

    end = GUTEN_END_RE.search(text)
    if end:
        text = text[:end.start()]

    return text

def main():
    parser = argparse.ArgumentParser(description='Normalize and count tokens')

    parser.add_argument("filepath", type=str, help="Path to input text file")
    parser.add_argument("-lowercase", action="store_true", help="Lowercase tokens")
    parser.add_argument("-stem", action="store_true", help="Apply stemming")
    parser.add_argument("-lemmatize", action="store_true", help="Apply lemmatization")
    parser.add_argument("-stopwords", action="store_true", help="Remove stopwords")
    parser.add_argument("-removegutenberg", action="store_true", help="Remove Gutenberg header and footer")

    args = parser.parse_args()

    with open(args.filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if args.removegutenberg:
        text = strip_gutenberg(text)

    tokens = tokenize(text)

    if args.lowercase:
        tokens = [t.lower() for t in tokens]

    if args.stem:
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
    
    if args.lemmatize:
        import nltk
        nltk.download("wordnet", quiet=True)
        nltk.download("omw-1.4", quiet=True)
        from nltk.stem import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
    
    if args.stopwords:
        from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
        stop = set(ENGLISH_STOP_WORDS)
        tokens = [t for t in tokens if t not in stop]

    
    # used llm to take list of tokens and get {token: frequency}
    counts = Counter(tokens)
    sorted_tokens = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    print(f"{'TOKEN':<20}COUNT")
    print("-" * 26)

    for token, count in sorted_tokens:
        print(f"{token:<20}{count}")

    frequencies = [count for _, count in sorted_tokens]
    ranks = list(range(1, len(frequencies) + 1))

    plt.figure(figsize=(8, 5))
    plt.bar(ranks, frequencies)

    plt.xscale("log")
    plt.yscale("log")

    plt.title("Token Rank vs Frequency (Log-Log Scale)")
    plt.xlabel("Rank")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()