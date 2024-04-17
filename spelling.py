import enchant
import re


def spelling_check(word):
    dictionary = enchant.Dict()
    if not word.isalpha():
        raise ValueError("word should only contain alphabets")
    if not dictionary.check(word):
        spel = dictionary.suggest(word)
        if spel:
            correct_word = spel[0]
            return correct_word
        else:
            return word
    else:
        return word

def check_spelling_document(document_path):
    with open(document_path, 'r') as f:
        content = f.read()
        # Replace found incorrect words with correct ones
        corrected_content = re.sub('[a-zA-Z]+', lambda match: spelling_check(match.group(0)), content)
        return corrected_content

# Test the function with a file path
document_path = "C:/Users/pro/Desktop/test_document.txt"
corrected_content = check_spelling_document(document_path)
print(corrected_content)
# Save the corrected content to a new file
with open('corrected_document.txt', 'w') as f:
    f.write(corrected_content)