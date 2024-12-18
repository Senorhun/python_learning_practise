
user_input = input("Pick a month to find out, how many days does it long:  ")
month = ["january","february","march","april","may","june","july","august","september","october","november","december"]
if user_input not in month:
    print("Month does not exists...")
else:
    match user_input:
        case "february":
            print(f"{user_input} is 28/29 days long depends on the year")
        case "april" | "june" | "september" | "november":
            print(f"{user_input} is 30 days long")
        case _:
            print(f"{user_input} is 31 days long")