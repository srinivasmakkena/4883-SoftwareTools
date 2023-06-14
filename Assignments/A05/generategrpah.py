import graphviz
import math
import pandas as pd
import os
from generatefamily import get_random_family_data

graph = graphviz.Digraph()

number_of_generations=4

get_random_family_data(no_generations=number_of_generations)

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
        graph.edge(pid, str(int(spouse_id)),color='black', penwidth='2')

    if not pd.isna(parent_id1):
        if df.loc[df['pid'] == parent_id1, 'gender'].values[0]=="Male":
            color='blue'
        else:
            color='orange'
        graph.edge(str(int(parent_id1)), pid,color=color, penwidth='3')
    if not pd.isna(parent_id2):
        if df.loc[df['pid'] == parent_id2, 'gender'].values[0]=="Male":
            color='blue'
        else:
            color='orange'
        graph.edge(str(int(parent_id2)), pid,color=color, penwidth='3')

    rank = f'rank{int(generation)}'
    ranks[rank].append((pid, label))

graph.graph_attr['rankdir'] = 'TB'
graph.graph_attr['nodesep'] = '1.2'
graph.graph_attr['ranksep'] = '1.5'
# graph.graph_attr["splines"] = "polyline"
graph.graph_attr["splines"] = "ortho"
for rank, nodes in ranks.items():
    with graph.subgraph() as sub:
        sub.attr(rank='same')
        for node, label in nodes:
            sub.node(node, label)
legend_items = {
    'black': 'Spouse Edge Relation',
    'orange': 'Mother-Child Relation',
    'blue': 'Father-Child Relation'
}

# Create a subgraph for the legend
with graph.subgraph(name='cluster_legend') as legend:
    legend.attr(label='Color code of Edges', labelloc='top', fontweight='bold', labeljust='center', fontsize='15', underline='true', shape='invis', style='filled', color='lightgrey')
    legend.attr(rankdir='TB')
    legend.attr('node', shape='plaintext')

    for color, label in legend_items.items():
        legend.node(color, label, color=color, fontcolor='white', fontweight='bold', shadow='true',fontsize='15', shape='box', width='2', height='0.5', padding='0',style='filled')


graph.render('family_tree', format='png', view=True)
