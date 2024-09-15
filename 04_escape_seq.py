str = "Islamabas is the capital of Pakistan"
print(str)
# \n is used to shift substring on next line
str = "Islamabas is the \n capital of Pakistan"
print(str) # Islamabas is the
           #  capital of Pakistan


str = "Islamabas is the \n capital \t of \t Pakistan"
# Islamabas is the
# capital         of      Pakistan
print(str) # like tab space


str = "'Islamabas' \'is\' the \"capital\" of Pakistan \\"
print(str) # Islamabas is the "capital" of Pakistan \

str = "abc\rdef" # skip the previous string text
print(str) # def

str = "abcd\befgh"
print(str) # Backspace (deletes the previous character). Output: abcefgh

str = "Austra\filia"
print(str) # Output : ilia

str = "Wali\vngton"
print(str)  #Output : # Wali
                      # ngton 

str = r"abcdef\nghijk"
print(str) # fix the string by using r
           # \n is treated like string