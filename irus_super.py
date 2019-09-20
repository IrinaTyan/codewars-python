def expression_matter(a, b, c):
    first = a*(b+c)
    second = a*b*c
    third = a+b*c
    fourth = (a+b)*c
    return max(first,second,third,fourth)


def find_needle(haystack):
    hey = haystack.index('needle') 
    return "found the needle at position " + str(hey)


def move(position, roll):
    return position + roll * 2

def other_angle(a, b):
    return 180 - (a+b)   


def square_sum(numbers):
    result = 0
    for x in numbers:
        result = result + x * x
    return result

# def square_sum(numbers):
    # return sum(x ** 2 for x in numbers)

# print(expression_matter(1,2,3))
# print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))
# print(move(3, 6))
# print(other_angle(30,60))
print(square_sum([1, 2]))