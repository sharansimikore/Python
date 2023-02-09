letter = '''
Dear <|Name|>,
Greetings from Johnson Controls. I am happy to announce your selection 
Your are selected

Thanks and Redards,
Sharanbasappa
Date: <|Date|>'''

name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)