def expression_matter(a, b, c):
    first = a*(b+c)
    second = a*b*c
    third = a+b*c
    fourth = (a+b)*c
    return max(first,second,third,fourth)


def find_needle(haystack):
    hey = haystack.index('needle') 
    return "found the needle at position " + str(hey)



# print(expression_matter(1,2,3))
# print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))
