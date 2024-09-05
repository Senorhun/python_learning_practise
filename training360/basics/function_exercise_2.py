wordList = ['apple','melon','banana', '']
counter  = 0

for word in wordList:
    if len(word) == 0:
        continue
    if word[0] == "a":
        counter = counter +1
        
verb = 'is'
if counter > 1:
    verb = 'are'

word = 'word'
if counter > 1:
    word = 'words'

print(f'There {verb} {counter} {word} in the list beginning with an "a"')