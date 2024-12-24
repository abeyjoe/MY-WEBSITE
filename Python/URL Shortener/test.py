# pip install pyshorteners
# pip install pyperclip

import pyshorteners

url = input('Enter the url: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)



fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I love ",fruit)

print("")
count = 0

while count < 5:
    print(count)
    count += 1

print("")
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is: ", grade)


print(len("Glorious day"))