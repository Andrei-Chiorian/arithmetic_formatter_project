def arithmetic_arranger(problems, show_answers=False):
    first_line = []
    second_line = []
    operators = []
    result_line = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        split_problem = problem.split(' ')
        if split_problem[1] != '+' and split_problem[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not split_problem[0].isdigit() or not split_problem[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if not len(split_problem[0]) <= 4 or not len(split_problem[2]) <= 4:
            return 'Error: Numbers cannot be more than four digits.'
        first_line.append(split_problem[0])
        second_line.append(split_problem[2])
        operators.append(split_problem[1])
        result = int(split_problem[0]) + int(split_problem[2]) if split_problem[1] == '+' else int(
            split_problem[0]) - int(split_problem[2])
        result_line.append(str(result))

    first_line = [
        ' ' * (len(second_line[index]) - len(element)) + element
        if len(element) < len(second_line[index])
        else element
        for index, element in enumerate(first_line)
    ]

    second_line = [
        operators[index] + ' ' + ' ' * (len(first_line[index]) - len(element)) + element
        if len(element) < len(first_line[index])
        else operators[index] + ' ' + element
        for index, element in enumerate(second_line)
    ]

    first_line = [
        ' ' * 2 + element
        for element in first_line
    ]

    result_line = [
        ' ' * (len(second_line[index]) - len(element)) + element
        for index, element in enumerate(result_line)
    ]

    dash_line = [
        '-' * len(second_line[index])
        for index, element in enumerate(second_line)
    ]
    first_line = first_line[0] + '    ' + '    '.join(first_line[1:])
    second_line = second_line[0] + '    ' + '    '.join(second_line[1:])
    result_line = result_line[0] + '    ' + '    '.join(result_line[1:])
    dash_line = dash_line[0] + '    ' + '    '.join(dash_line[1:])

    problems = first_line + '\n' + second_line + '\n' + dash_line + ('\n' + result_line if show_answers else '')

    return problems


print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')
