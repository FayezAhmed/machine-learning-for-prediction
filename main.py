# 4. Second Project Extension
# Author: Fayez Ahmed
# Date: Nov. 28, 2022
# Interactively processes a user-provided CSV file and then uses a machine
# learning model to predict values from the CSV file
import fayezMachineLearning # File containing functions
                            # for machine learning model

# Greet user
print("Welcome to the Interactive Machine Learning Model")

# Get user input for the name of the csv file
csv_filename = input(
    "\nEnter the name of your CSV file, \
\nincluding \".csv\" at the end (ex:filename.csv): ")

# Get user input for column containing output
output_index = int(input(
    "\nEnter the index containing the output (column being predicted): "))

# Get user input for columns containing input
# Create list of 
input_indicies = input(
    "\nEnter the indicies of the input variables, seperated by commas \
\n(columns used for prediction, ex: 2,3,4,5): ").strip(" ").split(",")

# Open file and remove header
dataset_file = open(csv_filename)
dataset_file.readline()

# Initialize input and output lists
input_list = []
output_list = []

# Go through each line in the file
for line in dataset_file:
    # Convert the line into a list
    line_data = line.split(",")
    # Remove "/n" from the last item if it is there
    line_data[-1] = line_data[-1].rstrip("\n")

    # Go through each item in the list and add zeros if it is missing
    for i in range(0, len(line_data)):
        if line_data[i] == "":
            line_data[i] = "0.0"

    # Add the output item from the list into the output list
    # Ouput index is given by the user
    output_list += [float(line_data[output_index])]

    # Initialize list to store all the input items from the line
    prediction_variables = []
    # Go through the indicies of the input items and add them to the
    # list of prediction variables
    # The indicies are given by the user
    for i in input_indicies:
        prediction_variables += [float(line_data[int(i)])]
    # Adds the items for predictions to the input list
    input_list += [prediction_variables]

# Initialize dictionary that will contain lists of inputs and outputs
inputs_and_outputs = {}
# Split the lists for training and testing into a dictionary
fayezMachineLearning.split_lists(input_list, output_list, inputs_and_outputs)

# Use machine learning to predict the test values
# Train machine learning model and then test it
# Store the outcomes into a list
predictions = fayezMachineLearning.machine_learning_model(inputs_and_outputs)

# Calculate the errors from the machine learning model and
# store the errors into a dictionary
error_collection = fayezMachineLearning.calculate_model_efficiency(
    inputs_and_outputs, predictions)

# Create a graph to display the errors caused by the machine
# learning model to display its efficiency
bar_color = "#00e676" # sets color for bars of the graph
fayezMachineLearning.percentage_error_graph(error_collection, bar_color)
