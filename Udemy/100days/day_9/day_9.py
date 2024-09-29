def bidding():
    bid_dict = {}
    contin = True
    while contin:
        name = input("bidder's name:  ")
        bid = int(input("how much do u bid:  "))
        bid_dict[name] = bid
        while True:
            contin_str = input("Is there another bidder yes or no?  ")
            if contin_str == "yes" or contin_str == "no":
                if contin_str == "no":
                    contin = False
                    break
                elif contin_str == "yes":
                    break
                else:
                    print("\n" *10)              
            print("Please choose: yes or no?   ")

    return bid_dict

def counting(bid_dict):
    biggest = 0
    winner = ""
    for bidder in bid_dict:
        if bid_dict[bidder] > biggest:
            biggest = bid_dict[bidder]
            winner = bidder
    return [winner,biggest]



if __name__ == "__main__":
    print("Welcome to the secret auction")
    result_list = counting(bidding())
    print(f"{result_list[0]} won the auction by {result_list[1]} ")
