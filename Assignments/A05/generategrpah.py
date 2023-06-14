import graphviz
import math
import pandas as pd
import os
from generatefamily import get_random_family_data

graph = graphviz.Digraph()

get_random_family_data(no_generations=3)

df = pd.read_csv('family_data.csv')

max_generation = int(df['generation'].max())
min_birth_year = int(df['byear'].min())
max_birth_year = int(df['byear'].max())
median_birth_year = int(df['byear'].median())

ranks = {f'rank{i}': [] for i in range(1, max_generation + 1)}
current_location = os.path.dirname(os.path.abspath(__file__))
image_base_path = current_location + '/resources/images/'

for _, row in df.iterrows():
    pid = str(row['pid'])
    name = row['name']
    last_name = row['last_name']
    gender = row['gender']
    byear = row['byear']
    generation = row['generation']
    spouse_id = row['spouse_id']
    parent_id1 = row['parent_id1']
    parent_id2 = row['parent_id2']
    generation = row['generation']
    clan = row['clan']
    dyear = row['dyear']
    if not math.isnan(dyear):
        dyear = int(dyear)
    else:
        dyear = "_"
    if gender == "Male":
        if byear >= max_birth_year - 20:
            image_path = image_base_path + "kid_male.png"
        elif byear >= median_birth_year - 20:
            image_path = image_base_path + "young_male.png"
        else:
            image_path = image_base_path + "old_male.png"
    else:
        if byear >= max_birth_year - 20:
            image_path = image_base_path + "kid_female.png"
        elif byear >= median_birth_year - 10:
            image_path = image_base_path + "young_female.png"
        else:
            image_path = image_base_path + "old_female.png"

    # Change node shape to 'box' to remove round shape
    label = f"<<TABLE BORDER='0' CELLBORDER='1' CELLSPACING='0'><TR><TD><FONT FACE='arial' POINT-SIZE='14'><B>{name} {last_name}</B></FONT></TD></TR><TR><TD><IMG SRC='{image_path}'/></TD></TR><TR><TD>Gender: ({gender})</TD></TR><TR><TD>Years: ({byear}-{dyear})</TD></TR><TR><TD>clan: ({clan})</TD></TR></TABLE>>"

    graph.node(pid, label, shape='box')

    if not pd.isna(spouse_id):
        graph.edge(pid, str(int(spouse_id)), style='dashed')

    if not pd.isna(parent_id1):
        graph.edge(str(int(parent_id1)), pid)
    if not pd.isna(parent_id2):
        graph.edge(str(int(parent_id2)), pid)

    rank = f'rank{int(generation)}'
    ranks[rank].append((pid, label))

graph.graph_attr['rankdir'] = 'TB'

for rank, nodes in ranks.items():
    with graph.subgraph() as sub:
        sub.attr(rank='same')
        for node, label in nodes:
            sub.node(node, label)

graph.render('family_tree', format='png', view=True)
