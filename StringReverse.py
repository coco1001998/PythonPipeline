def strLength(my_string):
    reverseString = ""
    for i in my_string:
        #print(i)
        reverseString = i + reverseString
    return reverseString

my_string = "Hey, there!"

# driver code
str_rev=strLength(my_string)

print("The reverse string is :", str_rev)
print("The reverse string is :", my_string[::-1])