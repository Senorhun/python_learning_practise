smurf_name = {
    'Tudor',
    'Vidor',
    'Szende',
    'Szundi',
    'Hapci',
    'Morgó',
    'Kuka',
}

print("Sorold fel a 7törpe neveit!")
input_smurf = set()
while True:
    smurf = input("Írj be egy nevet vagy kilépéshez 'vége': ").lower().capitalize()
    if smurf == 'Vége':
        break
    elif smurf == '':
        continue
    elif smurf in input_smurf:
        print("Már mondtad!")
    elif smurf in smurf_name:
        print("Eltaláltad!")
    else:
        print("Nem jó..")
    input_smurf.add(smurf)
found_smurf_name = smurf_name.intersection(input_smurf)
print("Matches: " + ", " .join(found_smurf_name))
print(f"Grade: {round((len(found_smurf_name)/len(smurf_name))*100,2)}%")
print("Misses: " + ", " .join(smurf_name.difference(found_smurf_name)))