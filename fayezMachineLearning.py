# fayezMachineLearning
# Author: Fayez Ahmed
# Date: Dec. 05, 2022
# Organized functions used by main.py
# for machine learning programs
import turtle
from sklearn.linear_model import LinearRegression


def split_lists(input_list, output_list, list_collection):
    """
    Input: input_list - list of lists containing inputs for predictions
           output_list - list containing outputs
           list_collection - empty dictionary
    Output: Modifies a dictionary to contain 4 lists:
            train_input, train_output, test_input, test_ouput.
            These are split from the input_list and output_list.
    """
    # Create a key called "train_input" in the dictionary
    # which contains approximately 80% of the inputs 
    list_collection["train_input"] = input_list[:int(0.80 * len(input_list))]

    # Create a key called "test_input" in the dictionary
    # which contains approximately 20% of the inputs 
    list_collection["test_input"] = input_list[int(0.80 * len(input_list)):]

    # Create a key called "train_output" in the dictionary
    # which contains approximately 80% of the outputs
    list_collection["train_output"] = output_list[:int(0.80 * len(output_list))]

    # Create a key called "test_output" in the dictionary
    # which contains approximately 20% of the outputs
    list_collection["test_output"] = output_list[int(0.80 * len(output_list)):]


def machine_learning_model(list_collection):
    """
    Input: list_collection - dictionary which contains 4 lists for
           training and testing the machine learning model
    Output: Returns a list of outcome values predicted by the
            machine learning model
    """
    # Create machine learning model
    predictor = LinearRegression(n_jobs = -1)

    # Train the model
    predictor.fit(X = list_collection["train_input"], y = list_collection["train_output"])

    # Get model to predict a set of outcomes
    outcome = predictor.predict(X = list_collection["test_input"])

    # Return the predictions
    return outcome


def calculate_model_efficiency(list_collection, outcome):
    """
    Input: list_collection - dictionary which contains 4 lists for
           training and testing the machine learning model
           outcome - list of predictions created by the machine learning model
    Output: Returns a dictionary containing percent errors by comparing the
            outcomes from the machine learning model and the actual values
            (test_output)
    """
    # Intialize an empty list to contain all the percent errors
    percent_errors = []
    
    # Go through predicted value from outcome compare it to
    # the actual value from "test_output" 
    for i in range(len(list_collection["test_input"])):
        if list_collection["test_output"][i] != 0.0:

            # Calculate the percent error by the equation:
            #(actual value - predicted value)/actual value
            # Add each value to the percent errors list
            percent_errors += [int(
                (abs(list_collection["test_output"][i] - outcome[i]))
                / list_collection["test_output"][i] * 100)]

    # Create dictionary to separate the percent errors by 10%
    counted_percent_errors = {10:0, 20:0, 30:0, 40:0, 50:0,
                              60:0, 70:0, 80:0, 90:0, 100:0, "100+":0}

    # Go through each percent and check which bracket it falls in
    for percent in percent_errors:
        for percent_bracket in range(10,110,10):
            # Check if error is within range of the bracket
            if percent < percent_bracket and percent >= (percent_bracket - 10):
                # Add to the count for the corresponding key in the dictionary
                counted_percent_errors[percent_bracket] += 1

    # Go through each percent and check if the percent error is over 100
    for percent in percent_errors:
        if percent >= 100:
            # Add the count to the "100+" key in the dictionary
            counted_percent_errors["100+"] += 1

    # Return the dictionary containing all the counted percent errors to graph
    return counted_percent_errors


def percentage_error_graph(data_table, color):
    """
    Input: data_table - dictionary containing percent errors to graph
           color - string containing hex code for color of the graph
    Output: Creates a graph using turtle to display efficiency of the
            machine learning model
    """
    # Set up the turtle screen, with title and dimensions
    window = turtle.Screen()
    window.title("Percentage Errors")
    window.setup(600,500)

    # Create turtle and adjust speed and position
    graph = turtle.Turtle()
    graph.speed(0)
    graph.penup()
    x = -150
    y = -100
    graph.setposition(x,y)
    graph.pendown()
    graph.forward(5)

    # Draw each bar representing a percent bracket
    for key in data_table:
        graph.forward(5)
        graph.left(90)
        graph.fillcolor(color)
        graph.begin_fill()
        graph.forward(data_table[key])
        graph.right(90)

        # Print y-value above the bar
        graph.forward(12.5)
        graph.write(str(data_table[key]), move = False,
                    align = "center", font = ("Arial", 5, "normal"))
        graph.forward(12.5)

        graph.right(90)
        graph.forward(data_table[key])
        graph.end_fill()
        graph.left(90)

    # Get height of tallest bar
    max = 0
    for key in data_table:
        if data_table[key] > max:
            max = data_table[key]

    # Create border for graph
    height = 10 + max # Uses tallest bar to set height
    width = 25*11 + 5*10 + 5 + 10
    graph.forward(5)
    graph.left(90)
    graph.forward(height)
    graph.left(90)
    graph.forward(width)
    graph.left(90)
    graph.forward(height)
    graph.left(90)
    graph.forward(width)

    # Reset postion of pen for writing x-values
    graph.penup()
    graph.setposition(x,y - 10)

    # Create list of x-values
    x_values = ["0-10%", "10-20%", "20-30%", "30-40%", "40-50%",
                "50-60%", "60-70%", "70-80%", "80-90%", "90-100%", "100%+"]

    # Write out the x-values
    graph.forward(5)
    for i in x_values:
        graph.forward(5 + 12.5)
        graph.write(i, move = False, align = "center",
                    font = ("Arial", 5, "normal"))
        graph.forward(12.5)

    # Write x-axis title
    graph.setposition(x,y - 25)
    graph.forward((width)/2)
    graph.write("Percent Bracket", move = False, align = "center")

    # Write y-axis title
    graph.setposition(x - 5,y)
    graph.left(90)
    graph.forward(height/2)
    graph.write("Errors", move = False, align = "right")

    # Write graph title
    graph.setposition(x + (width/2),y + height)
    graph.write("Percentage Errors", move = False, align = "center",
                font = ("Arial", 15, "bold"))

    # Hide pen and leave window open till user clicks
    graph.hideturtle()
    turtle.exitonclick()

