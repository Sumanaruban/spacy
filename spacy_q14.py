# Sumani
# [21-5-2022]

import spacy

def multi_lingual_NER(text, lang_code):
    ret = []
    nlp = spacy.load(lang_code)
    doc = nlp(text)
    for token in doc:
        d = {'text':token.text, 'type':token.type, 'start_pos':token.idx, 'end_pos':token.idx+len(token.text)}
        ret.append(d)
    return ret   
