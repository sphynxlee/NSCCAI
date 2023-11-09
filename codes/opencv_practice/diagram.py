import graphviz
from graphviz import Digraph

# Create a new Graphviz Digraph
dot = Digraph(comment='Convolutional Neural Network')

# Add nodes for layers
dot.node('Input', 'Input Image\n(1, 1, 28, 28)')
dot.node('Conv1', 'Conv2d(1, 6, 5, padding=2)\n(1, 6, 28, 28)')
dot.node('ReLU1', 'ReLU()\n(1, 6, 28, 28)')
dot.node('MaxPool1', 'MaxPool2d(2, stride=2)\n(1, 6, 14, 14)')
dot.node('Conv2', 'Conv2d(6, 16, 5, padding=0)\n(1, 16, 10, 10)')
dot.node('ReLU2', 'ReLU()\n(1, 16, 10, 10)')
dot.node('MaxPool2', 'MaxPool2d(2, stride=2)\n(1, 16, 5, 5)')
dot.node('Flatten', 'Flatten()\n(1, 400)')
dot.node('FC1', 'Linear(400, 120)\n(1, 120)')
dot.node('FC2', 'Linear(120, 84)\n(1, 84)')
dot.node('FC3', 'Linear(84, 10)\n(1, 10)')
dot.node('Output', 'Predicted Label\n(1,)')

# Define edges to connect nodes
dot.edges([
    ('Input', 'Conv1'),
    ('Conv1', 'ReLU1'),
    ('ReLU1', 'MaxPool1'),
    ('MaxPool1', 'Conv2'),
    ('Conv2', 'ReLU2'),
    ('ReLU2', 'MaxPool2'),
    ('MaxPool2', 'Flatten'),
    ('Flatten', 'FC1'),
    ('FC1', 'FC2'),
    ('FC2', 'FC3'),
    ('FC3', 'Output')
])

# Render the diagram to a file (e.g., 'cnn_diagram.gv.png')
dot.format = 'png'
dot.render('cnn_diagram')

print("CNN diagram saved as 'cnn_diagram.png'")
