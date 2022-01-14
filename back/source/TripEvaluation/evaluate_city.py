import spacy
import source.TripEvaluation.evaluate_token as et

def evaluate_city(str):
    print("Request: " + str)
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(str)
    cities = []
    for ent in doc.ents:
        if ent.label_ == 'GPE' or ent.label_ == 'LOC':
            cities.append(ent.text)
    print(f"Cities found: {cities}")
    # if len(cities) == 1:
    #     return cities, doc
    if len(cities) <= 1:
        return 83, 83
    else:
        return cities, doc