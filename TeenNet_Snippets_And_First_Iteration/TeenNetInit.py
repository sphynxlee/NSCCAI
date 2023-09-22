  def __init__(self,num_input_nodes,num_hidden_nodes, num_output_nodes, learning_rate):
    self.num_input_nodes = num_input_nodes
    self.num_hidden_nodes = num_hidden_nodes
    self.num_output_nodes = num_output_nodes

    self.learning_rate = learning_rate
    self.activation_function = lambda x: scipy.special.expit(x)
  
    # [TODO:explain  in more detail]
    #self.first_weights = numpy.random.normal(0.0,pow(self.num_hidden_nodes,-0.5),(self.num_hidden_nodes,self.num_input_nodes))
    #self.second_weights = numpy.random.normal(0.0,pow(self.num_output_nodes,-0.5),(self.num_output_nodes,self.num_hidden_nodes))
    self.first_weights = numpy.random.rand(self.num_hidden_nodes,self.num_input_nodes) - 0.5
    self.second_weights = numpy.random.rand(self.num_output_nodes,self.num_hidden_nodes) - 0.5