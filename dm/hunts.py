import pandas as pd
import math
import pprint
from collections import deque
from typing import List


def check_if_given_is_present(record: dict, **given):
    if len(given) == 0:
        return True

    for key in given.keys():
        if given[key] != record[key]:
            return False
    return True


def check_if_pure(records: list, dependent_variable: str, **given):
    filtered_records = set(
        [record[dependent_variable] for record in records if check_if_given_is_present(record, **given)])
    if len(filtered_records) > 1:
        return False
    return True


class TreeNode:
    def __init__(self, path):
        self.path = path
        self.value = None
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def construct_tree_recursive(distinct_values, records, dependent_variable, columns, node, path):
    max_gain_attr = ''

    if check_if_pure(records, dependent_variable, **path):
        filtered_records = [record for record in records if check_if_given_is_present(record, **path)]
        # print(path)
        if len(filtered_records) == 0:
            return
        node.value = f'final decision: {filtered_records[0][dependent_variable]}'
        return

    if len(columns) == 0:
        filtered_records = [record for record in records if check_if_given_is_present(record, **path)]
        node.value = f'final decision --- not pure: {filtered_records[0][dependent_variable]}'
        return

    # print(columns[0])
    max_gain_attr = columns[0]
    node.value = max_gain_attr

    for attr_type in distinct_values[max_gain_attr]:
        new_node = TreeNode(path={**path, max_gain_attr: attr_type})
        node.add_child(new_node)
        new_columns = [column for column in columns if column != max_gain_attr]
        construct_tree_recursive(distinct_values, records, dependent_variable, new_columns, new_node,
                                 {**path, max_gain_attr: attr_type})


def driver(distinct_values, records, dependent_variable, columns):
    root = TreeNode(path=None)
    construct_tree_recursive(distinct_values, records, dependent_variable, columns, root, {})
    return root


def traverse_tree_bfs_levels(root, file_name: str):
    f = open(file_name, 'w')
    queue = deque()
    queue.append(root)
    curr_level_count = 1
    next_level_count = 0

    while queue:
        node = queue.popleft()
        curr_level_count -= 1
        f.write(f'{node.value}={node.path}    ')

        for child in node.children:
            queue.append(child)
            next_level_count += 1

        if curr_level_count == 0:
            f.write('\n\n\n\n')
            curr_level_count = next_level_count
            next_level_count = 0


def main():
    dataset = pd.read_csv('PlayTennis.csv')

    columns = list(dataset.columns)
    records = dataset.to_dict('records')
    dependent_variable = 'Play Tennis'

    distinct_values = {col: set() for col in columns}

    for column in columns:
        for record in records:
            distinct_values[column].add(record[column])

    root = driver(distinct_values, records, dependent_variable, columns[:-1])
    traverse_tree_bfs_levels(root, file_name='hunts.txt')


if __name__ == '__main__':
    main()
