text = input("Enter a string\n")

if("my name is sharan" in text):
    spam = True
elif("karan" in text):
    spam = True
elif("charan" in text):
    spam = True
elif("haran" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is a spam")
else:
    print("Not a spam")    