#WAP to remove a given word from a list and strip it at the same time

# l1 = ["sharan", "basappa", "cloud", "aws"]
# print(l1) 
# l1.remove("aws")
# print(l1)

#This is about how to strip
# st = "    This is to learn about strip        "
# print(st)
# print(st.strip())

#WAP to remove a given word from a string and strip it at the same time

def remove_and_strip(string, word):
    newstr = string.replace(word, "")
    return newstr.strip() 


that = "   I am sharan basappa     "
st = remove_and_strip(that, "sharan")
print(st)

