"""Task: to resolve the rebus. Need to understand how it hided and output the secret word."""

a = [{6, 'A'},
     (5, 'R'), (13, 'O'),
     {2: 'O'}, {1: 'C'},
     [3, 'N'],
     {'hah,trick': {4: 'G'}},
     7, 'T', 8, 'U', 9, 'L', 10, 'A',
     {15: 'S'}, {14: 'N'}, {11: 'T'}, {12: 'I'}
     ]


# Function which receive a list, check the type of all elements and make from them list of similar lists inside
def rebus(task):
    # list for our result
    result = []

    # general loop for going through all incoming list
    for element in task:

        # checking element type if set
        if type(element) == set:
            element = list(element)
            # additional check to be sure that on the [0] index we have integer for result output loop
            if type(element[0]) != int:
                element[0], element[1] = element[1], element[0]
            result.append(element)

        # checking element type if tuple
        elif type(element) == tuple:
            new_element = list(element)
            result.append(new_element)

        # checking element type if dict
        elif type(element) == dict:
            new_element = [[key, value] for key, value in element.items()]
            result.extend(new_element)

        # checking element type if list
        elif type(element) == list:
            # additional check to be sure that on the [0] index we have integer for result output loop
            if type(element[0]) != int:
                element[0], element[1] = element[1], element[0]
                result.append(element)
            result.append(element)

        # checking element type if it simple separate int then we create list of this element and second one
        elif type(element) == int:
            new_element = task[task.index(element)], task[task.index(element) + 1]
            new_element1 = list(new_element)
            result.append(new_element1)

    # additional checking for hided dictionaries in the result and convert it also to list
    for element in result:
        if type(element[1]) == dict:
            new_element = [[key, value] for key, value in element[1].items()]
            result.remove(element)
            result.extend(new_element)

    # output of results
    for i in range(len(result) + 1):
        for elem in result:
            if elem[0] == i:
                print(elem[1], end='')


if __name__ == '__main__':
    rebus(a)
