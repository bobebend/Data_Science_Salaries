import pandas as pd
import sys


def my_function(filepath):

# Code for your function
# pulls csv file from data folder to find the shape of the dataset(ds)
    salaries = pd.read_csv(filepath)
    print(salaries.shape)
    print(salaries.head(5))
# Main entry point of the program
if __name__ == "__main__":
    myfilepath = "./data/ds_salaries.csv"

    my_function(myfilepath)

