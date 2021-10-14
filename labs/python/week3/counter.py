while True:
    try:
        start_number = int(input('Please enter the start number: '))
    except Exception:
        print('---Please enter a number---')
    else:
        break

while True:
    try:
        end_number = int(input('Please enter the end number: '))
    except Exception:
        print('---Please enter a number---')
    else:
        break

while True:
    try:
        step = int(input('Please enter the number you would like to increment by: '))
    except Exception:
        print('---Please enter a number---')
    else:
        break

print([i for i in range(start_number, end_number+1, step)])
