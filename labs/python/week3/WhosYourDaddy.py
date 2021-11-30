father_son_pairs = {
    'Sam': 'Darren',
    'Jacob': 'Darren',
    'Darren': 'Donald',
    'Nemo': 'Marlin',
    'Jaden': 'Will',
    'Will': 'Willard'
}

print('''
    WELCOME TO WHOS YOUR DADDY

        WOULD YOU LIKE TO
          1. FIND A PAIR
          2. ADD A PAIR
          3. REMOVE A PAIR
          4. REPLACE A PAIR

''')

choice = int(input('What would you like to do (1-4): '))

if choice == 1:
    name = input('Please enter the sons name: ')
    try:
        print(f'Their father is: {father_son_pairs[name]}')
    except Exception:
        print('That name is not in the database')

elif choice == 2:
    son = input('Sons Name: ')
    father = input('Fathers Name: ')
    father_son_pairs[son] = father
    print('Added')

elif choice == 3:
    print('SON     :     FATHER')
    for key in father_son_pairs.keys():
        print(key,' : ',father_son_pairs[key])

    print()
    son = input('Enter the name of the son in the pair you like to remove: ')
    father_son_pairs[son].remove()

elif choice == 4:
    print('SON     :     FATHER')

    for key in father_son_pairs.keys():
        print(key,' : ',father_son_pairs[key])
    
    son = input('Please enter the name of the son to edit their father: ')
    new_father = input('Please enter their new fathers name: ')
    father_son_pairs[son] = new_father