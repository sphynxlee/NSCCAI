#########################
# Actually Using TeenNet
########################
NUM_INPUT_NODES  = 28*28
NUM_HIDDEN_NODES = 200
NUM_OUTPUT_NODES = 10

LEARNING_RATE = 0.15


tNet = TeenNet(NUM_INPUT_NODES,NUM_HIDDEN_NODES,NUM_OUTPUT_NODES,LEARNING_RATE)

training_data_file = open("mnist_train_small.csv",'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

NUM_EPOCHS = 1

for epoch in range(NUM_EPOCHS):
  for record in training_data_list:
    # put all values - including first actual digit - into a list
    all_values = record.split(',')
    # make a numpy array of just the images pixels
    # [TODO:explain in more detail]
    inputs = (numpy.asfarray(all_values[1:])/255.0 * .99) + 0.01

    # create the output vector we want to see in this case
    # we should have all close-to-zeros, except for the slot
    # that represents the actual digit - there we want close-to-one
    targets = numpy.zeros(NUM_OUTPUT_NODES) + 0.01
    targets[int(all_values[0])] = 0.99
    
    # go ahead and pass in the inputs and expected output to TeenNet to train
    tNet.train(inputs,targets)