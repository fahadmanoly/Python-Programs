import enchant

def spelling_check(word):
    dictionary = enchant.Dict("en_US")
    if not word.isalpha():
        print(word)
        return word
    if not dictionary.check(word):
        spel = dictionary.suggest(word)
        if spel:
            correct_word = spel[0]
            return correct_word
        else:
            return word
    else:
        return word

# def correct_document(document_path):
#     with open(document_path, 'r') as file:
#         document = file.read()
    
#     words = document.split()
#     corrected_words = [spelling_check(word) for word in words]
    
#     corrected_document = ' '.join(corrected_words)
    
#     return corrected_document

# # Use the function
# document_path = "C:/Users/pro/Desktop/test_document.txt"
# corrected_document = correct_document(document_path)

# def correct_spelling_in_document(document_path):
#     dictionary = enchant.Dict("en_US")  # US English dictionary
#     with open(document_path, 'r') as file:
#         document = file.read()
#     words = document.split()  # split the document into words
#     corrected_words = []
#     for word in words:
#         corrected_word = spelling_check(word)  # use the spelling_check function
#         corrected_words.append(corrected_word)
#     corrected_document = ' '.join(corrected_words)  # join the corrected words back into a document
#     return corrected_document

def correct_spelling_in_document(document_path):
    dictionary = enchant.Dict("en_US")  # US English dictionary
    with open(document_path, 'r') as file:
        document = file.read()

    corrected_document = ""
    word_start = 0
    for i, char in enumerate(document):
        if char.isspace():
            word = document[word_start:i]
            corrected_word = spelling_check(word)  # use the spelling_check function
            corrected_document += corrected_word + char
            word_start = i + 1
        elif i == len(document) - 1:  # last word in the document
            word = document[word_start:]
            corrected_word = spelling_check(word)
            corrected_document += corrected_word
    return corrected_document

path = "C:/Users/pro/Desktop/test_document.txt"
correct_doc = correct_spelling_in_document(path)

print(correct_doc)