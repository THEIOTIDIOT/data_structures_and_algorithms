"""
def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]

    return array[index] + sum_array_index(array, index + 1)


arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))
"""
"""
def recursion(listy, num):
    if len(listy) == 0:
        print('False')
        return False
    
    for item in listy:
        if isinstance(item, list):
            recursion(item, num)
        else:
            if num == item:
                print('True')
                return True
            else:
                continue

listy = [1,[1,2],[1,2,[1,88,3]]]
recursion(listy, 88)
"""
"""
def addDigits(num):


    new_num = 0
    num_str = str(num)

    for n in num_str:
        new_num += int(n)

    if num < 10:
        return num

    return addDigits(new_num)

num = 38
print(addDigits(num))
"""
def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    return return_permutation(string, 0)
def return_permutation(string, index):
    
    if index >= len(string):
        return [""]
    
    small_output = return_permutation(string, index + 1)
    output = []
    current_char = string[index]
    
    for permutation in small_output:
        for index in range(len(small_output[0]) + 1):
            new_permutation = permutation[0:index] + current_char + permutation[index:]
            output.append(new_permutation)
    return output

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)