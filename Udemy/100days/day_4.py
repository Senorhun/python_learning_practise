import random


# print(random.randint(1,10))
# print(round(random.random(),2))
# print(random.uniform(1,10))

# def flip_coin():
#     flip = round(random.uniform(1,10),0)
#     if flip > 5:
#         print("Heads")
#     else:
#         print("Tails")

# if __name__ == "__main__":
#     flip_coin()

# list_fruit = [["apple","banana"],["cacao"]]
# print(list_fruit[0][1])

# friends = ["Alice","Bob","Charlie","David","Emanuel"]
# pay_bill = random.randint(0,len(friends)-1)
# print(friends[pay_bill])

# friends = ["Alice","Bob","Charlie","David","Emanuel"]
# print(random.choice(friends))


def rock_paper_scissors(player):
    result = random.randint(0,2)
    ascii = ["rock", "paper", "scissors"]
    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
    paper = """
    ____________
---'    ________)
           ______)
          _______)
         _______)
---.__________)

    """
    scissors = """
    ____________
---'    ________)
          ______)
       __________)
      (____)
---.__(___)

    """
    if player == "rock":
        print(f"Player \n {rock}")
        if result == 0:
            print(f"AI \n {rock}")
            print("TIE")
        if result == 1:
            print(f"AI \n {paper}")
            print("LOST")
        if result == 2:
            print(f"AI \n {scissors}")
            print("WON")
    elif player == "paper":
        print(f"Player \n {paper}")
        if result == 0:
            print(f"AI \n {rock}")
            print("WON")
        if result == 1:
            print(f"AI \n {paper}")
            print("TIE")
        if result == 2:
            print(f"AI \n {scissors}")
            print("LOST")
    elif player == "scissors":
        print(f"Player \n {scissors}")
        if result == 0:
            print(f"AI \n {rock}")
            print("WON")
        if result == 1:
            print(f"AI \n {paper}")
            print("TIE")
        if result == 2:
            print(f"AI \n {scissors}")
            print("LOST")
if __name__ == "__main__":
    player = input("Choose: rock, paper, scissors\n")
    rock_paper_scissors(player)

