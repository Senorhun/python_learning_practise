"""
inputWord = input('Input a word to translate to bird language: ')

for letter in inputWord:
    if letter == 'a' or letter == 'á' or letter == 'e' or letter == 'é' or letter == 'i' or letter == 'í' or letter == 'o' or letter == 'ó' or letter == 'u' or letter == 'ú':
        print(letter,'v', sep ="",end ="")
    print(letter, end="")
print("")
def is_vowel(inputWord):
    for letter in inputWord:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            print("magánhangzo")
        else:
            print("mássalhangzó")
        
is_vowel(inputWord)
"""

def vowel(letter):
   # return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'
    return letter.lower() in 'aeiou'

def bird_language(inputWord):
    result = ""
    for letter in inputWord:
        if vowel(letter):
            result += letter + 'v' + letter.lower()
        else:
            result += letter
    return result

def main():
    inputWord = input('Input a word: ')
    print(bird_language(inputWord))

main()