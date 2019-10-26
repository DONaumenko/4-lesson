def multiplication(*args):
    # print(type(args))
    result = 1
    for number in args:
        result *= number  # result = result * number
    return result


print(multiplication(2, 3))
print(multiplication(2, 3, 4))
print(multiplication(2, 3, 4, 5))
print(multiplication(1))


def multiplication(numbers):
    # print(type(numbers))
    result = 1
    for number in numbers:
        result *= number  # result = result * number
    return result


print(multiplication([2, 3]))
print(multiplication([2, 3, 4]))
print(multiplication([2, 3, 4, 5]))
print(multiplication([1]))



