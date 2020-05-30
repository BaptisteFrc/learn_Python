from time import time 

start_time = time()

list_lines = []
list_value_element = [[0 for i in range(j)] for j in range(1,101)]
for _ in range(100):
    list_lines.append(list(map(int, input().split(" "))))


def maximum_path_sum(line, column):

    Value_element = list_value_element[line][column]
    if Value_element != 0:
        return Value_element


    if line == 99:
        return list_lines[line][column]

    else:
        value_left = maximum_path_sum(line + 1, column)
        value_right = maximum_path_sum(line + 1, column + 1)
        if value_left > value_right:
            value_element = value_left + list_lines[line][column]
            list_value_element[line][column] = value_element
            return value_element
        else:
            value_element = value_right + list_lines[line][column]
            list_value_element[line][column] = value_element
            return value_element

  
print(maximum_path_sum(0,0))
print(time() - start_time)
