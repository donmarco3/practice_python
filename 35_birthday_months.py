# load the json file from disk
# extract the months of the birtdays
# count how many people have birthdays in each month

import json
from collections import Counter

with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

months = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}

months_list = []
for item in birthdays.values():
    months_list.append(months[item[:2]])

print(Counter(months_list))
