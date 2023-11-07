from time import sleep

from main import read
data = read()
seconds = data['Second']
minutes = data['Minute']
hours = data['Hour']
days = data['Day']
weeks = data['Week']
mouths = data['Mouth']
years = data['Year']

while True:
    try:
        seconds += 1
        if seconds >= 59:
           seconds = 0
           minutes += 1
        if minutes >= 59:
           minutes = 0
           hours += 1
        if hours >= 24:
           hours = 0
           days += 1
        if days >= 7:
           days = 0
           weeks += 1
        if weeks >= 4:
           weeks = 0
           mouths += 1
        if mouths >= 12:
           mouths = 0
           years += 1
        sleep(1)
    except KeyboardInterrupt:
        with open('data.json', 'w') as f:
            data = f"""
                 "Year": {years},
                 "Mouth": {mouths},
                 "Week": {weeks},
                 "Day": {days},
                 "Hour": {hours},
                 "Minute": {minutes},
                 "Second": {seconds}"""
            f.write("{" + data + "}")
            f.close()
        break