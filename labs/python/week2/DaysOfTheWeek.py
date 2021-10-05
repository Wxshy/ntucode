week = {
    'monday' : '9-3, gym and hockey',
    'tuesday' : 'actually in person',
    'wednesday' : 'BUCS GAMEDAYYYYYYYYY',
    'thursday' : 'recovery day',
    'friday' : 'programming support',
    'saturday' : 'LEAGUE GAMEDAYYYYYYYYY',
    'sunday' : 'recovery day'
}

while True:
    day = input('Please enter a day of the week or q to exit: ')
    if day == 'q': break
    try:
        print(week[day.lower()])
    except Exception:
        print('Please enter a valid input')
    
