# plot a histogram of which months have birthdays in it

import json
from collections import Counter
from bokeh.plotting import figure, show, output_file
import math

output_file('plot.html')

with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

num_to_month = {
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
    months_list.append(num_to_month[item[:2]])
months_list = Counter(months_list)

months, count = list(zip(*months_list.items()))

categories = list(num_to_month.values())
p = figure(x_range=categories)
p.xaxis.major_label_orientation = math.pi/4
p.vbar(x=months, top=count)

show(p)
