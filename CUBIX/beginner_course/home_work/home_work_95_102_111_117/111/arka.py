arka = "Nem minden fajta szarka farka tarkabarka, csak a tarkabarka farkú szarkafajta farka tarkabarka, mert ha minden fajta szarka farka tarkabarka volna, akkor minden szarkafajta tarkabarka-farkú szarkafajta volna."

print("------Hibás megoldás-------")
arka_list = arka.split(' ')
counter = 0
for word in arka_list:
    if 'arka' in word:
        counter += 1
print(f"There are {counter} occurrences in the arka tale.")
print("Hibás verzió, mivel szavanként(elemenként) csak 1x ellenőrzi benne van-e 'arka' vagy sem.")

print("\n------Helyes megoldás-------")
counter = 0
counter = arka.count("arka")
print(f"There are {counter} occurrences in the arka tale.")
