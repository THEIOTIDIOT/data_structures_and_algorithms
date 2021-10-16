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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def potential_telemarketers(texts, calls):
    message = "These numbers could be telemarketers: \n"
    callers = []
    answerers = []
    texters = []
    text_recipients = []
    telemarketers = []

    for i in range(len(calls)):
        callers.append(calls[i][0])
        answerers.append(calls[i][1])

    for j in range(len(texts)):
        texters.append(texts[j][0])
        text_recipients.append(texts[j][1])

    callers_set = set(callers)
    answerers_set = set(answerers)
    texters_set = set(texters)
    text_recipients_set = set(text_recipients)


    callers_set -= answerers_set
    callers_set -= texters_set
    callers_set -= text_recipients_set
    telemarketers = list(sorted(callers_set))

    for telemarketer in telemarketers:
        message += (telemarketer + "\n")

    return message

print(potential_telemarketers(texts, calls))
