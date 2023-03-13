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


def custom_log(val: float):
    if val == 0.0:
        return 1.0
    return math.log2(val)


def calc_gain(distinct_values: dict, records: list, dependent_variable: str, attribute: str, **given):
    filtered_records = [record for record in records if check_if_given_is_present(record, **given)]
    total_dataset_count = len(filtered_records)
    entropy_sv = 0
    entropy = 0

    for value in distinct_values[dependent_variable]:
        count = 0
        total_count = total_dataset_count
        for record in filtered_records:
            if record[dependent_variable] == value:
                count += 1
        # print(f"{count}/{total_count}")
        entropy += (-1) * (count / total_count) * custom_log(count / total_count)
    # print(f"total_entropy of filtered set is {entropy}")

    for attr_type in distinct_values[attribute]:
        entropy_per_val = 0
        total_count_distinct = 0
        for value in distinct_values[dependent_variable]:
            count = 0
            total_count = 0
            for record in filtered_records:
                if record[attribute] == attr_type:
                    total_count += 1
                    if record[dependent_variable] == value:
                        count += 1
            # print(f"{count}/{total_count}")
            total_count_distinct = total_count
            if total_count != 0:
                entropy_per_val += (-1) * (count / total_count) * custom_log(count / total_count)
        # print(f"entropy of {attr_type} is {entropy_per_val}")
        # print(f'Sv/S = {total_count_distinct}/{len(filtered_records)}')
        entropy_sv += (total_count_distinct / len(filtered_records)) * entropy_per_val
    return entropy - entropy_sv


class TreeNode:
    def __init__(self, path):
        self.path = path
        self.value = None
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def construct_tree_recursive(distinct_values, records, dependent_variable, columns, node, path):
    max_gain_value = 0.0
    max_gain_attr = ''

    if len(columns) == 0:
        filtered_records = [record for record in records if check_if_given_is_present(record, **path)]
        node.value = f'final decision: {filtered_records[0][dependent_variable]}'
        return

    for column in columns:
        gain = calc_gain(distinct_values, records, dependent_variable, column, **path)
        # print(f'{column}: {gain}')
        # print(path)
        if gain > max_gain_value:
            max_gain_value = gain
            max_gain_attr = column

    # print(f"\n\n{max_gain_attr}: {max_gain_value}")
    # print(path)
    node.value = max_gain_attr

    if max_gain_value == 0.0:
        filtered_records = [record for record in records if check_if_given_is_present(record, **path)]
        node.value = f'final decision: {filtered_records[0][dependent_variable]}'
        return

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
    traverse_tree_bfs_levels(root, file_name='play_tennis_id3.txt')


if __name__ == '__main__':
    main()
