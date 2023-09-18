mlAlgorithmProblem = "There have problem with machine learning.\nBut we could gradually solve them, and finally you would have a suggestion of a set of possible Machine Learning algorithms to solve your problem";
print(mlAlgorithmProblem, '\n\n');

labelDataFlag = True
while labelDataFlag:
  isLabeledData = input("Do you have labeled data?\nPlease input [Y] or [N]: \n");
  isLabeledData = isLabeledData.upper();
  if (isLabeledData == 'Y'):
    while True:
      print("Your answer is labeled data, therefore it should be using Supervised learning.\n");
      isCategoryOrQuantityData = input("Are these labeled data with Category or Quantity?\nPlease input [C] or [Q]: \n");
      isCategoryOrQuantityData = isCategoryOrQuantityData.upper();
      if (isCategoryOrQuantityData == 'C'):
        print("Your answer is Category, therefore the answer is that your Labeled Data is Classification.\nAnd the suggestion algorithm is below:");
        print("Neural Network\nLogistic Regression\nRandom Forest\nNaive Bayes\nSupport Vector Machine");
        labelDataFlag = False;
        break;
      elif (isCategoryOrQuantityData == 'Q'):
        print("Your answer is Quantity, therefore the answer is that your Labeled Data is Regression.\nAnd the suggestion algorithm is below:");
        print("Support Vector Machine\nNeural Network\nRidge Regression\nRandom Forest\nLasso");
        labelDataFlag = False;
        break;
      else:
        print("Your input is incorrect, neither Category or Quantity, please try again.\n\n");
  elif (isLabeledData == 'N'):
    while True:
      print("Your answer is NOT labeled data, therefore it should be using Unsupervised learning.\n");
      isGroupOrLowerDimData = input("Are these unlabeled data with Group or Lower Dim?\nPlease input [G] or [L]: \n");
      isGroupOrLowerDimData = isGroupOrLowerDimData.upper();
      if (isGroupOrLowerDimData == 'G'):
        print("Your answer is Group, therefore the answer is that your Unlabeled Data is Clustering.\nAnd the suggestion algorithm is below:");
        print("K-means\nGaussian Mixture\nDBSCAN\nSpectral Clustering\nHierarchical Clustering");
        labelDataFlag = False;
        break;
      elif (isGroupOrLowerDimData == 'L'):
        print("Your answer is Lower Dim, therefore the answer is that your Unlabeled Data is Dimensionality reduction.\nAnd the suggestion algorithm is below:");
        print("PCA\nLDA\nIsomap\nAutoencoder");
        labelDataFlag = False;
        break;
      else:
        print("Your input is incorrect, neither Group or Lower Dim, please try again.\n\n");
  else:
    print("Your input is incorrect, please confirm if your have Labeled data, please try again.\n\n");