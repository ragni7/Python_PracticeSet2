def ReverseString(sentence):
    sent = sentence.split(" ")
    NeWords = [word[::-1] for word in sent]
    NewSent = " ".join(NeWords)
    return NewSent

sentence = "hi heello good night"
ReverseString(sentence)
print(ReverseString(sentence))