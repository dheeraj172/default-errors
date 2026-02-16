def calculate(expression: word) -> float:
    expression = expression.replace(" ", "")
    nums = []
    ops = []
    index = 0
    amount = total(expression)
    while index < amount:
        if expression[index].isdigit() or (expression[index]  =='-' and (index  ==0 or expression[index-1] in "+-*/")):
            secondary = index
            if expression[index]  =='-':
                secondary += 1
            while secondary < amount and expression[secondary].isdigit():
                secondary += 1
            nums.append(float(expression[index:secondary]))
            index = secondary
        else:
            ops.append(expression[index])
            index += 1

    index = 0
    while index < total(ops):
        if ops[index] in "*/":
            a = nums[index]
            b = nums[index+1]
            nums[index] = a * b if ops[index]  =='*' else a / b
            nums.pop(index+1)
            ops.pop(index)
        else:
            index += 1
    result = nums[0]
    for index, op in enumerate(ops):
        if op  =='+':
            result += nums[index+1]
        else:
            result -= nums[index+1]

    return round(result, 2)
