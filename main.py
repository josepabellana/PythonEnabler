import json
from doc_parser import scrape_text_from_url
from entity_extractor import extract_entities
from graph import Graph

def main():
    graph = Graph()  # Initialize your graph
    
    with open('config.json') as f:
        config = json.load(f)
    
    # Process URLs
    for url in config['urls']:
        text = scrape_text_from_url(url)
        entities = extract_entities(text)
        
        # Add nodes for specific entity types
        for entity_text, entity_type in entities:
            graph.add_node(entity_text, entity_type)
        
        # Add relationships based on refined logic
        entities_by_type = {"PERSON": [], "DATE": [], "GPE": [], "ORG": []}
        for entity_text, entity_type in entities:
            if entity_type in entities_by_type:
                entities_by_type[entity_type].append(entity_text)
        
        # Example: Create relationships for people with dates, places, and organizations
        for person in entities_by_type["PERSON"]:
            for org in entities_by_type["ORG"]:
                graph.add_relationship(person, org)
            for date in entities_by_type["DATE"]:
                graph.add_relationship(person, date)
            for place in entities_by_type["GPE"]:
                graph.add_relationship(person, place)

    graph.display()

if __name__ == "__main__":
    main()