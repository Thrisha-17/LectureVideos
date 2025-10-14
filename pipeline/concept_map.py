import networkx as nx
import matplotlib.pyplot as plt
import spacy
nlp = spacy.load("en_core_web_sm")

def build_concept_map(text, out_file):
    doc = nlp(text)
    G = nx.Graph()
    # Add entities as nodes
    for ent in doc.ents:
        G.add_node(ent.text, label=ent.label_)
    # Connect entities that appear in same sentence
    for sent in doc.sents:
        ents = [ent.text for ent in sent.ents]
        for i in range(len(ents)):
            for j in range(i+1, len(ents)):
                G.add_edge(ents[i], ents[j])
    plt.figure(figsize=(10,8))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
    plt.savefig(out_file)
    plt.close()
