#!/usr/bin/python3
def multiple_returns(sentence):
    lenth = len(sentence)
    my_char = sentence[0] if lenth > 0 else "None"
    tup = lenth, my_char
    return(tup)
