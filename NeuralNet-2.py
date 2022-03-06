#####################################################################################################################
#   Assignment 2: Neural Network Analysis
#   This is a starter code in Python 3.6 for a neural network.
#   You need to have numpy and pandas installed before running this code.
#   You need to complete all TODO marked sections
#   You are free to modify this code in any way you want, but need to mention it
#       in the README file.
#
#####################################################################################################################

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


class NeuralNet:
    def __init__(self, dataFile, header=True):
        self.raw_input = pd.read_excel(dataFile)

    # TODO: Write code for pre-processing the dataset, which would include
    # standardization, normalization,
    #   categorical to numerical, etc
    def preprocess(self):
        self.processed_data = self.raw_input
        #convert categorical bean classes to numbers
        self.processed_data['Class'].replace(['SEKER', 'BARBUNYA', 'BOMBAY', 'CALI', 'DERMASON', 'HOROZ', 'SIRA'],
                        [0, 1, 2, 3, 4, 5, 6], inplace=True)
        #take a look at the processed data
        print(self.processed_data)

        ncols = len(self.processed_data.columns)
        nrows = len(self.processed_data.index)

        #divide attributes (X) from class (Y) which is the target that we want to predict
        X = self.processed_data.iloc[:, 0:(ncols - 1)]
        y = self.processed_data.iloc[:, (ncols-1)]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y)

        #Scale data, sklearn documentation says this is important to do for the Multi-Layer Perceptron
        scaler = StandardScaler()
        scaler.fit(self.X_train)
        self.X_train = scaler.transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)
        return 0

    # TODO: Train and evaluate models for all combinations of parameters
    # specified. We would like to obtain following outputs:
    #   1. Training Accuracy and Error (Loss) for every model
    #   2. Test Accuracy and Error (Loss) for every model
    #   3. History Curve (Plot of Accuracy against training steps) for all
    #       the models in a single plot. The plot should be color coded i.e.
    #       different color for each model

    def train_evaluate(self):
        # Below are the hyperparameters that you need to use for model
        #   evaluation
        activations = ['logistic', 'tanh', 'relu']
        learning_rate = [0.01, 0.1]
        max_iterations = [100, 200] # also known as epochs
        num_hidden_layers = [2, 3]

        # Create the neural network and be sure to keep track of the performance metrics
        # TODO: cycle through activations, learning rates, max iterations
        neural_network = MLPClassifier(activation=activations[0], hidden_layer_sizes=num_hidden_layers, alpha=1e-5, learning_rate_init=learning_rate[0], max_iter=max_iterations[1])
        #Train the model on the training data
        neural_network.fit(self.X_train, self.y_train)
        #Test the model on the training data
        y_train_predictions = neural_network.predict(self.X_train)
        #Test the model on the test data
        y_test_predictions = neural_network.predict(self.X_test)

        rmse = (np.sqrt(mean_squared_error(self.y_train, y_train_predictions)))
        r2 = r2_score(self.y_train, y_train_predictions)

        print("Training set performance:")
        print('RMSE is {}'.format(rmse))
        print('R2 score is {}'.format(r2))
        print("\n")

        rmse = (np.sqrt(mean_squared_error(self.y_test, y_test_predictions)))
        r2 = r2_score(self.y_test, y_test_predictions)

        print("Test set performance:")
        print('RMSE is {}'.format(rmse))
        print('R2 score is {}'.format(r2))
        print("\n")

        # Plot the model history for each model in a single plot
        # model history is a plot of accuracy vs number of epochs
        # you may want to create a large sized plot to show multiple lines
        # in a same figure.

        return 0


if __name__ == "__main__":
    neural_network = NeuralNet("Dry_Bean_Dataset.xlsx") # put in path to your file
    neural_network.preprocess()
    neural_network.train_evaluate()
