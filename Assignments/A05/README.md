# FamilyTree via Graphviz
## Srinivas Makkena

### Description:

This project provides a way to generate a random family tree and visualize it using Graphviz. The following files and folders are included:

| File/Folder | Description |
|----------|----------|
| [Resources](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/tree/main/Assignments/A05/resources) | Contains resources such as images that are used to generate the family tree graph. |
| [Person.py](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A05/Person.py) | This file defines the Person class, which is responsible for saving person objects and their attributes. |
| [family_data.csv](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A05/family_data.csv) | After generating the family tree data, it is saved in this CSV file. It contains information about the individuals in the family. |
| [family_tree.png](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A05/family_tree.png) | This is the output image file that represents the generated family tree. It visualizes the relationships between family members. |
| [generatefamily.py](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A05/generatefamily.py) | Running this file generates a random family by utilizing the Person class. It creates a family tree with randomly assigned individuals and their relationships. |
| [generategraph.py](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A05/generategraph.py) | This file is responsible for generating the graph by utilizing the generated family data and creating the Graphviz code. It uses the family_data.csv file as input to create the visual representation of the family tree. |

## Instructions:

1. Install Graphviz for Windows or Mac based on your operating system from [https://graphviz.org/download/](https://graphviz.org/download/) and make sure to add it to your PATH.
2. Install the required libraries by running `pip install -r requirements.txt` in your command line or terminal.
3. If you want to adjust the number of generations in the family tree, modify the `generation.py` file accordingly.
4. Run the [generatefamily.py](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A05/generatefamily.py) file to generate the random family tree data.
5. The output of the script will be the family tree graph saved as family_tree.png, representing the relationships between the generated individuals.

With this project, you can easily create and visualize random family tree data, allowing you to explore different family structures and relationships.
