from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print(f"Today's date is {today}")
print(f"Current date and time is {now}")

print('Date components: ', today.year, today.month, today.day)