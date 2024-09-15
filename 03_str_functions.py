# String Function
str = "sukkur IBA university"
print(len(str))
print(str.endswith("sity"))
print(str.startswith("Suk"))
print(str.capitalize())
print(str.find("IBA"))  # IBA is on index 7
print(str.replace("sukkur","karachi"))
print(str) # original string str would be same
print(str.upper())
print(str.lower())
print(str.title()) # convert first letter of each word to upper case
print(str.strip()) # remove extra white spaces
print(str.split()) # ['sukkur', 'IBA', 'university']
print(str.isalpha())
str = '12'
print(str.isdigit()) # Returns True if all characters in the string are digits.
# Returns True if all characters in the string are alphanumeric (letters and numbers).
print(str.isalnum())

