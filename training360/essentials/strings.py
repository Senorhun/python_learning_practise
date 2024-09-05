word = "apple"
#  a  p  p  l  e
#  0  1  2  3  4
# -5 -4 -3 -2 -1

print(f" using '0' index to print the letter: {word[0]}")
print(f" using '-5' reverse index to print the letter: {word[0-5]}")

print(f" using '[1:]' to print from include index: {word[1:]}")
print(f" using '[1:4]' to print from include index till exclude index: {word[1:4]}")
print(f" using '[1:4:2]' to print from include index till exclude index jumping every 2: {word[1:4:2]}")
print(f" using '[::-1]' to print reverse: {word[::-1]}")

word2 = "There is an apple."
word2= word2.replace(" ", "")
print(word2)

word2 = "There is an apple."
word2 = word2.split(" ")
word2.reverse()
print(word2)

word2 = "There is an apple."
print(f"There are {word2.count("e")} 'e' in the stirng: {word2}")
print(f"There is {word2.count("an")} 'an' in the stirng: {word2}")
print(f"The snippet 'an' in the string starts at index: {word2.find("an")}")

word3 = "apple is good"
word3 = word3.split()
print(word3)

word3 = "apple"
word3 = list(word3)
print(word3)
word3.reverse()
print(word3)

list = [0,1,2,3,4]
new_list = list.copy()
print(new_list)


