import random
import pandas as pd


def nested_tree():
    operators = [['+', 'added with', 'plus'], ['-', 'minus', 'extracted by'], ['*', 'multiplied by', 'times'],
                 ['/', 'divided by']]
    numbers = [['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'], ['7', 'seven'],
               ['8', 'eight'],
               ['9', 'nine'], ['10', 'ten']]

    nested_operators = []
    nested_numbers = []

    for i in range(2):
        nested_operators.append(random.choice(random.choice(operators)))

    for i in range(3):
        nested_numbers.append(random.choice(random.choice(numbers)))

    root = nested_operators[0]
    number_root = nested_numbers[0]

    nested_root = nested_operators[1]
    nested_number_left = nested_numbers[1]
    nested_number_right = nested_numbers[2]
    return {
        'root': root,
        'number_root': number_root,
        'nested_root': nested_root,
        'nested_number_left': nested_number_left,
        'nested_number_right': nested_number_right
    }


def operator_string_to_abs(operator):
    operators = [['+', 'added with', 'plus'], ['-', 'minus', 'extracted by'], ['*', 'multiplied by', 'times'],
                 ['/', 'divided by']]

    for i in operators:
        if operator in i:
            operator = i[0]
            return operator


def number_string_to_int(number):
    numbers = [['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'], ['7', 'seven'],
               ['8', 'eight'],
               ['9', 'nine'], ['10', 'ten']]

    for j in numbers:
        if number in j:
            number = j[0]
            return number


def absolute_operators_int(tree):
    nested_left = number_string_to_int(tree.get('nested_number_left'))
    nested_operator = operator_string_to_abs(tree.get('nested_root'))
    nested_right = number_string_to_int(tree.get('nested_number_right'))
    number_root = number_string_to_int(tree.get('number_root'))
    root = operator_string_to_abs(tree.get('root'))
    return {
        'root': root,
        'number_root': number_root,
        'nested_operator': nested_operator,
        'nested_number_left': nested_left,
        'nested_number_right': nested_right
    }


def nested_to_string(tree):
    options = ['what is', 'I would like to know what is', 'How many is', 'I want to calculate']
    option = random.choice(options)
    sentence = option + " " + tree.get('nested_number_left') + " " + tree.get('nested_root') + " " + tree.get(
        'nested_number_right') + " " + tree.get('root') + " " + tree.get('number_root') + "?"
    return sentence


def nested_to_infix(tree):
    numbers_and_operators = absolute_operators_int(tree)
    infix = "(" + numbers_and_operators['nested_number_left'] + " " + numbers_and_operators['nested_operator'] + " " + \
            numbers_and_operators['nested_number_right'] + ")" + " " + numbers_and_operators['root'] + " " + \
            numbers_and_operators['number_root']
    return infix


def nested_to_prefix(tree):
    numbers_and_operators = absolute_operators_int(tree)
    prefix = numbers_and_operators['root'] + " " + "(" + numbers_and_operators['nested_operator'] + " " + \
             numbers_and_operators['nested_number_left'] + " " + numbers_and_operators[
                 'nested_number_right'] + ")" + " " + numbers_and_operators['number_root']
    return prefix


def gen_output():
    L = []
    for i in range(1000):
        tree = nested_tree()
        string = nested_to_string(tree)
        infix = nested_to_infix(tree)
        prefix = nested_to_prefix(tree)
        row = {'string': string, 'infix': infix, 'prefix': prefix}
        L.append(row)
    return L


def make_dataframe():
    d = {'string': ['What is 1 - 2'], 'infix': ['1-2'], 'prefix': ['- 1 2']}
    df = pd.DataFrame(data=d)
    df.append(d, ignore_index=True)
    df = df.append(gen_output(), ignore_index=True)
    return df


make_dataframe()