# GRPA 1

def DishPrepareOrder(order_list):
    (d, d_new) = ({}, {})
    for order in order_list:
        if order in d:
            d[order] += 1
        else:
            d[order] = 1
    for key in d:
        if d[key] in d_new:
            d_new[d[key]].append(key)
        else:
            d_new[d[key]] = [key]
    # store the max occurance in a list and sort it
    order_no_list = []
    [order_no_list.append(key) for key in d_new.keys()]
    order_no_list.sort()
    new_order_list = []
    while len(order_no_list) > 0:
        new_array = d_new[order_no_list[-1]]
        new_array.sort()
        [new_order_list.append(order) for order in new_array]
        order_no_list = order_no_list[0:len(order_no_list)-1]
    return new_order_list


nums = eval(input())
print(DishPrepareOrder(nums))


# GRPA 2

def operation(a, b, operator):
    if operator == "+":
        return a+b
    if operator == "-":
        return a-b
    if operator == "*":
        return a*b
    if operator == "/":
        return a/b
    if operator == "**":
        return a**b


def EvaluateExpression(exp):
    exp_new = exp.split(" ")
    stack = []
    for e in exp_new:
        if e.isnumeric():
            stack.append(float(e))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(operation(a, b, e))
    return stack[0]


print(float(EvaluateExpression(input())))


# GRPA 3

def reverse(root):
    prev = None
    current = root
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
