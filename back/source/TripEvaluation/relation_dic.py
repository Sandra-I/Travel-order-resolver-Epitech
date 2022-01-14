import source.TripEvaluation.word_class as wcl

CCONJ_Relation = [
    wcl.WordSense("depuis",     wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("puis",       wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("et",         wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("enfin",      wcl.Dire.DEST,  wcl.Impact.STRONG)
]

NOUN_Relation = [
    wcl.WordSense("provenance",     wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("direction",      wcl.Dire.DEST,  wcl.Impact.WEAK),
    wcl.WordSense("destination",    wcl.Dire.DEST,  wcl.Impact.WEAK)
]

ADP_FIXED_Relation = [
    wcl.LinkedWordSense("à","partir",       wcl.Dire.START, wcl.Impact.STRONG),
    wcl.LinkedWordSense("en", "partant",    wcl.Dire.START, wcl.Impact.STRONG),
    wcl.LinkedWordSense("à","destination",  wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.LinkedWordSense("en","direction",   wcl.Dire.DEST,  wcl.Impact.WEAK)
]
ADP_Relation = [
    wcl.WordSense("de",     wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("du",     wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("des",    wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("depuis", wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("à",      wcl.Dire.DEST,  wcl.Impact.WEAK),
    wcl.WordSense("au",     wcl.Dire.DEST,  wcl.Impact.WEAK),
    wcl.WordSense("aux",    wcl.Dire.DEST,  wcl.Impact.WEAK),
    wcl.WordSense("dans",   wcl.Dire.DEST,  wcl.Impact.WEAK),
    wcl.WordSense("en",     wcl.Dire.DEST,  wcl.Impact.WEAK),
    wcl.WordSense("par",    wcl.Dire.DEST,  wcl.Impact.WEAK)
]

VERB_MARK_Relation = [
    wcl.WordSense("après",   wcl.Dire.START, wcl.Impact.WEAK),
    wcl.WordSense("de",   wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("avant", wcl.Dire.DEST, wcl.Impact.STRONG),
]
VERB_Relation = [
    wcl.WordSense("décoller",   wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("passer",     wcl.Dire.START, wcl.Impact.WEAK),
    wcl.WordSense("être",       wcl.Dire.START, wcl.Impact.STRONG),
    wcl.WordSense("arriver",    wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("aller",      wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("visiter",    wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("atterrir",   wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("découvrir",  wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("voyager",    wcl.Dire.DEST,  wcl.Impact.STRONG),
    wcl.WordSense("rendre",     wcl.Dire.DEST,  wcl.Impact.STRONG)
]