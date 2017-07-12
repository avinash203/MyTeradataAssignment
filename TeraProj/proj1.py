f= open("sample.txt")
text=f.read()
ext = text.find(':')
result = text[ext+1:]
print(result)
