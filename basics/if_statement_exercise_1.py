userAge = int(input('How old are you? -> '))
drink = input('What can I serve you, beer or cola? ->')
if userAge <18 and drink == 'beer':
 print('You are too young to drink Beer')
elif userAge >=60 and drink == 'cola':
 print('Be aware of coffenie causing high bloodpreasure in your age')
elif drink != "beer" and drink != "cola":
 print('Sorry but we only have Beer and Cola...')
else:
 print('Here is your', drink,'enjoy!')