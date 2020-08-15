char = input("Enter a character: ")
if (char >= 'A' and char <= 'Z'):
    char = char.lower()
    print("The Entered Character is UpperCase. In LowerCase It is " + char)
else:
    char = char.upper()
    print("The Entered Character is LowerCase. In UpperCase It is " + char)
