"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
def longest_caller(calls):
    message = "{} spent the longest time, {} seconds, on the phone during September 2016."
    phone_number_call_time = {}
    phone_number = ''
    call_time = 0

    for i in range(len(calls)):

        calling_number = calls[i][0]
        receiving_number = calls[i][1]
        seconds = int(calls[i][3])
        phone_number_call_time[calling_number] = phone_number_call_time.get(calling_number, 0) + seconds
        phone_number_call_time[receiving_number] = phone_number_call_time.get(receiving_number, 0) + seconds

    for key, seconds in phone_number_call_time.items():
        if call_time < seconds:
            call_time = seconds
            phone_number = key

    return message.format(phone_number, call_time)

print(longest_caller(calls))
