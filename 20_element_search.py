# check whether number in in list

import random

random_list = [random.randint(1, 100) for _ in range(10)]
number = random.randint(1, 100)

if number in random_list:
    print(f'{number} is in the list')
else:
    print(f'{number} is not in the list')
