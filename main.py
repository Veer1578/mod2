import random
import time

def get_random_date(start_date, end_date):
    print(f'A random date between {start_date} and {end_date}')
    date_format = "%m/%d/%Y"

    start = time.mktime(time.strptime(start_date, date_format))
    end = time.mktime(time.strptime(end_date, date_format))

    random_time = start + random.random() * (end - start)

    random_date = time.strftime(date_format, time.localtime(random_time))
    return random_date

print('Random date = ', get_random_date('01/01/2016', '12/12/2018'))
