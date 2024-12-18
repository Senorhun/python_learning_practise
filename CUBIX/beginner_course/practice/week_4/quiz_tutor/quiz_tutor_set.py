choco_type = {
    'kerek',
    'szögletes',
    'hosszú',
    'rövid',
}

print("Milyen csokoládét szeret Gombóc Artúr")
input_choco = set()
while True:
    choco = input("Input a choco type or 'end': ")
    if choco == 'end':
        break
    elif choco == '':
        continue
    elif choco in input_choco:
        print("Already said it")
    elif choco in choco_type:
        print("Yes!")
    else:
        print("Wrong..")
    input_choco.add(choco)
found_choco_type = choco_type.intersection(input_choco)
print("Matches: " + ", " .join(found_choco_type))
print(f"Grade: {(len(found_choco_type)/len(choco_type))*100}%")
print("Misses: " + ", " .join(choco_type.difference(found_choco_type)))



#    'gömbölyű',
#     'lapos',
#     'tömör',
#     'lyukas',
#     'csomagolt',
#     'meztelen',
#     'egész',
#     'megkezdett',
#     'édes',
#     'keserű',
#     'csöves',
#     'mogyorós',
#     'tej',
#     'likőrös',
#     'tavalyi',
#     'idei',