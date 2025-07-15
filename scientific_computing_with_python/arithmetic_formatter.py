def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_lines, second_lines, dashes, results = [], [], [], []

    for problem in problems:
        operator = '+' if '+' in problem else '-' if '-' in problem else None
        if operator is None:
            return "Error: Operator must be '+' or '-'."
        operand1, operand2 = [p.strip() for p in problem.split(operator)]
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        result = eval(f"{operand1} {operator} {operand2}")
        width = max(len(operand1), len(operand2)) + 2
        first_lines.append(operand1.rjust(width))
        second_lines.append(operator + operand2.rjust(width-1))
        dashes.append('-' * width)
        results.append(str(result).rjust(width))

    arranged_problems = '    '.join(first_lines) + '\n' + '    '.join(second_lines) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)
    
    arranged_problems = '    '.join(first_lines) + '\n' + '    '.join(second_lines) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems

print(f'\n{arithmetic_arranger(["3 + 698", "380 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["15 + 482", "346 - 9", "41 + 83", "58 / 44" , "68 * 289"])}')
print(f'\n{arithmetic_arranger(["15 + 482", "346 - 9", "41 + 83", "58 + 44" , "68 - 289"], True)}')
print(f'\n{arithmetic_arranger(["15 + 482", "346 - 9", "41 + 83", "58 + 44" , "68 - 289", "5 + 56"])}')