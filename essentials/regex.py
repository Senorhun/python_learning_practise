import re

text = "Bono is a 122 lucky dog with an id: 122"
pattern = r"\d\d\d"
regex = re.compile(pattern)
#result = regex.findall(text)
#result = regex.search(text)
#result = regex.match(text)

#for match in regex.finditer(text):
#    print(f"starting index: {match.start()}, {match.group(0)}")

#result = regex.sub("OK", text)
result = regex.split(text)
print(result)