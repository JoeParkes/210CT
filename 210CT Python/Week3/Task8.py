word = str(input("What is your word?: "))

def remove_vowels(word):

    """Recursively remove vowels from the input."""
    if not word: # empty string
        return word

    elif word[0] in "aeiouAEIOU": # first character is vowel
        return remove_vowels(word[1:]) # skip first character and process rest

    return word[0] + remove_vowels(word[1:]) # return first character and process rest


print ("We have removed the Vowels from the word :" , word , ("\n" "The none vowels shall appear below"))

print (remove_vowels(word[1:]))

remove_vowels(word)

