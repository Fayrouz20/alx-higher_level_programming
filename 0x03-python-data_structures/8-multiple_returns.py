#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        len_sen = len(sentence)
    else:
        len_sen = 0
    return (len_sen, sentence if not sentence else sentence[:1])
