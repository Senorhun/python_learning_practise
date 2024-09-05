consumptionRoad= 7
consumptionCity= 9

onRoad = int(input('How much km do you travel on road?'))
inCity = int(input('How much km do you travel in the city?'))

toThereConsumption = (consumptionRoad*onRoad) + (consumptionCity*inCity)
print(f'Only to there consumption is', toThereConsumption, 'L')
toThereAndBackConsumption = 2 * ((consumptionRoad*onRoad) + (consumptionCity*inCity))
print(f'To there and back consumption is', toThereAndBackConsumption, 'L')
costOfDiesel = 350 * toThereAndBackConsumption
print('Total amount of money to pay for the diesel is', costOfDiesel, 'Ft')
