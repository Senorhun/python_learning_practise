questions = [
    "What is 2 + 2?  ",
    'What is "2" + "2"?  ',
    "What is 3 / 2?  ",
    "What is 3 // 2?  ",
    "What is 2 ** 3?  ",
]

answers = [
    4,
    22,
    1.5,
    1,
    8,
]

score = 0
number_of_questions = len(questions)
for i in range(len(questions)):
    if float(input((questions[i]))) == answers[i]:
        score += 1
        print("Well done!")
    else:
        print(f"Nope, right answer was {answers[i]}...")
print("Your result is: " + str(int((score / number_of_questions) * 100)) + "%")

print("---------------")

def LNKO(a, b):    
    while a != b:        
        if a > b:        
            a -= b        
        else:        
            b -= a        
    return a

def LKKT(a, b):
    return (a * b) // LNKO(a, b)

if __name__ == "__main__":
    a = 30
    b = 12
    
    print("Legnagyobb közös osztó (LNKO):", LNKO(a, b))
    print("Legkisebb közös többszörös (LKKT):", LKKT(a, b))
