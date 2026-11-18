# Check whether a string is a palindrome without using slicing.

text = "madam"
reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")