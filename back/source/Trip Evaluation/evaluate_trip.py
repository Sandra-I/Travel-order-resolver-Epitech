import word_class as wcl

def evaluate_trip(weighedTokens):
    city_order = []
    orderedTokens = []
    numberOfStrongStrength = 0
    for i in range(len(weighedTokens)):
        token, weight = weighedTokens[i]
        if weight.direction == wcl.Dire.START:
            if weight.strength == wcl.Impact.STRONG:
                orderedTokens.insert(numberOfStrongStrength, token)
                numberOfStrongStrength = numberOfStrongStrength + 1
            else:
                orderedTokens.append(token)
    numberOfStrongStrength = 0
    for i in range(len(weighedTokens)):
        token, weight = weighedTokens[i]
        if weight.direction == wcl.Dire.DEST:
            if weight.strength == wcl.Impact.STRONG:
                orderedTokens.append(token)
                numberOfStrongStrength = numberOfStrongStrength + 1
            else:
                if numberOfStrongStrength == 0:
                    orderedTokens.append(token)
                else:
                    orderedTokens.insert(len(orderedTokens) - numberOfStrongStrength, token)
    for token in orderedTokens:
        city_order.append(token.text)
    return city_order