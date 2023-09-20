import numpy as np

# create a class named TeenNet
class TeenNet:
    # create a constructor
    def __init__(self, input_nodes_num, hidden_nodes_num, output_nodes_num, learning_rate, activation_function):
        # layer nodes
        self.input_nodes_num = input_nodes_num
        # just one hidden layer - at least for now
        self.hidden_nodes_num = hidden_nodes_num
        self.output_nodes_num = output_nodes_num

        # create weights
        self.weights_input_hidden = np.random.rand(input_nodes_num * hidden_nodes_num)
        self.weights_hidden_output = np.random.rand(hidden_nodes_num * output_nodes_num)

        # hyperparameters
        self.activation_function = activation_function
        self.learning_rate = learning_rate

    # create a training_pass method

    # create a forward_pass method
    def forward_pass(self, input_value):
        # create a variable named hidden
        hidden_input_value = np.dot(self.weights_input_hidden, input_value)
        hidden_output_value = self.activation_function(hidden_input_value)
        final_input_value = np.dot(self.weights_hidden_output, hidden_output_value)
        final_output_value = self.activation_function(final_input_value)

        return final_output_value

