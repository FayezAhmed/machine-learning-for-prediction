# Machine Learning for Prediction

This is a machine learning project that focuses on building a prediction model using scikit-learn package in Python. The project demonstrates how to create a machine learning model, generate a training set, train the model, and use it for prediction.

## Project Overview

Machine learning systems are widely used in various domains such as image understanding, speech recognition, medical diagnosis, prediction systems, and more. The core of any machine learning system is building a model that analyzes a large number of inputs and their corresponding outputs to identify the relationship between them.

In this project, I explore the process of building a machine learning model using scikit-learn to predict outcomes based on input data. 

## Getting Started

To run this project, you will need to have Python and scikit-learn installed on your system. You have two options for running the project:

1. **Online:** If you are working online using a platform like Repl.it, scikit-learn is already available. You can upload the code there.
2. **Local Machine:** If you are working on your own machine, you need to install scikit-learn using pip after installing Python/IDLE. Refer to the official scikit-learn installation guide for detailed instructions.

## Building a Model with Real-World Data

1. **Processing the data:** The program processes the data given in a .csv file. The user must provide the program with the column that contains the output value and other numeric columns that can be used as inputs. Two example .csv files are provided: dataset_Facebook.csv and SeoulBikeData.csv, which can be used for testing.
2. **Reading and splitting the data:** The .csv file is read and formatted into two list: the output list containing all output values and the input list as a list of lists, with each sublist containing numeric values from one line of the file. The the input and output lists are split into training and test sets.
3. **Training the model:** The training input and output lists are used to train and build your machine learning model using scikit-learn. 
4. **Using the model for prediction:** The the test input list is used to predict values for the desired output using the trained model. Predictions are compared to actual values in the test output list.
5. **Visualizing the performance of the model:** The percentage error for each prediction is calculated and categorized them based on their range of deviation from the actual value. A visualization is created using Turtle.
Certainly! Here are the updated instructions for the README with code prompts:

---

## Instructions

1. **Install Python**: Make sure Python is installed on your operating system. You can download Python from the official website: [python.org](https://www.python.org/).

2. **Install scikit-learn**: Open a terminal or command prompt and install scikit-learn using pip by running the following command:
   ```
   pip install scikit-learn
   ```

3. **Prepare the Dataset**: Prepare a CSV file containing the data for prediction. Ensure that the dataset has a header row and is free of any special characters, such as the degree symbol (°). 

4. **Identify Input and Output Columns**: Determine the column to be predicted (output column) and identify all other numeric columns that will be used for prediction. If you're using the provided test file (SeoulBikeData.csv), the rented bike count column should be considered as the output column, and the other numeric columns can be used for prediction.

5. **Run the Program**: Open a terminal or command prompt and navigate to the project directory. Run the `main.py` file and follow the instructions provided in the terminal to proceed with the machine learning model training and prediction:
   ```
   python main.py
   ```

6. **View the Prediction Error Graph**: Once the prediction process is completed, locate the generated Turtle application to view the prediction error graph. The graph will depict the performance of the model in predicting the rented bike count.

Make sure to follow these instructions step by step to successfully run the project and visualize the prediction error graph.
