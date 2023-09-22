import numpy

def train(self,inputs_list,targets_list):
  # [TODO:explain in more detail]
  inputs  = numpy.array(inputs_list,ndmin=2).T
  targets = numpy.array(targets_list,ndmin=2).T

  hidden_in = numpy.matmul(self.first_weights,inputs)
  hidden_out = self.activation_function(hidden_in)

  final_in = numpy.matmul(self.second_weights,hidden_out)
  final_out = self.activation_function(final_in)

  # notice that our subtraction here is acting on numpy arrays
  # this is our - very simple - COST FUNCTION. It's living here
  # for now - because it's so simple.
  output_errors = targets-final_out


  # use output errors to update weights between hidden layer and output layer
  self.second_weights += self.learning_rate * numpy.matmul((output_errors * final_out  * (1.0-final_out)),numpy.transpose(hidden_out))


  # backprop errors from output_errors to hidden_errors
  hidden_errors = numpy.matmul(self.second_weights.T,output_errors)
  # use hidden errors to update weights between input layer and hidden layer
  self.first_weights += self.learning_rate * numpy.matmul((hidden_errors * hidden_out * (1.0-hidden_out)),numpy.transpose(inputs))