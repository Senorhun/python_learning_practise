print("-----for cycle-----")
result_list = []
for item in range(1, 11):
    if item % 2 == 0:
        result_list.append(item)
print(result_list)

print("-----list comprehension-----")
print([item for item in range(1, 11) if item % 2 == 0])

print("-----list comprehension exercise 1-----")
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_length = []
for word in words:
    if word != "the":
        word_length.append(len(word))
print(word_length)

print([len(word) for word in words if word != "the"])