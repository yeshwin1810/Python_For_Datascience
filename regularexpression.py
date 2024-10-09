#Check if the string starts with "The" and ends with "Spain":
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")


#Using findall
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x,'(Output by using findall)')

import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x,'(Output by using findall)')


text = "The cat sat on the mat. The dog barked at the cat. Cats and dogs live in harmony."
x = re.findall(r"cat|dog", text, re.IGNORECASE)
print(x)

import re
txt = "The rain in Spain"
x = re.search(r"\s", text)
print("The first white-space character is located in position:",
x.start(),'(Using search)')

#split
y = re.split(r"\s", text)
print(y)

y = re.split(r"\s", text, 1)
print(y)

y = re.sub(r"\s", "8", text)
print(y)


text1 = """Contact us at support@example.com, sales@company.org, or admin@website.net.
For more information, visit www.example.com."""

x = re.findall(r"example", text, re.IGNORECASE) 
print(x,'/n')

#Using Search
x = re.search("\s", text)
print("The first white-space character is located in position:",
x.start(),'(Using search)')

#Using Split
x = re.split(r"\s", text1)
print(x)

x = re.split(r"\s", text1, 1)
print(x)

#Match object
x = re.search("the", text1)
print(x) 

x = re.search(r"\bi\w+", text1)
print(x.span())

x = re.search(r"\bi\w+", text1)
print(x.string)



