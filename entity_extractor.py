import spacy

nlp = spacy.load("es_dep_news_trf")

def extract_entities(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities