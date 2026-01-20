#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if sentence == '':
        first = None
    else:
        first = sentence[0]
    return lenght, first
