from spacy.symbols import NOUN, CCONJ, ADP, VERB
import numpy as numpy

import relation_dic as rd
import word_class as wcl


def evaluate_token_strength(tokens):
    tokens_strength = numpy.zeros(len(tokens), dtype=object)
    for i in range(len(tokens)):
        foundWeight = []
        parent = tokens[i].head

        for child in tokens[i].children:
            if child.pos == CCONJ:
                for ref in rd.CCONJ_Relation:
                    if ref.word == child.lemma_:
                        foundWeight.append(ref)
                        break

        if len(foundWeight) <= 0:
            if parent.pos == NOUN:
                for ref in rd.NOUN_Relation:
                    if ref.word == parent.lemma_:
                        foundWeight.append(ref)
                        break

        if len(foundWeight) <= 0:
            for child in tokens[i].children:
                if child.pos == ADP:
                    for subChild in child.children:
                        if subChild.dep_ == 'fixed':
                            for ref in rd.ADP_FIXED_Relation:
                                if ref.word == child.lemma_ and ref.fixedWord == subChild.lemma_:
                                    foundWeight.append(ref)
                                    break

        if len(foundWeight) <= 0:
            for child in tokens[i].children:
                for ref in rd.ADP_Relation:
                    if ref.word == child.lemma_:
                        foundWeight.append(ref)
                        break

        if len(foundWeight) <= 1:
            if parent.pos == VERB:
                for child in parent.children:
                    if child.dep_ == 'mark' and child.pos == ADP:
                        for ref in rd.VERB_MARK_Relation:
                            if ref.word == child.lemma_:
                                foundWeight.append(ref)
                                break

        if len(foundWeight) <= 1:
            for ref in rd.VERB_Relation:
                if ref.word == parent.lemma_:
                    foundWeight.append(ref)
                    break

        if len(foundWeight) == 0:
            foundWeight.append(wcl.WordSense("default", wcl.Dire.DEST, wcl.Impact.WEAK))

        selectedWeight = None
        for j in range(len(foundWeight)):
            if foundWeight[j].strength == wcl.Impact.STRONG:
                selectedWeight = foundWeight[j]
                break
        if selectedWeight is None:
            selectedWeight = foundWeight[0]

        tokens_strength[i] = (tokens[i], selectedWeight)
    return tokens_strength