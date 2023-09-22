  def forward_pass(self,inputs_list):
    # [TODO:explain in more detail]
    inputs = numpy.array(inputs_list,ndmin=2).T

    hidden_inputs = numpy.matmul(self.first_weights,inputs)
    hidden_outputs = self.activation_function(hidden_inputs)
    
    final_inputs = numpy.matmul(self.second_weights,hidden_outputs)
    final_outputs = self.activation_function(final_inputs)
    return(final_outputs)