import pandas as pd
import math
import pprint
from collections import deque
from typing import List


def fill_dependent_variable(records, dependent_variable):
    for record in records:
        if record[dependent_variable['name']] not in dependent_variable:
            dependent_variable[record[dependent_variable['name']]] = 1
        else:
            dependent_variable[record[dependent_variable['name']]] += 1


def fill_independent_variable(records, independent_variables, dependent_variable):
    for record in records:
        for variable in independent_variables.keys():
            if record[variable] not in independent_variables[variable]:
                independent_variables[variable][record[variable]] = {key: 0 for key in dependent_variable.keys() if
                                                                     key != 'name'}
            independent_variables[variable][record[variable]][record[dependent_variable["name"]]] += 1


def predict(classify, independent_variables, dependent_variable):
    p_yes = dependent_variable['Yes']
    p_no = dependent_variable['No']
    total = p_yes + p_no

    p_yes_total = p_yes / total
    p_no_total = p_no / total

    for key, value in classify.items():
        p_yes_total = p_yes_total * (independent_variables[key][value]['Yes'] / p_yes)
        p_no_total = p_no_total * (independent_variables[key][value]['No'] / p_no)

    print(p_yes_total)
    print(p_no_total)
    # Yes, No
    return p_yes_total / (p_yes_total + p_no_total), p_no_total / (p_yes_total + p_no_total)


def main():
    dataset = pd.read_csv('PlayTennis.csv')
    columns = list(dataset.columns)[:-1]
    records = dataset.to_dict('records')
    dependent_variable = {'name': 'Play Tennis'}

    fill_dependent_variable(records, dependent_variable)
    independent_variables = {col: {} for col in columns}
    fill_independent_variable(records, independent_variables, dependent_variable)
    classify = {"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "High", "Wind": "Strong"}
    Yes, No = predict(classify, independent_variables, dependent_variable)
    if Yes > No:
        print(f"{dependent_variable['name']} = Yes")
    else:
        print(f"{dependent_variable['name']} = No")


if __name__ == '__main__':
    main()
