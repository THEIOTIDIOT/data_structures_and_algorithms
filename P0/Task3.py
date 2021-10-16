"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def bangalore_codes_called(calls):

    message = "The numbers called by people in Bangalore have codes:\n"
    area_code_or_prefix = []
    area_code = ''

    for i in range(len(calls)):
        calling_number = calls[i][0]
        receiving_number = calls[i][1]

        if calling_number[0:5] == '(080)':
            if receiving_number[0] == '7' or receiving_number[0] == '8' or receiving_number[0] ==  '9':
                area_code_or_prefix.append(receiving_number[0:4])
            elif receiving_number[0:3] == '140':
                area_code_or_prefix.append('140')
            elif receiving_number[0] == '(':
                area_code = receiving_number[0:receiving_number.find(')') + 1]
                area_code_or_prefix.append(area_code)

    set_of_codes = sorted(set(area_code_or_prefix))

    for code in set_of_codes:
        message += code + '\n'

    return message

def fixed_bangalorian_calls(calls):
    message = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
    bangalore_fixed_line_calls_percentage = 0
    bangalore_caller_count = 0
    bangalore_to_bangalore_calls = 0

    for i in range(len(calls)):
        calling_number = calls[i][0]
        receiving_number = calls[i][1]

        if calling_number[0:5] == '(080)':
            bangalore_caller_count += 1

        if calling_number[0:5] == '(080)' and receiving_number[0:5] == '(080)':
            bangalore_to_bangalore_calls += 1

    bangalore_fixed_line_calls_percentage = (bangalore_to_bangalore_calls / bangalore_caller_count) * 100
    return message.format(round(bangalore_fixed_line_calls_percentage, 2))


print(bangalore_codes_called(calls))
print(fixed_bangalorian_calls(calls))
