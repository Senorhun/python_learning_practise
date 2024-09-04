try:
    inputNumber = int(input('Please enter a number: '))
except (ValueError, Exception) as e:
    print(f'Error: {e}')
else:
    print('Success')
finally:
    print('This message was needed as a final touch')