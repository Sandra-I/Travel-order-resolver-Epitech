from spacy.symbols import PROPN, NOUN
import numpy as numpy

def evaluate_token(cities, doc):
    tokens = numpy.zeros(len(cities), dtype=object)
    for i in range(len(cities)):
        tokenFound = False
        for token in doc:
            if token.pos == PROPN:
                isUsable = True
                for tokenSelected in tokens:
                    if type(tokenSelected) != int and tokenSelected == token:
                        isUsable = False
                if isUsable:
                    if token.text in cities[i]:
                        tokens[i] = token
                        tokenFound = True
                        break

        if tokenFound == False:
            for token in doc:
                if token.pos == NOUN:
                    isUsable = True
                    for tokenSelected in tokens:
                        if type(tokenSelected) != int and tokenSelected == token:
                            isUsable = False
                    if isUsable:
                        if token.text in cities[i]:
                            tokens[i] = token
                            tokenFound = True
                            break

        if tokenFound == False:
            for token in doc:
                isUsable = True
                for tokenSelected in tokens:
                    if type(tokenSelected) != int and tokenSelected == token:
                        isUsable = False
                if isUsable:
                    if token.text in cities[i]:
                        tokens[i] = token
                        tokenFound = True
                        break

        if tokenFound == False:
            print(f"Localization {cities[i]} not found")
            tokens[i] = None

    tmpTokens = tokens
    tokens = []
    for token in tmpTokens:
        if token != None:
            tokens.append(token)
    return tokens
