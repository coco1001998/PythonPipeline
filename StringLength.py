def strLength(my_string):
    len_count = 0
    for i in my_string:
        len_count = len_count + 1
    return len_count

my_string = "Hey, there! Please subscribe logicOps Lab!"
# 42

# driver code
str_len=strLength(my_string)

print("The length of the given string is :", str_len)
print("The length of the given string is :", len(my_string))