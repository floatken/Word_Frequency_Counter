import os

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def remove_punctuation(text):
    for char in text:
        if char in punc:
            text = text.replace(char, "")
    return text

def count_word_frequency(text):
    wordcount = {}
    lowered = text.lower()
    for word in lowered.split():
        wordcount[word] = wordcount.get(word, 0) + 1
    return wordcount

def display_top_words(wordcount):
    descending_wordcount = {k: v for k, v in sorted(wordcount.items(), key=lambda item: item[1], reverse=True)}
    total_words = len(descending_wordcount)
    top20 = total_words // 5
    top20_words = list(descending_wordcount.items())[:top20]
    for key, value in top20_words:
        print(key, value)

while True:
    file = input("Enter the filename: ")
    if not os.path.isfile(file):
        print("Error: File not found. Please enter a valid filename.")
        continue

    with open(file, 'r') as f:
        content = f.read()

    content = remove_punctuation(content)
    wordcount = count_word_frequency(content)
    display_top_words(wordcount)
