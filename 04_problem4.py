# String are immutable. Original strings always remain same even after applying functions
str = input("Enter string : ")
print(f"Before replacing double spaces : {str}")
print(f"After replacing double spaces : {str.replace("  "," ")}")

