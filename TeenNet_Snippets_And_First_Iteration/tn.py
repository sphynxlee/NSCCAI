import numpy as np
import scipy.special

import os
pwd = os.getcwd()

class TeenNet:

  def __init__(self,num_input_nodes,num_hidden_nodes, num_output_nodes, learning_rate):
    self.num_input_nodes = num_input_nodes
    self.num_hidden_nodes = num_hidden_nodes
    self.num_output_nodes = num_output_nodes

    self.learning_rate = learning_rate
    self.activation_function = lambda x: scipy.special.expit(x)

    # [TODO:explain  in more detail]
    #self.first_weights = np.random.normal(0.0,pow(self.num_hidden_nodes,-0.5),(self.num_hidden_nodes,self.num_input_nodes))
    #self.second_weights = np.random.normal(0.0,pow(self.num_output_nodes,-0.5),(self.num_output_nodes,self.num_hidden_nodes))
    self.first_weights = np.random.rand(self.num_hidden_nodes,self.num_input_nodes) - 0.5
    self.second_weights = np.random.rand(self.num_output_nodes,self.num_hidden_nodes) - 0.5

  def train(self,inputs_list,targets_list):
    # [TODO:explain in more detail]
    inputs  = np.array(inputs_list,ndmin=2).T
    targets = np.array(targets_list,ndmin=2).T

    hidden_in = np.matmul(self.first_weights,inputs)
    hidden_out = self.activation_function(hidden_in)

    final_in = np.matmul(self.second_weights,hidden_out)
    final_out = self.activation_function(final_in)

    # notice that our subtraction here is acting on np arrays
    # this is our - very simple - COST FUNCTION. It's living here
    # for now - because it's so simple.
    output_errors = targets - final_out


    # use output errors to update weights between hidden layer and output layer
    self.second_weights += self.learning_rate * np.matmul((output_errors * final_out  * (1.0 - final_out)),np.transpose(hidden_out))


    # backprop errors from output_errors to hidden_errors
    hidden_errors = np.matmul(self.second_weights.T,output_errors)
    # use hidden errors to update weights between input layer and hidden layer
    self.first_weights += self.learning_rate * np.matmul((hidden_errors * hidden_out * (1.0 - hidden_out)),np.transpose(inputs))


  def forward_pass(self,inputs_list):
    # [TODO:explain in more detail]
    inputs = np.array(inputs_list,ndmin=2).T

    hidden_inputs = np.matmul(self.first_weights,inputs)
    hidden_outputs = self.activation_function(hidden_inputs)

    final_inputs = np.matmul(self.second_weights,hidden_outputs)
    final_outputs = self.activation_function(final_inputs)
    return(final_outputs)



#########################
# Actually Using TeenNet
########################
NUM_INPUT_NODES  = 28*28
NUM_HIDDEN_NODES = 200
NUM_OUTPUT_NODES = 10

LEARNING_RATE = 0.15


tNet = TeenNet(NUM_INPUT_NODES,NUM_HIDDEN_NODES,NUM_OUTPUT_NODES,LEARNING_RATE)

pwd_mnist_train_small = pwd + '/NSCCAI/TeenNet_Snippets_And_First_Iteration/mnist_train_small.csv'
print('pwd_mnist_train_small is: ', pwd_mnist_train_small)
training_data_file = open(pwd_mnist_train_small,'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

NUM_EPOCHS = 1

for epoch in range(NUM_EPOCHS):
  for record in training_data_list:
    # put all values - including first actual digit - into a list
    all_values = record.split(',')
    # make a np array of just the images pixels
    # [TODO:explain in more detail]
    inputs = (np.asfarray(all_values[1:])/255.0 * .99) + 0.01

    # create the output vector we want to see in this case
    # we should have all close-to-zeros, except for the slot
    # that represents the actual digit - there we want close-to-one
    targets = np.zeros(NUM_OUTPUT_NODES) + 0.01
    targets[int(all_values[0])] = 0.99

    # go ahead and pass in the inputs and expected output to TeenNet to train
    tNet.train(inputs,targets)


##############################################
# Check quality of results
##############################################

# to check results, we want to load up the training data and get it into a list
pwd_mnist_test = pwd + '/NSCCAI/TeenNet_Snippets_And_First_Iteration/mnist_test.csv'
print('pwd_mnist_test is: ', pwd_mnist_test)
test_data_file = open(pwd_mnist_test,'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# just a place to store some info, we can make this fancier later
scorecard = []

for record in test_data_list:

  # a split used just like we did in programming class
  all_values = record.split(',')

  # the actual digit is the first item in each row
  actual_digit = int(all_values[0])

  # the inputs are all the values except the 0-th one
  # [TODO:explain in more detail]
  inputs = (np.asfarray(all_values[1:]) / 255.0 *.99) + 0.01

  # ask TeenNet for the outputs, based on the inputs
  outputs = tNet.forward_pass(inputs)

  # ask np to grab the biggest output, this is the first step in Michel's _translation_ function in this case
  guessed_digit = np.argmax(outputs)


  if(guessed_digit == actual_digit):
    scorecard.append(1) # yippee!
  else:
    scorecard.append(0) # ouch :(

# trivial scoring - just percent correct
scorecard_array = np.asarray(scorecard)
print("Performance = ", scorecard_array.sum()/scorecard_array.size*100, "%")