class Graph:
    def __init__(self):
        self.nodes = {}  # key: entity name, value: entity type
        self.relationships = set()  # Use a set to avoid duplicates

    def add_node(self, entity_name, entity_type):
        """Add a node if it does not exist already, for specific types."""
        if entity_name not in self.nodes and entity_type in ["PERSON", "DATE", "GPE", "ORG"]:
            self.nodes[entity_name] = entity_type

    def add_relationship(self, entity1, entity2):
        """Add a relationship between two nodes if they are of the correct types, avoiding duplicates."""
        valid_pairs = [("PERSON", "ORG"), ("PERSON", "DATE"), ("PERSON", "GPE"),
                       ("ORG", "GPE"), ("ORG", "DATE"), ("GPE", "DATE")]
        if entity1 in self.nodes and entity2 in self.nodes:
            if (self.nodes[entity1], self.nodes[entity2]) in valid_pairs or (self.nodes[entity2], self.nodes[entity1]) in valid_pairs:
                # Add a tuple to the set; sets automatically avoid duplicates
                self.relationships.add((entity1, entity2))

    def display(self):
        """Display nodes and relationships."""
        print("Nodes:")
        for node, n_type in self.nodes.items():
            print(f"{node} ({n_type})")
        print("\nRelationships:")
        for rel in self.relationships:
            print(f"{rel[0]} - {rel[1]}")

# The main function and entity extraction logic remain largely the same,
# but you should ensure the entity extraction process filters out invalid entities.