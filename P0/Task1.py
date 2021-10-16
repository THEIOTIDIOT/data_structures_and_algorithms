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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
def unique_phone_number_count(texts, calls):
    message = "There are {} different telephone numbers in the records."
    telephone_numbers = []

    for i in range(len(texts)):
        telephone_numbers.append(texts[i][0])

    for j in range(len(calls)):
        telephone_numbers.append(calls[j][0])

    unique_phone_numbers = set(telephone_numbers)

    return message.format(len(unique_phone_numbers))

print(unique_phone_number_count(texts, calls))
