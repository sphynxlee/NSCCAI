import numpy
from tn import tNet

##############################################
# Check quality of results
##############################################

# to check results, we want to load up the training data and get it into a list
test_data_file = open("mnist_test.csv",'r')
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
  inputs = (numpy.asfarray(all_values[1:]) / 255.0 *.99) + 0.01

  # ask TeenNet for the outputs, based on the inputs
  outputs = tNet.forward_pass(inputs)

  # ask numpy to grab the biggest output, this is the first step in Michel's _translation_ function in this case
  guessed_digit = numpy.argmax(outputs)


  if(guessed_digit == actual_digit):
    scorecard.append(1) # yippee!
  else:
    scorecard.append(0) # ouch :(

# trivial scoring - just percent correct
scorecard_array = numpy.asarray(scorecard)
print("Performance = ", scorecard_array.sum()/scorecard_array.size*100, "%")