# use the code from exercise 17 and write the results to a new text file

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


with open('ny_times_headings.txt', 'w') as open_file:
    for heading in soup.find_all(class_='css-5mgoji'):
        if (heading.text != ''):
            open_file.write(f'{heading.text} \n')
