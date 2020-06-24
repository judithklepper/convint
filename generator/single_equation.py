import random
import pandas as pd


def generate_datum():
    operators = [['+', 'added with', 'plus'], ['-', 'minus', 'extracted by'], ['*', 'multiplied by', 'times'],
                 ['/', 'divided by']]
    numbers = [['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'], ['7', 'seven'],
               ['8', 'eight'],
               ['9', 'nine'], ['10', 'ten']]
    tree = generate_tree(operators, numbers)
    return tree


def tree_to_sentence(tree):
    tree = tree
    options = ['what is', 'I would like to know what is', 'How many is', 'I want to calculate']
    option = random.choice(options)

    sentence = option + " " + tree.get('left') + " " + tree.get('operator') + " " + tree.get('right') + "?"
    return sentence


def operator_string_to_abs(tree):
    tree = tree
    operators = [['+', 'added with', 'plus'], ['-', 'minus', 'extracted by'], ['*', 'multiplied by', 'times'],
                 ['/', 'divided by']]

    for i in operators:
        if tree.get('operator') in i:
            operator = i[0]
            return operator


def number_string_to_int_left(tree):
    tree = tree
    numbers = [['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'], ['7', 'seven'],
               ['8', 'eight'],
               ['9', 'nine'], ['10', 'ten']]

    for j in numbers:
        if tree.get('left') in j:
            left = j[0]
            return left


def number_string_to_int_right(tree):
    tree = tree
    numbers = [['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'], ['7', 'seven'],
               ['8', 'eight'],
               ['9', 'nine'], ['10', 'ten']]

    for j in numbers:
        if tree.get('right') in j:
            right = j[0]
            return right


def tree_to_prefix(tree):
    operator = operator_string_to_abs(tree)
    left = number_string_to_int_left(tree)
    right = number_string_to_int_right(tree)

    prefix = operator + " " + left + " " + right
    return prefix


def tree_to_infix(tree):
    operator = operator_string_to_abs(tree)
    left = number_string_to_int_left(tree)
    right = number_string_to_int_right(tree)
    infix = left + " " + operator + " " + right
    return infix


def generate_tree(operators, numbers):
    root = random.choice(random.choice(operators))
    left = random.choice(random.choice(numbers))
    right = random.choice(random.choice(numbers))

    return {
        'operator': root,
        'left': left,
        'right': right
    }


def gen_output():
    L = []
    for i in range(40000):
        tree = generate_datum()
        string = tree_to_sentence(tree)
        infix = tree_to_infix(tree)
        prefix = tree_to_prefix(tree)
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