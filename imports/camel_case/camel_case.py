import camelcase
text1 = "there is an apple on the table."
text2 = camelcase.CamelCase().hump(text1)
print(text1)
print(text2)