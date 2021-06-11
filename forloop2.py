# def biggie(num_list):
#     for i in range(len(num_list)):
#         if num_list[i] > 0:
#             num_list[i] = "big"
#         return num_list

# print(biggie([-1, 3, 5, -5]))

            
# def count(num_list):
#     new_val = 0
#     for x in range(len(num_list)):
#         if x > 0:
#             new_val += 1
#     num_list[len(num_list) - 1] = new_val
#     return num_list

# print(count([-1, 1, 1, 1]))


# def total(num_list):
#     sum = 0
#     for x in range(len(num_list) + 1):
#         sum += x
#     return sum

# print(total([1, 2, 3, 4]))


# def average(num_list):
#     sum = 0
#     for x in range(len(num_list) + 1):
#         sum += x
    
#     return float(sum) / float(len(num_list))

# print(average([1, 2, 3, 4]))



# def length(num_list):
#     new_list = []
#     x = len(num_list)
#     return x

# print(length([37, 2, 1, -9]))


# def minimum(num_list):
#     if len(num_list) == 0:
#         return False
#     result = num_list[0]
#     for x in num_list:
#         if x < result:
#             result = x
#     return result

# print(minimum([3, 2, 1, -9]))


# def max(num_list):
#     if len(num_list) == 0:
#         return False
#     result = num_list[0]
#     for x in num_list:
#         if x > result:
#             result = x
#     return result

# print(max([37, 2, 1, -9]))




def ultimate_analysis(num_list):
    result = {
        'sum': None,
        'max': None,
        'min': None,
        'avg': None,
        'length': 0,
    }
    if len(num_list) == 0:
        return result
    else:
        result['sum'] = 0
        result['max'] = num_list[0]
        result['min'] = num_list[0]

    for val in num_list:
        if val > result['max']:
            result['max'] = val
        elif val < result['min']:
            result['min'] = val

        result['sum'] += val
        result['length'] += 1
    result['avg'] = result['sum'] / len(num_list)

    return result

print(ultimate_analysis([37, 2, 1, -9]))



def reverse(num_list):
    new = int(len(num_list) / 2)
    for x in range(new):
        num_list[x], num_list[len(num_list) - 1 - x] = num_list[len(num_list) - 1- x], num_list[x]
    return num_list
print(reverse([37, 2, 1, -9]))