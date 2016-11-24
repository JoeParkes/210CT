sentence = "This is Awesome!"

def rev(sentence): 
    if sentence == "":
        return sentence 
    else:
        return rev(sentence[1:]) + sentence[0]

print("This is the sentence muddled up in reverse: ")
print rev(sentence)

rev(sentence)