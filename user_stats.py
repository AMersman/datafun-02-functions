"""
Ashley Mersman
Fundamentals of Data Analysis
1/23/23

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics as stats

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]
#use stats. to calculate central tendency for scores
mean = stats.mean(scores)
print(f"Mean is {mean}.")

median = stats.median(scores)
print(f"Median is {median}.")

mode = stats.mode(scores)
print(f"Mode is {mode}.")

variance = stats.variance(scores)
print(f"Variance is {round(variance,2)}.")

std_dev = stats.stdev(scores)
print(f"Std_Dev is {round(std_dev,2)}.")
# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

slope, intercept = stats.linear_regression(x_times,y_temps)
print(f"The slope of the best fit line is {round(slope,2)} and the intercept of the line is {round(intercept,2)}.")

#Use slope and intercept to forecase temperature at hour 13
x_future = 13
y_future = slope * x_future + intercept
print(f"At hour 13 the temperature shoule be {round(y_future,2)}C based on the previous data.")