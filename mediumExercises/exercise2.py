# Build a simple text analyzer. Problem: Write a function count_words(text) that:

# Accepts a paragraph of text
# Returns a dictionary where keys are words and values are how many times they appeared (case-insensitive)
# Example input: | text = "AI is the future. The future is now."

# Expected Output: {'ai': 1, 'is': 2, 'the': 2, 'future': 2, 'now.': 1}

#Solution
def textAnalyser(theText: str()):
    words=[word.replace('.', '') for word in theText.lower().split()]
    word_dict = {word:0 for word in words}
    for word in word_dict:
        for wd in words:
            if (word==wd):
                word_dict[word]=word_dict[word]+1
    print(word_dict)
textAnalyser("AI is the future. The future is now.")
