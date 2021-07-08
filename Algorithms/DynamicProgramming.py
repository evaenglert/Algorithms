import numpy as np


def findOptimalValue(items, costs, values, max_cost):
    # fist find the smallest cost to get an idea how granular our matrix should be
    minimal_cost = min(costs.values())

    # These are needed to get matrix dimensions
    granularity = max_cost // minimal_cost
    number_of_items = len(items)

    # Initalize matrices
    value_matrix = np.zeros((number_of_items, granularity))
    item_matrix = np.empty([number_of_items, granularity], dtype="S40")

    item_to_check = items[0]
    for i in range(0, granularity):

        if (i + 1) * minimal_cost < costs[item_to_check]:
            value_matrix[0][i] = 0

        else:
            value_matrix[0][i] = values[item_to_check]
            item_matrix[0][i] = item_to_check

    for j in range(1, number_of_items):
        item_to_check = items[j]
        cost_of_item = costs[item_to_check]
        value_of_item = values[item_to_check]

        for i in range(0, granularity):
            previous_max = value_matrix[j - 1][i]

            current_max_cost = max_cost // granularity * (i + 1)

            remainder_cost = current_max_cost - cost_of_item

            if remainder_cost > 0:

                value_with_new = value_of_item + value_matrix[j - 1][remainder_cost - 1]
                new_items = item_to_check + str(item_matrix[j - 1][remainder_cost - 1])

            elif remainder_cost == 0:
                value_with_new = value_of_item
                new_items = item_to_check
            else:
                value_with_new = 0

            if previous_max >= value_with_new:
                value_matrix[j][i] = previous_max
                item_matrix[j][i] = item_matrix[j - 1][i]
            else:
                value_matrix[j][i] = value_with_new
                item_matrix[j][i] = new_items

    return item_matrix


def findLongestCommonSubstring(text_one, text_two):
    length_one = len(text_one)
    length_two = len(text_two)

    value_matrix = np.zeros((length_one, length_two))

    for i in range(0, length_two):
        if text_two[i] == text_one[0]:
            value_matrix[0][i] = 1
        else:
            value_matrix[0][i] = 0

    for i in range(0, length_one):
        if text_one[i] == text_two[0]:
            value_matrix[i][0] = 1
        else:
            value_matrix[i][0] = 0

    for i in range(1, length_two):
        for j in range(1, length_one):
            if text_one[j] == text_two[i]:
                value_matrix[j][i] = value_matrix[j - 1][i - 1] + 1
            else:
                value_matrix[j][i] = 0

    return value_matrix.max()
